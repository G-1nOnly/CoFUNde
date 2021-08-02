def gen(n):
  for each in range(1,n):
        print("Working!",each)
        yield each

n = int(input())
g = gen(n)
while True:
    try:
        next(g) #生成器直到有next才执行

    except StopIteration:
        break

#fibonacci+generator
def fib():
    a = 0
    b = 1
    while True:
        a,b = b,a+b
        yield a   #生成器会自动生成自动停止

value = int (input())

for each in fib():
    if each < value:
        print(each)
    else:
        break

#简易生成器
e = (i for i in range(1,10))
for each in e:
    print(each)

sum = sum(value for value in range(1,100))
print(sum)
