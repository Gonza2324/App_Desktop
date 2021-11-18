"cSpell:disable"
from tkinter import *
from tkinter import font, messagebox
from PIL import Image, ImageTk
from sympy import diff, Symbol

x = Symbol("x")
y = Symbol("y")

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

        self.funcion_input = StringVar()
        self.funcion = Entry(self.root, width=28)
        self.funcion.config(
            font = ("Arial", 20),
           justify=CENTER,
            bg="#DBDBDB",
            bd = 0
        )
        self.funcion.focus()
        self.funcion.place(x = 460, y = 245)

        self.img_textbox0 = Image.open('img_textBox0.png')
        self.python_img0 = ImageTk.PhotoImage(self.img_textbox0)
        self.canvas.create_image(680, 265, image = self.python_img0)

        self.img_answer = Image.open('img_textBox1.png')
        self.python_img1 = ImageTk.PhotoImage(self.img_answer)
        self.canvas.create_image(680, 400, image = self.python_img1)

        def calculo_one_variable_f():
            try:
                f = self.funcion.get()
                calcular = diff(f, x)
                self.derivate.set(calcular)
            except:
                messagebox.showerror("Error", "¡Introduce la funcion correctamente!")

        def calculo_two_variables_f():
            try:
                f = self.funcion.get()
                calcular_x = diff(f, x)
                calcular_y = diff(f, y)
            except:
                messagebox.showerror("Error", "¡Introduce la funcion correctamente!")

        self.derivate = StringVar()
        self.answer = Label(self.root, textvariable=self.derivate)
        self.answer.config(
            font=("Arial", 20),
            bg="#DBDBDB",
            justify=CENTER
        )
        self.answer.place(x = 460, y = 380)

        self.btn_calculo = Button(self.root, text = "1 variable", command=calculo_one_variable_f)
        self.btn_calculo.config(
            font = ("Arial", 27),
            activebackground="#FF8E15",
            background= "#FF8E15",
            relief="groove"
        )
        self.btn_calculo.place(x = 480, y = 500)

        self.btn_calculo_two_variables = Button(self.root, text = "2 variables", command=calculo_two_variables_f)
        self.btn_calculo_two_variables.config(
            font = ("Arial", 27),
            activebackground="#FF8E15",
            background= "#FF8E15",
            relief="groove"
        )
        self.btn_calculo_two_variables.place(x = 680, y = 500)

        self.root.resizable(False, False)
        self.root.mainloop()

#TODO: temporal, solo para poder trabajar en este archivo sin recurrir al de window
if __name__ == '__main__':
    root = Tk()
    app = Aplicacion(root)