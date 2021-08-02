from tkinter import *

root = Tk()
root.title("TEST")

sb = Scrollbar(root)
sb.pack(side=RIGHT, fill=Y)

LB = Listbox(root, yscrollcommand=sb.set)  # yscrollcommand 可拉动
LB.pack(side=LEFT, fill=BOTH)

s1 = Scale(root, from_=0, to=10, tickinterval=5)
s1.pack()
s2 = Scale(root, from_=0, to=200, tickinterval=50, orient=HORIZONTAL, length=200)
s2.pack()

for item in range(0, 51):
    LB.insert(END, item)  # 在末尾添加元素

sb.config(command=LB.yview)
button = Button(root, text='Delete', command=lambda x=LB: x.delete(ACTIVE))
# ACTIVE即当前选中项
button.pack(fill=X)

button2 = Button(root, text='Exit', command=root.quit)
button2.pack(fill=X)

mainloop()
