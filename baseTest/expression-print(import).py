#encoding:utf-8
#print可以接受多个参数来输出,每个参数之间使用空格隔开
print(1,2,3)
print('Hello,','World')
print('Hello,',end="")
print('Lijie')

#python3 同行输出：
for x in range(4):
	print(x,end=",")

#import和java里的import相似，但是有其他的用法例如：
#import 模块名
#from 模块名 import 函数名
#也可以给模块或者函数使用as起别名
#import 模块名 as aaa
#from 模块名 import 函数名 bbb