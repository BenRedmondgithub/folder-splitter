# Import necessary modules
import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
import threading
import time

# Define file extensions for RAW and JPEG image files
RAW_EXTENSIONS = [".cr2", ".nef", ".arw", ".dng", ".rw2", ".orf", ".sr2"]
JPEG_EXTENSIONS = [".jpg", ".jpeg"]
VIDEO_EXTENSIONS = [".mp4", ".mov", ".avi", ".mkv"]

class RetroLoader:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Processing...")
        self.window.geometry("400x200")
        self.window.resizable(False, False)
        self.window.transient(parent)
        self.window.grab_set()
        
        # Center the window
        self.window.update_idletasks()
        x = (self.window.winfo_screenwidth() // 2) - (400 // 2)
        y = (self.window.winfo_screenheight() // 2) - (200 // 2)
        self.window.geometry(f"400x200+{x}+{y}")
        
        # Retro styling
        self.window.configure(bg='#000000')
        
        # Title label
        title_label = tk.Label(self.window, text="RETRO PROCESSOR", 
                              bg='#000000', fg='#00ff00', 
                              font=('Courier', 16, 'bold'))
        title_label.pack(pady=20)
        
        # Loading text
        self.loading_label = tk.Label(self.window, text="SORTING FILES", 
                                     bg='#000000', fg='#00ff00', 
                                     font=('Courier', 12))
        self.loading_label.pack(pady=10)
        
        # Retro progress bar frame
        self.progress_frame = tk.Frame(self.window, bg='#000000')
        self.progress_frame.pack(pady=10)
        
        # Create retro progress bar using characters
        self.progress_chars = []
        for i in range(20):
            char_label = tk.Label(self.progress_frame, text="□", 
                                 bg='#000000', fg='#00ff00', 
                                 font=('Courier', 12))
            char_label.grid(row=0, column=i, padx=1)
            self.progress_chars.append(char_label)
        
        # Status label
        self.status_label = tk.Label(self.window, text="INITIALIZING...", 
                                    bg='#000000', fg='#00ff00', 
                                    font=('Courier', 10))
        self.status_label.pack(pady=10)
        
        self.animation_running = True
        self.current_progress = 0
        
        # Start animation
        self.animate()
    
    def animate(self):
        if self.animation_running:
            # Rotate through progress bar
            for i, char_label in enumerate(self.progress_chars):
                if i == self.current_progress:
                    char_label.config(text="■")
                else:
                    char_label.config(text="□")
            
            self.current_progress = (self.current_progress + 1) % len(self.progress_chars)
            self.window.after(150, self.animate)
    
    def update_status(self, text):
        self.status_label.config(text=text)
    
    def close(self):
        self.animation_running = False
        self.window.destroy()


def safe_move(src, dst_folder):
    """
    Move a file to the destination folder, renaming if a file with the same name exists.
    Prevents overwriting by appending a counter to the filename if needed.
    """
    base, ext = os.path.splitext(os.path.basename(src))
    dst_path = os.path.join(dst_folder, base + ext)
    counter = 1
    while os.path.exists(dst_path):
        dst_path = os.path.join(dst_folder, f"{base}_{counter}{ext}")
        counter += 1
    shutil.move(src, dst_path)


def sort_photos(folder, loader=None):
    """
    Sort files in the selected folder into 'RAW', 'JPEG', and 'VIDEO' subfolders based on their extensions.
    Shows a retro loader while processing and a message box when sorting is complete.
    """
    if loader:
        loader.update_status("SCANNING FILES...")
    
    raw_folder = os.path.join(folder, "RAW")
    jpeg_folder = os.path.join(folder, "JPEG")
    video_folder = os.path.join(folder, "VIDEO")

    # Create subfolders if they don't exist
    os.makedirs(raw_folder, exist_ok=True)
    os.makedirs(jpeg_folder, exist_ok=True)
    os.makedirs(video_folder, exist_ok=True)

    # Get all files first for progress tracking
    all_files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
    total_files = len(all_files)
    
    if loader:
        loader.update_status(f"FOUND {total_files} FILES")
        time.sleep(0.5)

    moved = 0
    for i, filename in enumerate(all_files):
        file_path = os.path.join(folder, filename)
        
        # Update status periodically
        if loader and i % 5 == 0:
            loader.update_status(f"PROCESSING {i+1}/{total_files}...")
        
        # Check file extension and move accordingly
        _, ext = os.path.splitext(filename.lower())
        if ext in RAW_EXTENSIONS:
            safe_move(file_path, raw_folder)
            moved += 1
        elif ext in JPEG_EXTENSIONS:
            safe_move(file_path, jpeg_folder)
            moved += 1
        elif ext in VIDEO_EXTENSIONS:
            safe_move(file_path, video_folder)
            moved += 1

    if loader:
        loader.update_status("FINALIZING...")
        time.sleep(0.5)

    # Notify user when done
    messagebox.showinfo("Done", f"Sorting complete.\nFiles moved: {moved}")


def browse_and_sort():
    """
    Open a dialog for the user to select a folder, then sort the photos in that folder.
    """
    folder_selected = filedialog.askdirectory(title="Select Folder to Sort")
    if folder_selected:
        # Show retro loader
        loader = RetroLoader(root)
        
        # Run sorting in a separate thread to keep UI responsive
        def sort_thread():
            try:
                sort_photos(folder_selected, loader)
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")
            finally:
                loader.close()
        
        thread = threading.Thread(target=sort_thread)
        thread.daemon = True
        thread.start()


# GUI setup
root = tk.Tk()
root.title("Photo Sorter")
root.geometry("300x150")
root.resizable(False, False)

# Add a label to the window
label = tk.Label(root, text="Sort RAW, JPEG, and VIDEO files", pady=20)
label.pack()

# Add a button to start the sorting process
sort_button = tk.Button(root, text="Select Folder and Sort", command=browse_and_sort, width=25, height=2)
sort_button.pack()

# Start the Tkinter event loop
root.mainloop()