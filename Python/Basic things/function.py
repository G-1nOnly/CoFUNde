def func(a, *b):
    print(a)
    print(b)


func(2, 3, 4, 5, 6)  # *tuple导入


def state(a, *b):
    print(a)
    for x in b:
        print(x,' ',end='')


state(2, 2, 3, 4, 5, 6)
print('\n')


def func(a, **b):
    print(a)
    print(b)


func(2, x=3, y=4)  # ** dictionary导入


def times2(a):
    return a * 2


print(times2(3))  # 不可变对象


def changelist(list1):
    del list1[0]  # list、dictionary 可变对象


list1 = [1, 2, 3, 4]
print(list1)
changelist(list1)
print(list1)

# 匿名函数 lambda
x = lambda x, y: x * y
print(x(1, 2))
y = lambda x: 2 * x
print(y(2))


def printme(name, age=0):
    print(name)
    print(age)

printme(name='xxx') #默认参数 不输入自动输出
printme(age=18, name='gjn')  # 关键字参数 调用时可以不按顺序

def func(x): #闭包+嵌套
    def func2(y):
      return x*y
    return func2

print(func(2)(5))

def func3(x):
    def func4(y):
      return x*y
    return func4

func3()

l = list(filter(lambda: x > 0,[-1,-2,-3,0,1,2,3])) #filter类似于sort
print(l)
