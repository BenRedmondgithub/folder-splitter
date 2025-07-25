import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

# Define file extensions
RAW_EXTENSIONS = [".cr2", ".nef", ".arw", ".dng", ".rw2", ".orf", ".sr2"]
JPEG_EXTENSIONS = [".jpg", ".jpeg"]

def safe_move(src, dst_folder):
    base, ext = os.path.splitext(os.path.basename(src))
    dst_path = os.path.join(dst_folder, base + ext)
    counter = 1
    while os.path.exists(dst_path):
        dst_path = os.path.join(dst_folder, f"{base}_{counter}{ext}")
        counter += 1
    shutil.move(src, dst_path)

def sort_photos(folder):
    raw_folder = os.path.join(folder, "RAW")
    jpeg_folder = os.path.join(folder, "JPEG")

    os.makedirs(raw_folder, exist_ok=True)
    os.makedirs(jpeg_folder, exist_ok=True)

    moved = 0
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        if os.path.isfile(file_path):
            _, ext = os.path.splitext(filename.lower())
            if ext in RAW_EXTENSIONS:
                safe_move(file_path, raw_folder)
                moved += 1
            elif ext in JPEG_EXTENSIONS:
                safe_move(file_path, jpeg_folder)
                moved += 1

    messagebox.showinfo("Done", f"Sorting complete.\nFiles moved: {moved}")

def browse_and_sort():
    folder_selected = filedialog.askdirectory(title="Select Folder to Sort")
    if folder_selected:
        sort_photos(folder_selected)

# GUI setup
root = tk.Tk()
root.title("Photo Sorter")
root.geometry("300x150")
root.resizable(False, False)

label = tk.Label(root, text="Sort RAW and JPEG files into folders", pady=20)
label.pack()

sort_button = tk.Button(root, text="Select Folder and Sort", command=browse_and_sort, width=25, height=2)
sort_button.pack()

root.mainloop()