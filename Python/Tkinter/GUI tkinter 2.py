from tkinter import *

root = Tk()
root.title("Testing")
v = IntVar()

v = [] # 以读取状态
Dict = ['w', 'x', 'y', 'z']
for value in Dict:
    v.append(IntVar())
    c = Checkbutton(root, text=value, variable=v[-1])
    c.pack(anchor=W)  # 左对齐


Dict2 = [('One', 1), ('Two', 2), ('Three', 3)]
v2 = IntVar()
v2.set(1)
for var, num in Dict2:
    b = Radiobutton(root, text=var, variable=v2, value=num, indicatoron=False)
    # indicatoron即按钮
    b.pack(fill=X)

mainloop()
