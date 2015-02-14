#encoding:utf-8
#this is a dictionary demo
#simple create dictionary
phonebook = {'Alice':'2341','Beth':'9102','Cecil':'3258'}
print(phonebook['Alice'])
#other way to create dictionary
items = [('name','Gumby'),('age',42)]
d = dict(items)
print(d)
d = dict(name='Gumby',age=42)
print(d)
#字典的嵌套示例
#简单的数据库
#使用人名作为key
people = {
	'Alice':{
		'phone':'2341',
		'addr':'Foo drive 23'
	},
	'Beth':{
		'phone':'9102',
		'addr':'Bar street 42'
	},
	'Cecil':{
		'phone':'3158',
		'addr':'Baz avenue 90'
	}
}
#针对电话号码和地址使用的标签，在打印输出的时候使用
labels = {
	'phone':'phone number',
	'addr':'address'
}
name = input('Name: ')
request = input('Phone number(p) or address (a)? ')
if request == 'p' : key = 'phone'
if request == 'a' : key = 'addr'

if name in people : print("%s's %s is %s." % (name,labels[key],people[name][key]))