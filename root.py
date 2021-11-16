"cSpell:disable"
from tkinter import *
from PIL import Image, ImageTk

class Aplicacion:
    def __init__(self, root):
        self.root = root
        self.root.title("Derivative Aplication")
        self.root.geometry("1000x700")

        self.canvas = Canvas(width = 1000, height=700)
        self.canvas.pack()

        self.img = Image.open('./img_root/bg.png')
        self.python_img = ImageTk.PhotoImage(self.img)
        self.canvas.create_image(470, 360, image = self.python_img)

        self.root.mainloop()
