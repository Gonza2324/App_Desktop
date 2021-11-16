from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

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

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    470, 380,
    image=background_img)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    820, 265,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry0.place(
    x = 610, y = 232,
    width = 418.0,
    height = 67)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    820, 380,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry1.place(
    x = 610, y = 348,
    width = 418.0,
    height = 67)

#TODO:*Entry 3
entry2_img = PhotoImage(file = f"img_textBox2.png")
entry2_bg = canvas.create_image(
    820, 500,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#C4C4C4",
    highlightthickness = 0)

entry2.place(
    x = 610, y = 467,
    width = 418.0,
    height = 67)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    cursor = "hand2",
    relief = "flat"
    )

b0.place(
    x = 671, y = 590,
    width = 294,
    height = 92)

window.resizable(False, False)
window.mainloop()