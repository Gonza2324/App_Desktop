"cSpell:disable"
from tkinter import *
from PIL import Image, ImageTk
from sympy import diff, Symbol, sympify

x = Symbol("x")

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

        self.funtion_label = Label(self.root, text = "Funtion to derivate")
        self.funtion_label.config(
            font = ("Arial", 20),
            border=0
        )
        self.funtion_label.place(x = 440, y = 190)

        self.img_textbox0 = Image.open('img_textBox0.png')
        self.python_img0 = ImageTk.PhotoImage(self.img_textbox0)
        self.canvas.create_image(680, 265, image = self.python_img0)

        self.img_answer = Image.open('img_textBox1.png')
        self.python_img1 = ImageTk.PhotoImage(self.img_answer)
        self.canvas.create_image(680, 400, image = self.python_img1)

        self.derivate = StringVar()
        self.answer = Label(self.root, textvariable=self.derivate)
        self.answer.config(
            font=("Arial", 20),
            bg="#DBDBDB"
        )
        self.answer.place(x = 460, y = 380)

        self.root.resizable(False, False)
        self.root.mainloop()

#TODO: temporal, solo para poder trabajar en este archivo sin recurrir al de window
if __name__ == '__main__':
    root = Tk()
    Aplicacion(root)
