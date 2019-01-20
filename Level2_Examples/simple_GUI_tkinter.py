from tkinter import *
import random

window = Tk()
lbl = Label(window,
            text="Random Number [1, 10]").pack()
lbl_n = Label(window, text="")
lbl_n.pack()


def clicked():
    lbl_n.configure(text=random.randint(1, 10))


btn = Button(window,
             text="Generate",
             command=clicked).pack()
window.mainloop()
