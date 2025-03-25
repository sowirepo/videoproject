import time
import os
import tkinter as tk
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from parse_manim_script import parse_manim

filename = 'compexp'

img_path = f'/home/chris/manim/videoproject/media/images/parsed_{filename}/Test_ManimCE_v0.19.0.png'
file_to_check = f'/home/chris/manim/videoproject/{filename}.py'
parsed_file_to_check = f'/home/chris/manim/videoproject/parsed_scripts/parsed_{filename}.py'

assert os.path.exists(file_to_check)

try:
    assert os.path.exists(parsed_file_to_check)
except AssertionError:
    parse_manim(f'{filename}.py')
    assert os.path.exists(parsed_file_to_check)

try:
    assert os.path.exists(img_path)
except AssertionError:
    print('Image file does not exist. Rendering image...')
    cmd = f"python3 -m manim -sql parsed_scripts/parsed_{filename}.py Test"
    os.system(cmd)
    time.sleep(0.2)

class FileChangeHandler(FileSystemEventHandler):
    """Handler to handle changes in files."""
    def __init__(self, label, img_path, file_to_check):
        super().__init__()
        self.label = label
        self.img_path = img_path
        self.file_to_check = file_to_check

    def on_modified(self, event):
        parse_manim(f'{filename}.py')
        # Reload image if image file is modified
        if event.src_path == self.img_path:
            self.reload_image()
        
        # check if code file is modified
        if event.src_path == self.file_to_check:
            self.render_image()

    def reload_image(self):
        # Small delay to ensure file writing is complete
        time.sleep(0.2)
        img = tk.PhotoImage(file=self.img_path)
        self.label.config(image=img)
        self.label.image = img  # Keep a reference to avoid garbage collection

    def render_image(self):
        cmd = f"python3 -m manim -sql parsed_scripts/parsed_{filename}.py Test"
        os.system(cmd)
        time.sleep(0.2)
        self.reload_image()

root = tk.Tk()
root.title('Live Preview')
img = tk.PhotoImage(file=img_path)
label = tk.Label(root, image=img)
label.pack()

# Setup watchdog observer
event_handler = FileChangeHandler(label, img_path, file_to_check)
observer = Observer()
# Observe the directory containing both files
observer.schedule(event_handler, os.path.dirname(img_path), recursive=False)
observer.schedule(event_handler, os.path.dirname(file_to_check), recursive=False)
# Also observe the directory containing the file_to_check if it's different
observer.start()

try:
    root.mainloop()
finally:
    observer.stop()
    observer.join()