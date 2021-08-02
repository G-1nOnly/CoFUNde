a=int(input())
for x in range(1,a):
    print('{} {} {}'.format(x,x*x,x*x*x))

b=input()
print('你刚刚输入的是：{}'.format(b))

c=input()
d=input()
print('{1}:{0}'.format(c,d))

print('{0:0.1f}'.format(1.12)) # :表示作用域 0.1f 一位浮点

e = "%x,%d" % (10, 100.12) #与c语言类似 % 用于分隔 (,)用元组表示
print(e)