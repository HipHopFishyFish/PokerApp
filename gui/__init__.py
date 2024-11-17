"""is this working"""

import tkinter as tk
import carddealer as cd
import tkinter as tk
import time
from PIL import Image, ImageTk

class PokerTable:
    def __init__(self):
        self.master = tk.Tk()
        self.setup()

    def setup(self):
        self.master.title("PokerApp")
        self.master.geometry("700x700")
        self.master.resizable(False, False)
        self.canvas = tk.Canvas(self.master, bg="green", width=700, height=700)
        self.canvas.pack()
    def mainloop(self):
        self.master.mainloop()

    def round(self, cards, players):
        global photo, photo2, photo3, photo4, photo5
        playercards = cd.dealPlayers(cards, players)
        image = Image.open(f"gui/cards/{playercards[0][0].number}{playercards[0][0].suit}.png")
        resizeimage = image.resize((80, 120))
        image = resizeimage
        photo = ImageTk.PhotoImage(image)
        self.canvas.create_image(300, 600, anchor=tk.CENTER, image=photo)

        image = Image.open(f"gui/cards/{playercards[0][1].number}{playercards[0][1].suit}.png")
        resizeimage = image.resize((80, 120))
        image = resizeimage
        photo2 = ImageTk.PhotoImage(image)
        self.canvas.create_image(400, 600, anchor=tk.CENTER, image=photo2)

        # bid chips here

        time.sleep(3)

        flopcards = cd.flop(cards)
        image = Image.open(f"gui/cards/{flopcards[0].number}{flopcards[0].suit}.png")
        resizeimage = image.resize((80, 120))
        image = resizeimage
        photo3 = ImageTk.PhotoImage(image)
        self.canvas.create_image(200, 250, anchor=tk.CENTER, image=photo3)  

        image = Image.open(f"gui/cards/{flopcards[1].number}{flopcards[1].suit}.png")
        resizeimage = image.resize((80, 120))
        image = resizeimage
        photo4 = ImageTk.PhotoImage(image)
        self.canvas.create_image(250, 250, anchor=tk.CENTER, image=photo4)   

        image = Image.open(f"gui/cards/{flopcards[2].number}{flopcards[2].suit}.png")
        resizeimage = image.resize((80, 120))
        image = resizeimage
        photo5 = ImageTk.PhotoImage(image)
        self.canvas.create_image(300, 250, anchor=tk.CENTER, image=photo5)   

        