import { spawn } from "node:child_process";
import { existsSync } from "node:fs";
import { fileURLToPath } from "node:url";
import path from "node:path";

const scriptDirectory = path.dirname(fileURLToPath(import.meta.url));
const viewerDirectory = path.resolve(scriptDirectory, "..");
const repositoryDirectory = path.resolve(viewerDirectory, "..");
const pythonRoot = path.join(repositoryDirectory, "python");
const pathSeparator = process.platform === "win32" ? ";" : ":";
const localVirtualEnvironment = path.join(repositoryDirectory, ".venv");
const configuredVirtualEnvironment = process.env.VIRTUAL_ENV;
const virtualEnvironment = configuredVirtualEnvironment && existsSync(configuredVirtualEnvironment)
  ? configuredVirtualEnvironment
  : existsSync(localVirtualEnvironment) ? localVirtualEnvironment : undefined;
const pythonCommand = process.env.PYTHON ?? (
  virtualEnvironment
    ? path.join(
        virtualEnvironment,
        process.platform === "win32" ? "Scripts/python.exe" : "bin/python",
      )
    : process.platform === "win32" ? "python" : "python3"
);
const environment = {
  ...process.env,
  PYTHONPATH: [pythonRoot, process.env.PYTHONPATH].filter(Boolean).join(pathSeparator),
};

const frontendCommand = process.platform === "win32" ? "npm.cmd" : "npm";
const frontend = spawn(frontendCommand, ["run", "dev:frontend"], {
  cwd: viewerDirectory,
  env: environment,
  stdio: "inherit",
  shell: false,
});
const backend = spawn(pythonCommand, ["-m", "foton.viewer", "--reload"], {
  cwd: repositoryDirectory,
  env: environment,
  stdio: "inherit",
  shell: false,
});

let shuttingDown = false;
const stop = (code = 0) => {
  if (shuttingDown) return;
  shuttingDown = true;
  frontend.kill("SIGTERM");
  backend.kill("SIGTERM");
  setTimeout(() => process.exit(code), 250);
};

frontend.on("exit", (code) => {
  if (!shuttingDown) stop(code ?? 1);
});
backend.on("exit", (code) => {
  if (!shuttingDown) stop(code ?? 1);
});
frontend.on("error", (error) => {
  console.error(`Frontend failed to start: ${error.message}`);
  stop(1);
});
backend.on("error", (error) => {
  console.error(`Backend failed to start: ${error.message}`);
  stop(1);
});
process.on("SIGINT", () => stop());
process.on("SIGTERM", () => stop());
