#encoding:utf-8
#between copy and deepcopy different is copy is shwllow copy(浅复制) deepcopy is 深复制
#copy
#列表中的copy实现是a=b[:],那么a就是b列表的复制
print('deep')
x = {'username':'admin','machines':['foo','bar','baz']}
y = x.copy()
print(x)
print(y)
y['username']='mlh'
print(x)
print(y)
y['machines'].remove('bar')
print(x)
print(y)

#deepcopy
#import copy
from copy import deepcopy
print('deepcopy')
x = {'username':'admin','machines':['foo','bar','baz']}
y = deepcopy(x)
print(x)
print(y)
y['username']='mlh'
print(x)
print(y)
y['machines'].remove('bar')
print(x)
print(y)