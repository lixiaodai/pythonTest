#encoding:utf-8
#else不止可以和if语句结合使用，也可以与while、for循环中的break结合使用
#只有当break没有执行的时候，else中的内容才会执行
#也就是当循环没有完整执行的情况下才执行else的内容，如果循环顺利的执行完了就不执行else
from math import sqrt
for n in range(99,80,-1):
	root = sqrt(n)
	if root == int(root):
		print(n)
		break
else:
	print("Didn't find it")