"""UNUSED"""

import tkinter as tk
from PIL import Image, ImageTk

# NOT USED
def display_card(table, card, x, y, sizex, sizey):
    image = Image.open(f"gui/cards/{card.number}{card.suit}.png")
    resizeimage = image.resize((sizex, sizey))
    image = resizeimage
    photo = ImageTk.PhotoImage(image)
    table.canvas.create_image(x, y, anchor=tk.CENTER, image=photo)