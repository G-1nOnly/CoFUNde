import tkinter as tk


class Test:
    def __init__(self, master):
        frame = tk.Frame(master)
        frame.pack(side=tk.TOP, padx=20, pady=10)

        self.b = tk.Button(frame, text='Press', fg='red', bg='yellow', command=self.press)
        self.b.pack()
        self.b2 = tk.Button(frame, text='Done', fg='red', bg='yellow', command=self.set)
        self.b2.pack()

    def press(self):
        print("Pressed!")

    def set(self):
        var.set("Tested!")


root = tk.Tk()
root.title("test")
var = tk.StringVar()  # tkinter自带
var.set("Testing!")
label = tk.Label(root, justify=tk.LEFT, textvariable=var, font=('TimesNewRoman', 20))
# 也可加入图片 pic = tk.PhotoImage(file = '文件名')
# imglabel = tk.Label(root,image=pic)
# 也可加图片背景 只需在上式中插入image='文件名'即可
label.pack()
test = Test(root)
root.mainloop()
