"""Run in Rhino 8 with _RunPythonScript after building/package extraction.

Set FOTON_GH_BUNDLE to an extracted ZIP and FOTON_HONEYBEE_EXE to the CLI.
Writes automated smoke evidence; does not claim fresh-install or manual UI checks.
"""
from __future__ import print_function
import json
import os
import shutil
import tempfile
import traceback


def main():
    import clr
    clr.AddReference("Grasshopper")
    clr.AddReference("GH_IO")
    import Grasshopper as gh
    from Grasshopper.Kernel import GH_Document, GH_RuntimeMessageLevel
    from Grasshopper.Kernel.Types import GH_Boolean, GH_String, GH_Number
    from Grasshopper.Kernel.Special import GH_BooleanToggle
    from GH_IO.Serialization import GH_Archive
    root = os.environ["FOTON_GH_BUNDLE"]
    executable = os.environ["FOTON_HONEYBEE_EXE"]
    output = tempfile.mkdtemp(prefix="foton-rhino-check-")
    report = {"scope": "automated_existing_Rhino_profile", "checks": {}, "output": output}
    path = os.path.join(root, "Foton First Analysis.gh")
    archive = GH_Archive()
    archive.ReadFromFile(path)
    document = GH_Document()
    if not archive.ExtractObject(document, "Definition"):
        raise RuntimeError("Cannot read example definition")
    document.FilePath = path
    gh.Instances.DocumentServer.AddDocument(document)
    previous_enabled = GH_Document.EnableSolutions
    try:
        GH_Document.EnableSolutions = True
        document.Enabled = True
        settings = next(o for o in document.Objects if o.Name == "Foton Settings")
        annual = next(o for o in document.Objects if o.Name == "Foton Annual Daylight")
        results = next(o for o in document.Objects if o.Name == "Foton Annual Results")
        factor = next(o for o in document.Objects if o.Name == "Foton Daylight Factor")
        def set_input(obj, name, value):
            p = next(p for p in obj.Params.Input if p.Name == name)
            p.RemoveAllSources()
            p.PersistentData.Clear()
            if isinstance(value, bool):
                p.PersistentData.Append(GH_Boolean(value))
            elif isinstance(value, (int, float)):
                p.PersistentData.Append(GH_Number(value))
            else:
                p.PersistentData.Append(GH_String(value))
        def values(obj, name):
            p = next(p for p in obj.Params.Output if p.Name == name)
            return [str(v) for v in p.VolatileData.AllData(True)]
        def result_path():
            path = os.path.realpath(values(annual, "manifest")[0])
            # IronPython does not resolve macOS's /var -> /private/var symlink.
            return path[len("/private"):] if path.startswith("/private/var/") else path
        def solve():
            for obj in document.Objects:
                obj.ExpireSolution(False)
            document.NewSolution(True)
            errors = dict((o.Name, list(o.RuntimeMessages(GH_RuntimeMessageLevel.Error))) for o in (settings, annual, results, factor))
            if any(errors.values()):
                raise RuntimeError(json.dumps(errors))
        set_input(settings, "executable_", executable)
        set_input(annual, "output_folder_", os.path.join(output, "annual"))
        set_input(factor, "output_folder_", os.path.join(output, "daylight_factor"))
        for obj in document.Objects:
            if isinstance(obj, GH_BooleanToggle):
                obj.Value = True
        solve()
        first = result_path()
        da = values(annual, "DA")
        report["checks"]["run"] = bool(da)
        report["checks"]["reload_results"] = da == values(results, "DA")
        report["backend"] = values(settings, "backend")[0]
        report["engine_version"] = values(settings, "engine_version")[0]
        saved_df = values(factor, "DF")
        report["checks"]["daylight_factor"] = bool(saved_df) and bool(values(factor, "results"))
        solve()
        report["reuse_report"] = values(annual, "report")
        report["reuse_paths"] = [first, values(annual, "manifest")[0]]
        report["checks"]["reuse"] = result_path() == first and any("Reused compatible results" in value for value in values(annual, "report"))
        # An older solver identity must not be accepted as current results.
        with open(first) as stream:
            old_manifest = json.load(stream)
        old_manifest["reuse_identity"]["provenance"]["engine_version"] = "older-test-version"
        with open(first, "w") as stream:
            json.dump(old_manifest, stream)
        solve()
        upgraded = result_path()
        report["checks"]["upgrade_invalidates_reuse"] = upgraded != first
        set_input(annual, "north_", 90.0)
        solve()
        report["checks"]["changed_inputs_new_folder"] = result_path() != upgraded
        # Live mode: the background worker returns the saved run's values,
        # writes nothing, and reuses its traced coefficients for new thresholds.
        saved_da = values(annual, "DA")
        set_input(annual, "live_", True)
        set_input(factor, "live_", True)
        solve()
        report["checks"]["live_matches_saved"] = (
            values(annual, "DA") == saved_da
            and values(factor, "DF") == saved_df
            and not values(annual, "results")
            and not values(factor, "results")
        )
        set_input(annual, "thresholds_", "-t 500 -lt 100 -ut 3000")
        solve()
        report["live_timings"] = values(annual, "timings_text")
        report["checks"]["live_reuses_coefficients"] = (
            values(annual, "DA") != saved_da
            and any("coefficient_trace_seconds: 0.0" in value for value in values(annual, "timings_text"))
        )
        set_input(annual, "live_", False)
        set_input(factor, "live_", False)
        set_input(annual, "thresholds_", "-t 300 -lt 100 -ut 3000")
        # Exercise portable result loading after a real move of an owned test folder.
        moved = os.path.join(output, "moved")
        shutil.move(os.path.dirname(first), moved)
        set_input(results, "_manifest", os.path.join(moved, "run_manifest.json"))
        # Avoid rerunning annual while checking standalone reload.
        annual.Locked = True
        document.NewSolution(True)
        report["checks"]["moved_results"] = da == values(results, "DA") and not list(results.RuntimeMessages(GH_RuntimeMessageLevel.Error))
        from grasshopper_foton.foton_gh import run_annual_daylight, FotonCancelled
        try:
            run_annual_daylight(os.path.join(root, "examples", "shoebox.hbjson"), os.path.join(root, "examples", "gothenburg.epw"), os.path.join(output, "cancelled"), executable=executable, reuse=False, cancel=lambda: True)
            report["checks"]["cancel_external_process"] = False
        except FotonCancelled:
            report["checks"]["cancel_external_process"] = not os.path.isfile(os.path.join(output, "cancelled", "run_manifest.json"))
        import Rhino
        report["rhino_version"] = str(Rhino.RhinoApp.Version)
    except Exception:
        report["error"] = traceback.format_exc()
    finally:
        GH_Document.EnableSolutions = previous_enabled
        gh.Instances.DocumentServer.RemoveDocument(document)
        report["passed"] = not report.get("error") and bool(report["checks"]) and all(report["checks"].values())
        target = os.path.join(output, "rhino-smoke.json")
        with open(target, "w") as stream:
            json.dump(report, stream, indent=2)
        print(target)


if __name__ == "__main__":
    main()
