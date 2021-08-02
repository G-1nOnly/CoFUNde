from tkinter import *

root = Tk()
c = Canvas(root, width=200, height=100, background="white")
# 单位为像素
c.pack()

line1 = c.create_line(0, 50, 200, 50, fill="yellow")
line2 = c.create_line(100, 0, 100, 100, fill="red", dash=(4, 4))
# 前面为长度，后面为间隔
rect = c.create_rectangle(50, 25, 150, 75, fill="blue")

c.coords(line1, 0, 25, 200, 25)  # 移动位置
c.itemconfig(rect, fill="red")
c.delete(line2)
c.create_text(100, 50, text="Canvas")


button = Button(root, text="Exit", command=root.quit).pack()

mainloop()
