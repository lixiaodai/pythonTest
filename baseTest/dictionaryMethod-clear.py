#encoding:utf-8
#clear is a method had setEffect(副作用)
d = {}
d['name'] = 'Lijie'
d['age'] = 26
print(d)
returned_value = d.clear()
print(d)
print(returned_value)

# 根据以下例子，猜测python和Java一样都是传递引用的，只不过Java分堆和堆栈，不知道python分不分
#demo1
x={}
y=x
x['key'] = 'value'
x={}
print('demo1')
print(x)
print(y)
#demo2
print('demo2')
x={}
y=x
x['key']='value'
print(x)
print(y)
x.clear()
print(x)
print(y)

