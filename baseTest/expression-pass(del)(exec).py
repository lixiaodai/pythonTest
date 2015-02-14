#encoding:utf-8
#pass 表示什么都没有执行，和break、continue 不完全相同
#因为在python中，空代码块是非法的，所以需要用到pass
name = 'aaa'
if name == 'Ralph Auldus Melish':
	print('Welcome!')
elif name == 'Enid':
	pass
elif name =='Bill Gates':
	print('Access Denied')
else:
	print('I don\'t know your name!')

#del 删除，列表中可以利用del删除元素。在其它情况下，也可以使用del删除变量，但是无法变量引用的值
#python的垃圾回收类似于Java 都是不用管理的，我们只能控制变量，但是无法控制引用的值
#可以使用del删除变量，但是内存中的值是无法控制的，python的解释器来负责CG垃圾回收
dic1 = {'age':42,'first name':'Robin','last name':'of Locksley'}
dic2 = dic1
print('dic1 is '+str(dic1))
print('dic2 is '+str(dic2))
dic1 = None
dic2 = None
print('dic1 is '+str(dic1))
print('dic2 is '+str(dic2))

#exec 用来执行动态的python语句，也就是根据用户输入拼接的字符串作为python语句执行
comm = 'print("Hello,World!")'
print(comm)
exec(comm) 
#由于很多时候exec执行的python语句是与用户交互后产生的python语句，而用户的输入是不可控的
#那么就会造成变量名重复，这点在JS当中也十分明显。JS当中我们通过创建function或者闭包来控制
#而python使用了命名空间(特殊字典)的概念：
from math import sqrt
scope = {}
exec('sqrt = 1',scope)
print('sqrt(4): '+str(sqrt(4)))
print("scope['sqrt']: " + str(scope['sqrt']))
print("len(scope): "+str(len(scope)))

#eval 用来执行动态的python语句，也就是根据用户输入拼接的字符串作为python语句执行
#但是eval与exec不同的是，eval这个函数式有返回值的也就是其执行的python语句是有结果的
#而exec只是执行python语句，没有返回值
#同时，python中的eval与JS中的eval相比，更加单一，只用来执行有返回值的python语句，
#而JS中的eval实际上包含了exec和eval的功能
print('eval(input("Enter a arithmetic expression: 2+3+4"))')
print(eval(input("Enter a arithmetic expression:")))