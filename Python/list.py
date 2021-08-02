l=[1,2,3,4]
l1=["hi "*4]
print(len(l))
print(l+l1)
print(3 in l)
for x in l:
    print(x,end=" ")

l2=[[1,2,3,4],[5,6,7,8]]#嵌套列表
print(l2[0])
print(l2[0][1])

list1=[1,2,3,4]
list2=[3,4,5,6]
print(list1)
list1.append(1234) #添加元素
list1.extend(list2) #添加列表
list1.insert(3,7878) #在指定位置添加元素
list1.pop(3) #括号里填代表去除某个指定元素，不填则随机去除
print(list1)
print(list1.index(2)) #给出第一个某元素序号
print(list1.count(3)) #计算某元素出现次数
list1.sort()  #排序
print(list1)
list3=list1.copy()
print(list3)
list1.reverse()  #反转
print(list1)