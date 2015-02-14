#encoding:utf-8
#使用了if语句,注意python中使用":"代表语句块的开始
print()
print("if start:")
name = input("What's is your name?")
if name.endswith('Jie'):
	print('Hello,Mr '+name)
print()
print("if else start:")
name = input("What's is your name?")
if name.endswith('Jie'):
	print('Hello,Mr ' + name)
else:
	print('Hello,stranger')
print()
print("if elif start")
num = int(input('Enter a number: '))
if num>0:
	print('The number is positive!')
elif num<0:
	print('The number is negative!')
else:
	print('The number is zero!')

print()
print("nest if start")
name = input("What is your name?")
if name.endswith("Jie"):
	if name.startswith("Li"):
		print("Hello,LiJie")
	elif name.startswith("Liu"):
	    print("Hello,LiuJie")
	else:
		print("Hello,"+name)
else:
	print("Hello,stranger!")