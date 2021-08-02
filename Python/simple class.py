import math
class point:
    x=y=0
    def __init__(self,a,b):
        self.x=a
        self.y=b

    def __add__(self,other):
        return point (self.x+other.x,self.y+other.y) #overloaded

    def show(self):
        print(self.x,self.y,end='\n')

    def getd(self,other):
        d=math.sqrt((self.x-other.x)**2+(self.y-other.y)**2)
        return d


print("Input point1's x coordinate:")
a=int(input())
print("Input point1's y coordinate:")
b=int(input())
print("Input point2's x coordinate:")
c=int(input())
print("Input point2's y coordinate:")
d=int(input())
p1=point(a,b)
p2=point(c,d)
p3=p1+p2
p1.show()
p2.show()
p3.show()
print(p1.getd(p2))