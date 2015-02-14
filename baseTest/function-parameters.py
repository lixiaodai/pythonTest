#encoding:utf-8
#Python中对于变量的处理类似于Java，函数/方法中不能直接改变参数，但是可以改变参数值指向的值
#类似于可以改变引用类型指向的内部实际值，而不能改变参数：
def try_to_change(val):
	'尝试改变不变参数的值'
	val = 'Mr. Gumby'
	return 

name = 'Mr. Li'
print(name)
print(try_to_change.__doc__)
try_to_change(name)
print(name)

def try_to_change_seq(val):
	'尝试改变引用类型参数内部的值'
	val[0]='Mr Li'
	return

names = ['Mr Lu','Mr Zhang']
print(names)
print(try_to_change_seq.__doc__)
try_to_change_seq(names)
print(names)