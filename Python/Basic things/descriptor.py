class Descriptor(object):

    def __init__(self):
        self._name = ''

    def __getattribute__(self, item):
        print("getattribute")
        return super().__getattribute__(item) #判断优先级

    def __get__(self, instance, owner):  #instance 即为实例 #owner即为拥有对象
        print("__get__",instance,owner)
        return self._name

    def __set__(self, instance, value):
        print("__set__")
        self._name = value

    def __delete__(self, instance):
        print("__delete__")
        del self._name


class Person(object):
    name = Descriptor()


p = Person()
p.name
p.name = 'jacob'
print(p.name)
del p.name
