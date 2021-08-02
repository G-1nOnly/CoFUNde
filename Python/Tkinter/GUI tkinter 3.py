from tkinter import *


def show():
    print("Name: %s" % e1.get())
    print("Password: %s" % e2.get())


def func1():
    if e1.get() == 'gjn519021910417':
        print('Entering...')
        return True
    else:
        print('Wrong Person')
        e1.delete(0, END)
        return False


def func2():
    print('Try again!')
    return False


root = Tk()
Label(root, text="Name:").grid(row=0, column=0)
Label(root, text="Password:").grid(row=1, column=0)

v1 = StringVar()
v2 = StringVar()

e1 = Entry(root, textvariable=v1, validate='focusout', validatecommand=func1,
           invalidcommand=func2)
# focus获得或消失焦点 focusin获得 focusout消失
e2 = Entry(root, textvariable=v2, show="*",)

e1.grid(row=0, column=1, padx=10, pady=5)
e2.grid(row=1, column=1, padx=10, pady=5)

Button(root, text="Get Info", width=10, command=show) \
    .grid(row=3, column=0, sticky=W, padx=10, pady=5)
Button(root, text="Exit", width=10, command=root.quit) \
    .grid(row=3, column=1, sticky=E, padx=10, pady=5)

mainloop()
