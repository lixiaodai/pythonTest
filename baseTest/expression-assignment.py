#encoding:utf-8
#序列解包，就是将多个值得序列解开，然后放到变量的序列中
x,y,z = 1,2,3
print(x,y,z)
x,y = y,x
print(x,y,z)
#就像是将多个变量自动的组成一列序列，然后在序列中赋值，如下：
values = (1,2,3)
print(values)
x,y,z = values
print(x,y,z)
#当某些调用的返回值是一个序列时，我们可以同时将返回值赋值给其他，就像是ORM一样
scoundrel = {'name':'Robin','girlfrend':'Marion'}
key,value = scoundrel.popitem()
print('key is '+key)
print('value is '+value)


#链式赋值
print()
print('链式赋值开始')
x=y='c'
print('x is '+x)
print('y is '+y)
print()
print('增量赋值开始')
#增量赋值
x = 2
print(x)
x += 1
print(x)
x *=2
print(x)

fnord = 'foo'
print(fnord)
fnord +='bar'
print(fnord)
fnord *= 2
print(fnord)

