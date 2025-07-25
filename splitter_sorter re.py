import os
import shutil

# Set the path to the folder you want to sort
SOURCE_FOLDER = r"E:\\tester"

# Create output folders
RAW_FOLDER = os.path.join(r"E:\\tester", "RAW")
JPEG_FOLDER = os.path.join(r"E:\\tester", "JPEG")

os.makedirs(RAW_FOLDER, exist_ok=True)
os.makedirs(JPEG_FOLDER, exist_ok=True)

# Define file extensions
RAW_EXTENSIONS = [".cr2", ".nef", ".arw", ".dng", ".rw2", ".orf", ".sr2"]
JPEG_EXTENSIONS = [".jpg", ".jpeg"]

# Sort files
for filename in os.listdir(SOURCE_FOLDER):
    # Skip the output folders themselves
    if filename in ["RAW", "JPEG"]:
        continue
        
    file_path = os.path.join(SOURCE_FOLDER, filename)
    if os.path.isfile(file_path):
        _, ext = os.path.splitext(filename.lower())
        
        try:
            if ext in RAW_EXTENSIONS:
                destination = os.path.join(RAW_FOLDER, filename)
                # Handle duplicate files by adding a number
                counter = 1
                while os.path.exists(destination):
                    name, ext_with_dot = os.path.splitext(filename)
                    destination = os.path.join(RAW_FOLDER, f"{name}_{counter}{ext_with_dot}")
                    counter += 1
                shutil.move(file_path, destination)
                print(f"Moved RAW: {filename}")
                
            elif ext in JPEG_EXTENSIONS:
                destination = os.path.join(JPEG_FOLDER, filename)
                # Handle duplicate files by adding a number
                counter = 1
                while os.path.exists(destination):
                    name, ext_with_dot = os.path.splitext(filename)
                    destination = os.path.join(JPEG_FOLDER, f"{name}_{counter}{ext_with_dot}")
                    counter += 1
                shutil.move(file_path, destination)
                print(f"Moved JPEG: {filename}")
                
        except Exception as e:
            print(f"Error moving {filename}: {e}")

print("Sorting complete.")
