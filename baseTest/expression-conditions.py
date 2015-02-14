#encoding:utf-8
#python中的比较运算符基本和java一样，多出来的有：
#in、not in、is、not is
#但是python中最特殊的是比较运算符是可以连接的比如
x = int(input("please input a number:"))
print("bool(10<x<99),x is "+str(x)+", "+str(bool(10<x<99)))

#is 和 == 类似，但是比==的检查性更强，类似于java中equals与==之间的区别
x = y = [1,2,3]
z = [1,2,3]
print("x==y : "+str(x==y))
print("x==z : "+str(x==z))
print("x is y : "+str(x is y))
print("x is z : "+str(x is z))

x = [1,2,3]
y = [2,4]
print("x is "+str(x))
print("y is "+str(y))
print("x is not y :"+str(x is not y))
del x[2]
print("x is "+str(x))
y[1] = 1
print("y is "+str(y))
y.reverse()
print("y is "+str(y))
print("x==y : "+str(x==y))
print("x is y : "+str(x is y))

#in 就是成员资格运算，类似于java中的contains
name = input("What is your name ?")
if 's' in name :
	print("Your name contains the letter 's'")
else :
	print("Your name does not contains the letter 's'")

#字符串和序列的比较
print("alpha < beta :" +str('alpha' < 'beta'))
print("李杰 < 刘晓洋 :" + str('李杰' < '刘晓洋'))

#python中的布尔关联关系有and、or、not类似于java中的&&、||、！
#python中的布尔运算符和java中一样，都是有短路的