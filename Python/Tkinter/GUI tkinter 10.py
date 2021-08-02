from tkinter import *


def myprint():
    print("Pressed!")


root = Tk()
root.title("MENU")

Options = ["One", "Two", "Three"]
variable = StringVar()
variable.set(Options[0])

menu0 = Menu(root)
menu = Menu(menu0, tearoff=False)  # tearoff 把虚线去除
menu.add_command(label="Press", command=myprint)
menu.add_separator()
menu.add_command(label="Exit", command=root.quit)
menu0.add_cascade(label="Menu", menu=menu)
w = OptionMenu(root, variable, *Options)  # *可将其解开
w.pack()

root.config(menu=menu0)

mainloop()
