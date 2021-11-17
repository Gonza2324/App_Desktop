"cSpell:disable"
from tkinter import *
import root as rt
import database as db

def Insert():
    db.conectar_basededatos()
    
    entry0 = text_entry0.get()
    entry1 = text_entry1.get()
    entry2 = text_entry2.get()

    db.Insert(entry0, entry1, entry2)
    window.destroy()

def btn_clicked():
    Insert()
    top = Tk()
    rt.Aplicacion(top)
    Insert()
#Sign Up
window = Tk()

window.title("Derivative--Sign Up")
window.geometry("1152x700")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 700,
    width = 1152,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = "background.png")
background = canvas.create_image(
    470, 380,
    image=background_img)

entry0_img = PhotoImage(file = "img_textBox0.png")
entry0_bg = canvas.create_image(
    820, 265,
    image = entry0_img)

text_entry0 = StringVar()
entry0 = Entry(
    window,
    textvariable=text_entry0,
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0,
    font = ("Arial", 24)
)

entry0.focus()

entry0.place(
    x = 610, y = 232,
    width = 418.0,
    height = 67)

entry1_img = PhotoImage(file = "img_textBox1.png")
entry1_bg = canvas.create_image(
    820, 380,
    image = entry1_img)

text_entry1 = StringVar()
entry1 = Entry(
    window,
    textvariable=text_entry1,
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0,
    font = ("Arial", 24)
)

entry1.place(
    x = 610, y = 348,
    width = 418.0,
    height = 67)

entry2_img = PhotoImage(file = "img_textBox2.png")
entry2_bg = canvas.create_image(
    820, 500,
    image = entry2_img)

text_entry2 = StringVar()
entry2 = Entry(
    window,
    textvariable= text_entry2,
    bd = 0,
    bg = "#C4C4C4",
    highlightthickness = 0,
    font = ("Arial", 24)
)

entry2.place(
    x = 610, y = 467,
    width = 418.0,
    height = 67)

img_btn = PhotoImage(file = "img0.png")
btn_Registrar = Button(
    image = img_btn,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    cursor = "hand2",
    relief = "flat"
    )

btn_Registrar.place(
    x = 671, y = 590,
    width = 294,
    height = 92)

window.bind("<Return>", lambda x: btn_clicked())
window.resizable(False, False)
window.mainloop()