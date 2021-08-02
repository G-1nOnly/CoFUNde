class test:
    def __init__(self,size = 10):
        self.size = size

    def getsize(self):
        return self.size

    def setsize(self,size):
        self.size = size

    def delsize(self):
        del self.size

    x = property(getsize,setsize,delsize)  #property其实就是收录了上面三个函数

t1 = test(100)
print(t1.x)
