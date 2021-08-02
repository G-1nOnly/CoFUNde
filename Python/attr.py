class test:
    def __init__(self):
        self.x = "Testing"

t = test()

print(hasattr(t,"x")) #hasattr 判断有没有 注意双引号
print(getattr(t,"x","Not included")) #getattr判断类中是否有" "中的属性，若无则return default

setattr(t,"x","testing again")  #setattr 若存在则修改 若不存在则创建后赋值
print(getattr(t,"x"))
print(getattr(t,"y","Not included"))
setattr(t,"y","created")
print(getattr(t,"y","Not included"))

print(getattr(t,"z",setattr(t,"z","Done"))) #综合使用


class C:
    def __getattribute__(self, item):
        print("getattribute") #定义当该类属性被访问时的行为
        return super().__getattribute__(item)

    def __getattr__(self, item):
        print("getattr")  #调用不存在的属性时出现

    def __setattr__(self, key, value):
        print("setattr")
        return super().__setattr__(key,value)

    def __delattr__(self, item):
        print("delattr")
        return super().__delattr__(item)

#调用顺序如下
c = C()
c.x
c.x = 1
del c.x

