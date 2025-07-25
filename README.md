# About Me
Hey, my name is Ben Redmond. I am a Student of Web design & Software development, and I am also a photographer.

# The issue

So, I shoot a lot when I'm on location, and what breaks my heart is that after the shoot, I have around 250 to 300 images, and I have to sort them into folders, RAW and JPEG, for the next step which is the editing.

# The solutions

One day, I got sick of the process that I've been using for the last five years and decided to develop a script to sort through the RAW and JPEG files, then place them into their own folders. I used Python for ease of use. The first script worked well; however, you needed to manually feed it the path in the source code, which was fine, but I wanted a GUI to make it more useful. For this step, I used tkinter cause I just needed something simple and clean.

there are a few verions of the script in this repo. there is a terminal verion and a GUI verions

# Photo Sorter GUI

A simple Python GUI application that automatically sorts RAW and JPEG photo files into separate folders.

## Features

- Automatically sorts RAW files (CR2, NEF, ARW, DNG, RW2, ORF, SR2) into a "RAW" folder
- Automatically sorts JPEG files (JPG, JPEG) into a "JPEG" folder
- Handles file name conflicts by adding numbered suffixes
- Simple and intuitive graphical user interface
- Cross-platform compatibility

## Requirements

- Python 3.6 or higher
- tkinter (usually included with Python)

## Installation

1. **Clone or download this repository:**
   ```bash
   git clone <your-repo-url>
   cd folder-splitter
   ```

2. **Verify Python installation:**
   ```bash
   python --version
   ```
   
   If Python is not installed, download it from [python.org](https://www.python.org/downloads/)

3. **Check if tkinter is available (optional):**
   ```bash
   python -c "import tkinter; print('tkinter is available')"
   ```

## Usage

### Running the Application

1. **Navigate to the project directory:**
   ```bash
   cd folder-splitter
   ```

2. **Run the script:**
   ```bash
   python "splitter_sorter GUI.py"
   ```

### Using the GUI

1. Click the **"Select Folder and Sort"** button
2. Browse and select the folder containing your photos
3. The application will automatically:
   - Create "RAW" and "JPEG" subfolders (if they don't exist)
   - Move RAW files to the "RAW" folder
   - Move JPEG files to the "JPEG" folder
   - Show a completion message with the number of files moved

### File Handling

- **Supported RAW formats:** CR2, NEF, ARW, DNG, RW2, ORF, SR2
- **Supported JPEG formats:** JPG, JPEG
- **File conflicts:** If a file with the same name already exists in the destination folder, the application automatically adds a numbered suffix (e.g., `photo_1.jpg`, `photo_2.jpg`)

## Example

**Before sorting:**
```
MyPhotos/
├── IMG_001.cr2
├── IMG_001.jpg
├── IMG_002.nef
├── IMG_003.jpeg
└── vacation.dng
```

**After sorting:**
```
MyPhotos/
├── RAW/
│   ├── IMG_001.cr2
│   ├── IMG_002.nef
│   └── vacation.dng
├── JPEG/
│   ├── IMG_001.jpg
│   └── IMG_003.jpeg
```

## Troubleshooting

### Common Issues

1. **"No module named 'tkinter'" error:**
   - On Ubuntu/Debian: `sudo apt-get install python3-tk`
   - On CentOS/RHEL: `sudo yum install tkinter`
   - On macOS: tkinter should be included with Python

2. **Permission errors:**
   - Ensure you have read/write permissions for the target folder
   - Try running as administrator (Windows) or with sudo (Linux/macOS)

3. **Files not moving:**
   - Check that the files have the correct extensions
   - Ensure the source folder contains actual files (not shortcuts/symlinks)

### Getting Help

If you encounter any issues:
1. Check that Python 3.6+ is installed
2. Verify file permissions
3. Ensure the folder contains supported file types

## License

This project is open source and available under the [MIT License](LICENSE).

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
