#encoding:utf-8
#斐波那契数列
arr = [0,1]
for i in range(10):
	arr.append(arr[-2]+arr[-1])
print(arr)

arr = [0,1]
num = input("How many Fibonacci numbers to want ? ")
for i in range(int(num)):
	arr.append(arr[-2]+arr[-1])
print(arr)