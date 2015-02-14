#encoding:utf-8
#python中的循环
#1，while循环
x = 1
while x<=100:
	print(x)
	x+=1

#name = ''
#while True:
#	name = input("Please input your name: ")
#	print('Hello,%s' % name)

#2,for循环,JS中也有这个形式的循环in，
#但是现在一般使用JQuery提供的$.each(数组,function(index,value))
words = 'this is an ex parrot'.split(' ')
for word in words:
	print(word)

numbers = [0,1,2,3,4,5,6,7,8]
for x in numbers:
	print(x)

for x in range(10):
	print(x)

#3,遍历/迭代字典
d = {'x':1,'y':2,'z':3}
#这里的in d 和in d.keys()的效果一样
for key in d:
	print("key is "+key+",and corresponds to "+str(d[key]))
#可以使用序列解包
for key,value in d.items():
	print("key is "+key+",and corresponds to "+str(value))
