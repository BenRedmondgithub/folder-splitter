#!/usr/bin/env python3
"""
Build script to create an executable from the photo sorter GUI application.
This script uses PyInstaller to create a standalone executable.
"""

import os
import sys
import subprocess
import shutil

def install_pyinstaller():
    """Install PyInstaller if not already installed."""
    try:
        import PyInstaller
        print("PyInstaller is already installed.")
        return True
    except ImportError:
        print("Installing PyInstaller...")
        try:
            # Try installing with pip
            subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
            print("PyInstaller installed successfully.")
            return True
        except subprocess.CalledProcessError:
            print("Failed to install PyInstaller automatically.")
            print("Please install it manually with: pip install pyinstaller")
            return False

def build_executable():
    """Build the executable using PyInstaller."""
    script_name = "splitter_sorter GUI.py"
    
    if not os.path.exists(script_name):
        print(f"Error: {script_name} not found in current directory.")
        return False
    
    # PyInstaller command to create a single executable file
    cmd = [
        sys.executable, "-m", "PyInstaller",
        "--onefile",           # Create single executable
        "--windowed",          # Don't show console window for GUI app
        "--name=PhotoSorter",  # Name of the executable
        "--clean",             # Clean temporary files
        script_name
    ]
    
    print(f"Building executable from {script_name}...")
    print("This may take a few minutes...")
    
    try:
        subprocess.check_call(cmd)
        print("\nBuild completed successfully!")
        print(f"Executable created in: dist/PhotoSorter.exe")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Build failed with error: {e}")
        return False

def main():
    """Main build process."""
    print("=== Photo Sorter Executable Builder ===\n")
    
    # Install PyInstaller if needed
    if not install_pyinstaller():
        return False
    
    # Build the executable
    if build_executable():
        # Check if executable was created
        exe_path = "dist/PhotoSorter.exe"
        if os.path.exists(exe_path):
            size_mb = os.path.getsize(exe_path) / (1024 * 1024)
            print(f"\nExecutable details:")
            print(f"  Location: {os.path.abspath(exe_path)}")
            print(f"  Size: {size_mb:.1f} MB")
            print(f"\nYou can now run PhotoSorter.exe on any Windows machine!")
        return True
    else:
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
