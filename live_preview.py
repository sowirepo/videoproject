# import time
# import os
# import tkinter as tk
# from watchdog.observers import Observer
# from watchdog.events import FileSystemEventHandler

# img_path = '/home/chris/manim/videoproject/media/images/unityroots/Test_ManimCE_v0.19.0.png'
# file_to_check = '/home/chris/manim/videoproject/unityroots.py'


# assert os.path.exists(img_path)

# class ImageReloadHandler(FileSystemEventHandler):
#     """Handler to reload the image when file changes."""
#     def __init__(self, label, img_path):
#         super().__init__()
#         self.label = label
#         self.img_path = img_path

#     def on_modified(self, event):
#         print("HELLO")
#         if event.src_path == self.img_path:
#             self.reload_image()

#     def reload_image(self):
#         time.sleep(0.2)
#         img = tk.PhotoImage(file=self.img_path)
#         self.label.config(image=img)
#         self.label.image = img  # Keep a reference to avoid garbage collection

# root = tk.Tk()
# root.title('Live Preview')
# img = tk.PhotoImage(file=img_path)
# label = tk.Label(root, image=img)
# label.pack()

# # Setup watchdog observer
# event_handler = ImageReloadHandler(label, img_path)
# observer = Observer()
# observer.schedule(event_handler, os.path.dirname(img_path), recursive=False)
# observer.start()

# try:
#     root.mainloop()
# finally:
#     observer.stop()
#     observer.join()


import time
import os
import tkinter as tk
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

img_path = '/home/chris/manim/videoproject/media/images/unityroots/Test_ManimCE_v0.19.0.png'
file_to_check = '/home/chris/manim/videoproject/unityroots.py'

assert os.path.exists(img_path)

class FileChangeHandler(FileSystemEventHandler):
    """Handler to handle changes in files."""
    def __init__(self, label, img_path, file_to_check):
        super().__init__()
        self.label = label
        self.img_path = img_path
        self.file_to_check = file_to_check

    def on_modified(self, event):
        # Reload image if image file is modified
        if event.src_path == self.img_path:
            self.reload_image()
        
        # Print "NOW" if the secondary file is modified
        if event.src_path == self.file_to_check:
            self.render_image()

    def reload_image(self):
        # Small delay to ensure file writing is complete
        time.sleep(0.2)
        img = tk.PhotoImage(file=self.img_path)
        self.label.config(image=img)
        self.label.image = img  # Keep a reference to avoid garbage collection

    def render_image(self):
        cmd = f"python3 -m manim -sql {file_to_check} Test"
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