#encoding:utf-8
#get method is like ['key'],but it not return exception if key is not exist return None
dic = {'name':'lijie','age':23}
print(dic)
print(dic.get('sex'))
#print(dic['sex'])
#get方法还可以定义如果未找到的输出，是get方法的第二个参数
print(dic.get('sex','there no sex define'))

#demo
#使用get()方法的简单数据库
#创建简单的数据库(字典)
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
labels = {
	'phone':'phone number',
	'addr':'address'
	}
name =  input('Name:')
request = input('Phone number (p) or address (a)?')
key = ''
if request == 'p' : key = 'phone'
if request == 'a' : key = 'addr'
#people是一个二维字典,当所取的人不存在的时候返回一个空字典
person = people.get(name,{})
#如果没有，那么就显示要输入的属性
label = labels.get(key,key)
#从person中取得key
result = person.get(key,'not available')
print("%s's %s is %s." % (name,label,result))