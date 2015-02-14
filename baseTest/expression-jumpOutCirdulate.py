#encoding:utf-8
#1,break 和java中的break一样,java中的break可以有label，跳出label指示的循环
from math import sqrt
for n in range(99,0,-1):
	root = sqrt(n)
	if root == int(root):
		print(n)
		break;

#2,continue和java中continue一样
for n in range(1,10):
	print('number is '+str(n))
	if n == 5:
		continue;
	print('end is '+str(n))

#3,While True/break 使用方式,通常While True/break 一起使用：
while True:
	name = input('Please input your name: ')
	if not name:
		break
	print('Your name is '+str(name))
