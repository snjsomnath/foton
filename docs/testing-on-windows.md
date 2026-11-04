# Testing Foton on Windows

Thanks for helping test Foton on Windows. Foton has been tested on Macs and on a
Linux cloud machine, but not yet on a Windows PC. A test on your computer helps
everyone who uses Rhino on Windows.

There are four parts. Together they take about an hour, most of it waiting for
installs and the benchmark.

1. Install Foton in Rhino 8 from the Package Manager.
2. Run the example file in Grasshopper.
3. Install Foton with Python on its own.
4. Run the speed benchmark and send the result.

**You need Foton 0.3.3 or newer.** The Package Manager listing, the automatic
install inside Grasshopper and the HB-Foton toolbar tab are new in 0.3.3. Check
the version at the top of [pypi.org/project/foton-daylight](https://pypi.org/project/foton-daylight/).
The steps below say 0.3.3; if a newer version is out, use that number instead.

**Please do the parts in this order.** Parts 1 and 2 test the route for people
who have never installed Python. If you install Python first (Part 3), that
route is skipped. If Python 3.10 to 3.13 is already on your computer, that's
fine, just mention it in your report.

While you work, keep a note of anything that confuses you, any error message and
how long each step takes. Screenshots help a lot (Windows key + Shift + S).

## Before you start: check your computer

Foton needs a graphics card with ray-tracing hardware and an up-to-date driver.
These work:

- **NVIDIA:** any RTX card (RTX 20, 30, 40 or 50 series, or an RTX workstation card).
- **AMD:** Radeon RX 6000 series or newer.
- **Intel:** Arc graphics.

Older cards, such as NVIDIA GTX, don't have ray tracing. Foton still runs on
them, but in a slow backup mode that uses only the processor. That's still worth
testing, but say so in your report and skip the benchmark in Part 4.

To find your card and driver:

1. Press Ctrl + Shift + Esc to open Task Manager.
2. Click **Performance**, then the **GPU** entry. The card's name is at the top
   right. Note the **Driver version** further down.
3. Take a screenshot of this page for your report.

Please update your graphics driver before you start:
[NVIDIA](https://www.nvidia.com/Download/index.aspx),
[AMD](https://www.amd.com/en/support) or
[Intel](https://www.intel.com/content/www/us/en/download-center/home.html).
If you have a laptop, plug it in.

You also need:

- **Rhino 8** (Rhino 7 won't work).
- **Ladybug Tools** installed in Rhino, from
  [food4rhino.com/app/ladybug-tools](https://www.food4rhino.com/en/app/ladybug-tools).
  The example file uses its Honeybee components.
- An internet connection. If your office network uses a proxy, it may block
  some downloads. Note it if so.

## Part 1: Install Foton in Rhino 8

1. Open Rhino 8. Type `PackageManager` and press Enter.
2. Search for **foton**. Select it, check the version, and click **Install**.
3. Close and reopen Rhino.
4. Open Package Manager again and click the **Installed** tab. **foton** should
   be in the list. Take a screenshot.
5. Type `Grasshopper` and press Enter. Look for an **HB-Foton** tab on the
   Grasshopper toolbar, with four components. Each one should have its own icon
   and show the Foton version underneath. Take a screenshot.
6. Double-click an empty spot on the Grasshopper canvas and type **Foton**. The
   four components should show up in the search.

## Part 2: Run the example in Grasshopper

The example file came with the package.

1. Open File Explorer, paste this into the address bar and press Enter:

   ```
   %APPDATA%\McNeel\Rhinoceros\packages\8.0\foton\0.3.3
   ```

2. Open **Foton First Analysis.gh** in Grasshopper. It holds a small shaded room
   with Gothenburg weather.
3. Find the **Foton Settings** component and set its `install_` toggle to
   **True**. Foton now sets itself up in a `.foton` folder in your user folder.
   If there is no Python on your computer, it first downloads its own copy. This
   runs in the background, so Rhino stays usable. The component shows how long
   it has been running, and its `report` output lists each step. It takes a few
   minutes. Note roughly how long, and take a screenshot when it finishes.
4. Set `_check` on Foton Settings to **True**. The report should show the Foton
   version and say **Vulkan** with your graphics card's name. If it says **CPU**
   or **reference** instead, that's important: take a screenshot.
5. Set `_run` on **Foton Annual Daylight** to **True**. The first run takes a
   little longer because it prepares the weather data. Note how long it takes,
   then set it to False and True again and note the time of the second run too.
6. Optional: connect `results` to **HB Annual Daylight Metrics**, and its `DA`
   output with the room's sensor grid mesh to **LB Spatial Heatmap**, to see the
   colours on the room in Rhino. Take a screenshot.
7. Optional: set `live_` to **True** on Foton Annual Daylight and change an
   input, such as the daylight threshold. After the first run, results should
   update within a few seconds.

If anything goes wrong, copy the full text of the `report` output (connect a
Panel to it) and include it in your report. To start the install again from
scratch, close Rhino and delete the `.foton` folder in `C:\Users\<your name>`.

## Part 3: Install Foton with Python

This is the route for people who script with Python instead of Grasshopper. It
is also what the benchmark in Part 4 uses.

1. If you don't have Python, install **Python 3.12** from
   [python.org/downloads/windows](https://www.python.org/downloads/windows/).
   On the first screen of the installer, tick **Add python.exe to PATH**. If you
   already have Python 3.10, 3.11 or 3.13, you can skip the download and use
   that number instead of 3.12 in the commands below.
2. Open **PowerShell** from the Start menu. Type each line below and press Enter
   after each one. The first makes a separate folder for this test, so nothing
   else on your computer is affected. The second installs Foton into it.

   ```
   py -3.12 -m venv $HOME\foton-test
   & $HOME\foton-test\Scripts\python -m pip install "foton-daylight[honeybee]==0.3.3"
   ```

3. Check that Foton finds your graphics card:

   ```
   & $HOME\foton-test\Scripts\python -c "from foton import Engine; print(Engine().capabilities())"
   ```

   Look for `vulkan` and your card's name in the output. Copy the whole output
   into your report. If it says `reference` instead, Foton couldn't use your
   card, and that's important to report.

To remove everything from this part afterwards, delete the `foton-test` folder
in your user folder.

## Part 4: Run the speed benchmark

The benchmark times Foton on four building models, from one small room up to a
256-room office block, and saves the times in one file. It also times the same
steps the Grasshopper component goes through. It saves its results inside the
folder you unzip. Skip this part if Foton said `reference` or CPU in Part 3.

1. Download the Foton source for your version:
   [github.com/snjsomnath/foton/archive/refs/tags/v0.3.3.zip](https://github.com/snjsomnath/foton/archive/refs/tags/v0.3.3.zip).
   Right-click the zip, choose **Extract All**, and extract it to your user
   folder. You should end up with a folder called `foton-0.3.3`.
2. Close other heavy programs, including Rhino. Keep a laptop plugged in.
3. In PowerShell, run:

   ```
   cd $HOME\foton-0.3.3
   & $HOME\foton-test\Scripts\python scripts\benchmark_suite.py
   ```

   Leave it alone until it finishes. It takes about two minutes on a fast Mac,
   so allow up to 20 minutes. If it stops with an error, copy all the text in
   the window into your report.

4. When it's done, open the folder `foton-0.3.3\benchmarks\machines`. Inside is
   a new folder named after your processor and graphics card, with one `.json`
   file in it. That file is your result.

The file lists your Windows version, processor, graphics card, driver, memory,
Python and Foton versions, and your computer's network name. If you'd rather not
share the name, open the file in Notepad, find your computer's name and replace
it with something like `my-pc`.

### Sending the result as a pull request

This adds your computer to Foton's public speed table, with your name on the
change. You only need a GitHub account and a web browser.

1. Sign in to GitHub and open
   [github.com/snjsomnath/foton/tree/main/benchmarks/machines](https://github.com/snjsomnath/foton/tree/main/benchmarks/machines).
2. Click **Add file**, then **Upload files**. GitHub may say it will make your
   own copy (a fork) of the project first. That's expected; agree to it.
3. In File Explorer, open `foton-0.3.3\benchmarks\machines`. Drag the folder
   named after your computer (not just the file inside it) onto the GitHub page.
4. Under **Commit changes**, type `Benchmark: <your processor> and <your graphics card>`,
   for example `Benchmark: Ryzen 9 7950X and RTX 4080`.
5. Click **Propose changes**, then **Create pull request** on the next page, and
   once more to confirm.

If you use git, [CONTRIBUTING.md](../CONTRIBUTING.md#adding-your-computer-to-the-benchmarks)
has the same steps from the command line.

## What to report

Open an [issue](https://github.com/snjsomnath/foton/issues/new/choose) titled
"Windows test: <your graphics card>" with these. If a part didn't work, send what
you have; a failed step is as useful as a working one.

- Graphics card name and driver version (the Task Manager screenshot).
- Windows version (Start, type `winver`), Rhino version (Help > About
  Rhinoceros) and Ladybug Tools version.
- Whether Python was already installed before you started, and which version.
- Part 1: screenshots of the Installed tab and the HB-Foton toolbar tab.
- Part 2: the full `report` text from Foton Settings after install and after
  check, how long the install took, and how long the first and second runs took.
- Part 2: a screenshot of the heatmap, if you got that far.
- Part 3: the full output of the check command.
- Part 4: the link to your benchmark pull request.
- Any error message, copied as text, plus a screenshot of where it appeared.
- Anything that was confusing, slow or not what you expected, even small things.

Before posting, remove any private project paths or names from the text you paste.
