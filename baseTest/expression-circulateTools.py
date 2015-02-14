#encoding:utf-8
#python提供了很多的迭代工具：
#1,并行迭代
names = ['anne','beth','george','damon']
ages = [12,45,32,102]
for i in range(len(ages)):
	print(names[i]+' is '+str(ages[i])+' years old')

#python中提供了zip函数来进行并行迭代，将多个*序列压缩在一起，相同索引的元素压缩为一个元组，

#zip返回一个元组列表
print(zip(names,ages))
for name,age in zip(names,ages):
	print(name + ' is ' + str(age) + ' years old')
#zip函数最重要的是可以有无限多个参数，同时各个参数的内部对象不一定等长，zip只取最短长度
for val1,val2 in zip(range(5),range(10000)):
	print('val1 is '+str(val1)+', val2 is '+str(val2))

#2,编号迭代
#python中并没有像java一样有for(int i;i<xxx;i++)的迭代形式，所以对于某些在迭代的时候需要当前
#元素的索引的情况下有些无力，最简单的实现方式:
index = 0
strings = ['a','b','c','d','e']
print(strings)
for string in strings:
	if('a' in string):
		strings[index] = 'z'
	index+=1
print(strings)
#上边这种方法比较笨拙，所以python提供了enumerate:类似于JQuery中的each
#enumerate方法的参数是序列，返回值是索引，值得序列解包
strings = ['a','b','c','d','e']
for index,value in enumerate(strings):
	if 'a' in value:
		strings[index] = 'z'
print(strings)