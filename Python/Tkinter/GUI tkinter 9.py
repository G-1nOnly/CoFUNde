from tkinter import *

root = Tk()
c = Canvas(root, width=800, height=400)
# 单位为像素
c.pack()


def paint(event):
    x1, y1 = (event.x - 1), (event.y - 1)  # event为鼠标当前选定点
    x2, y2 = (event.x + 1), (event.y + 1)
    c.create_oval(x1, y1, x2, y2, fill="red")


c.bind("<B1-Motion>", paint)  # 与鼠标左键绑定

Button(root, text="Exit", command=root.quit).pack()
Label(root, text="Move your mouse to paint")

mainloop()
