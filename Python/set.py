set=set((2,'rh',1,34,5456))
print(set)
set.add(2134)
print(set)
set.update([123,23],{9:9,10:10},(5,6,7,8))#可加入列表，元组，字典
print(set)
set.remove(2)
print(set)
set.discard(2134)
print(set)
set.pop()#随机删除
print(set)
print(len(set))
print(1 in set)
for x in set:
    print(type(x),' ')
set.clear()

a={x for x in'abdasjdjbkjs' if x not in 'bwjdbjew'}
print(a)

b={1,2,3,4,'dsfbjs'}
print(b)

seta = set('abracadabra')
setb= set('alacazam')
print(seta)                                  # a 中唯一的字母
print(seta - setb)                              # 在 a 中的字母，但不在 b 中
print(seta | setb)                              # 在 a 或 b 中的字母
print(seta & setb)                              # 在 a 和 b 中都有的字母
print(seta ^ setb)                              # 在 a 或 b 中的字母，但不同时在 a 和 b 中
