from tkinter import *

root = Tk()
root.title("TEST")


def callback(event):
    print("Position", event.x, event.y)


def callback2(event):
    print(event.keysym)


frame = Frame(root, width=200, height=200)
frame.bind("<Button-1>", callback)
frame.bind("<Key>", callback2)
frame.focus_set()
frame.pack()
Button(root, text="Exit", command=root.quit,
       background="yellow", foreground="red").pack()

mainloop()