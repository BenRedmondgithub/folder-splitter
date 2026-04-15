# Photo Sorter - Build Executable Instructions

## Overview
This guide will help you create a standalone executable (.exe) file from your Python photo sorter GUI application.

## Prerequisites
You need Python with pip installed on your system. If you don't have pip available, you'll need to install it first.

## Method 1: Automatic Build (Recommended)

### Step 1: Install Python with pip
If you don't have pip available, install Python from:
- Download from: https://www.python.org/downloads/
- During installation, make sure to check "Add Python to PATH" and "Install pip"

### Step 2: Run the build script
```bash
python build_executable.py
```

This script will:
- Automatically install PyInstaller if needed
- Build the executable with optimized settings
- Create `PhotoSorter.exe` in the `dist` folder

## Method 2: Manual Build

### Step 1: Install PyInstaller
```bash
pip install pyinstaller
```

### Step 2: Build the executable
```bash
pyinstaller --onefile --windowed --name=PhotoSorter "splitter_sorter GUI.py"
```

### Command Explanation:
- `--onefile`: Creates a single executable file
- `--windowed`: Hides the console window (for GUI apps)
- `--name=PhotoSorter`: Sets the executable name
- `"splitter_sorter GUI.py"`: Your Python script

## Method 3: Using requirements.txt
```bash
pip install -r requirements.txt
pyinstaller --onefile --windowed --name=PhotoSorter "splitter_sorter GUI.py"
```

## Result
After successful build, you'll find:
- `dist/PhotoSorter.exe` - Your standalone executable
- This file can be run on any Windows machine without Python installed

## Troubleshooting

### If pip is not found:
1. Install Python from python.org (ensure pip is included)
2. Or use: `python -m ensurepip --upgrade`

### If build fails:
1. Make sure you're using the correct Python executable
2. Try: `python -m PyInstaller --onefile --windowed --name=PhotoSorter "splitter_sorter GUI.py"`

### Antivirus warnings:
Some antivirus software may flag the executable as suspicious. This is normal for PyInstaller-created executables.

## File Size
The executable will be around 15-20 MB because it includes the Python interpreter and all necessary libraries.
