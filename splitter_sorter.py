import os
import shutil

# Set the path to the folder you want to sort
SOURCE_FOLDER = r"PATH_TO_YOUR_FOLDER"

# Create output folders
RAW_FOLDER = os.path.join(SOURCE_FOLDER, "RAW")
JPEG_FOLDER = os.path.join(SOURCE_FOLDER, "JPEG")

os.makedirs(RAW_FOLDER, exist_ok=True)
os.makedirs(JPEG_FOLDER, exist_ok=True)

# Define file extensions
RAW_EXTENSIONS = [".cr2", ".nef", ".arw", ".dng", ".rw2", ".orf", ".sr2"]
JPEG_EXTENSIONS = [".jpg", ".jpeg"]

# Sort files
for filename in os.listdir(SOURCE_FOLDER):
    file_path = os.path.join(SOURCE_FOLDER, filename)
    if os.path.isfile(file_path):
        _, ext = os.path.splitext(filename.lower())
        if ext in RAW_EXTENSIONS:
            shutil.move(file_path, os.path.join(RAW_FOLDER, filename))
        elif ext in JPEG_EXTENSIONS:
            shutil.move(file_path, os.path.join(JPEG_FOLDER, filename))

print("Sorting complete.")
