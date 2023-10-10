import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image

# Create a Tkinter window
root = tk.Tk()


# Create a function to open the file dialog box and display the selected image
def open_file_dialog():
    # Use the filedialog module to open the file dialog box
    file_path = filedialog.askopenfilename(filetypes=[("JPEG Files", "*.jpg"), ("PNG Files", "*.png")])

    # Open the selected image using the Pillow library
    image = Image.open(file_path)

    # Create an ImageTk object to display the image in the Tkinter window
    image_tk = ImageTk.PhotoImage(image)

    # Create a Tkinter label to display the image
    image_label = tk.Label(root, image=image_tk)
    image_label.pack()

    # Start the Tkinter main loop
    root.mainloop()

open_file_dialog()
