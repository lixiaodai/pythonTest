#encoding:utf-8
#Python中，函数的注释和Java不同，Java中是写在方法前面的/**/，同时可以使用javadoc命令生成java文档
#而Python的函数注释在函数体内部，函数第一行的string字符串就是该函数说明,使用：函数名.__doc__方式输出

import math
x = 1
y = math.sqrt
print("callable(1): "+str(callable(x)))
print("callable(sqrt): "+str(callable(y)))

def hello(name):
	'This function is used to print Hello xxxx'
	return 'Hello, ' + name + "!"
print(hello.__doc__)
print(hello('lijie'))

def createFibonacci(num):
	'This function is used to formular Fibonacci numbers'
	arr = [0,1]
	for i in range(num):
		arr.append(arr[-2]+arr[-1])
	return arr
print(createFibonacci.__doc__)
print(createFibonacci(23))

#help函数可以得到函数的注释也就是说明，第一行的字符串，以及类似于Java中的函数签名
print(help(hello))

#当函数没有返回值，也就是return后边没有返回值或者说没有return语句，
#那么在Python中，函数返回的是None。类似于java中的void声明