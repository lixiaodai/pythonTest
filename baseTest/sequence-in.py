#encoding:utf-8
#检查用户名和PIN码
database = [['albert','1234'],['dilbert','4242'],['smith','7524'],['jones','9843']]
names = ['a','b','c']
username = input('Username : ')
pin = input('PIN code: ')
if [username,pin] in database:print ('Access granted')
#常见使用的嵌套
print (input('your name : ') in names)