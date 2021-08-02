from tkinter import *


def check(value):
    return value.isdigit()


root = Tk()
root.title("My Calculator")

v1 = StringVar()
v2 = StringVar()
v3 = StringVar()
v4 = StringVar()


def calc():
    if v2.get() == '+':
        result = int(v1.get()) + int(v3.get())
    elif v2.get() == '-':
        result = int(v1.get()) - int(v3.get())
    elif v2.get() == '*':
        result = int(v1.get()) * int(v3.get())
    else:
        result = int(v1.get()) / int(v3.get())

    v4.set(result)


def leave():
    print("Exit!")
    root.quit()


testCMD = root.register(check)

e1 = Entry(root, textvariable=v1, validate='key', validatecommand=(testCMD, '%P'))
# %P表示 当输入框的值允许改变，该值有效。该值为当前文本框内容
e2 = Entry(root, textvariable=v2, width=2)
e3 = Entry(root, textvariable=v3, validate='key', validatecommand=(testCMD, '%P'))
e4 = Entry(root, textvariable=v4, state='readonly')  # readonly 不可更改但可复制

e1.grid(row=0, column=0)
e2.grid(row=0, column=1)
e3.grid(row=0, column=2)
e4.grid(row=0, column=3)

Button(root, text="Calculate", width=10, command=calc).grid(row=1, columnspan=2)
Button(root, text="Exit", width=10, command=leave).grid(row=1, columnspan=4)

mainloop()
