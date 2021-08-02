tup1=(1,2,3)
tup2=(4,5,6,7)
#tip1[0]=0 元组元素不能修改
tup3=tup1+tup2
print(tup3)
print(tup1*2)
del tup2 #可删除元组
for x in tup1:
    print(x,'',end='')
