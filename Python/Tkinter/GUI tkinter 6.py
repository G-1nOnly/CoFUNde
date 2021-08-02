from tkinter import *

root = Tk()
root.title("TEXT")
text = Text(root, widt=30, height=10)
text.pack()

text.insert(INSERT, "abcd\n")  # INSERT对于插入光标位置
text.insert(END, "ABCD\n")
text.mark_set("here", "2.0")  # mark位置
text.insert("here", "CAPITAL:")
text.tag_add("tag1", "1.0", "1.2", "1.3")  # 开始，结束，单独
text.tag_configure("tag1", background="yellow", foreground="red",
                   underline=True)

button = Button(text, text="Exit", command=root.quit)
text.window_create(INSERT, window=button)  # 也可插入图片 image=<文件名>
print(text.get("1.0", 2.0))
# "开始"，结束  x.y x为行数(从1开始) y为列数(从0开始) 可用.end指代该行最后一个字符

mainloop()
