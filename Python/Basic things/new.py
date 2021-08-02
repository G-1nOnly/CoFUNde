#new方法主要是当你继承一些不可变的class时(比如int, str, tuple) 提供给你一个自定义这些类的实例化过程的途径
class Capstr(str): #继承不可改变的对象字符串
    def __new__(cls,string): #利用new替换
        string = string.upper()
        return str.__new__(cls,string) #返回父类new出来的实例 然后用该实例init

A = Capstr("I love u")
print(A)
