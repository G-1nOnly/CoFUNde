dict={'name':'dhgasjdajd','age':18}
dict1={'gender':'male',1:1}
print(dict['name'])
del dict1[1]
dict2=dict1.copy()
print(dict2)

#item-> key:value
#使用.items()遍历
for x,y in dict.items():
    print(x,y)

for x in dict.keys():
    print (x,end='\n')

for x in dict.values():
    print (x,end='\n')

dict.clear()
dict1.clear()
