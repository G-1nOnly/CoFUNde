from tkinter import *
import hashlib

root = Tk()
root.title("Text")

text = Text(root, width=30, height=10, undo=True)
text.pack()

text.insert(INSERT, "Checking")
contents = text.get("1.0", END)


def getcontent(content):
    m = hashlib.md5(content.encode()) # 匹配是否有内容
    return m.digest()


sig = getcontent(contents)


def check():
    content = text.get("1.0", END)
    if sig != getcontent(content):
        print("Warning!")
    else:
        print("Working")


def delete():
    text.delete("1.0", END)


def undo():
    text.edit_undo()  # 撤销


Button(root, text="Check", command=check).pack()
Button(root, text="Delete", command=delete).pack()
Button(root, text="Undp", command=undp).pack()
Button(root, text="Exit", command=root.quit).pack()
mainloop()
