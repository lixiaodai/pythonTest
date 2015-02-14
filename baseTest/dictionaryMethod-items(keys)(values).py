#encoding:utf-8
dic = {'title':'Python Web Site','url':'http://www.python.org','spam':0}
print(dic.items())
#python3 没有了iterkeys/iteritems得方法，items和iteritems一样直接返回了迭代器对象,keys方法也直接返回迭代器对象
print(dic.keys())
#python3 也没有了valueitems,只有values
print(dic.values())
