#encoding:utf-8
#update方法可以利用一个dictionary来更新另一个dictionary
#就是求两个dictionary的并集

dic1 = {
	'title':'Python Web Site',
	'url':'http://www.python.org',
	'changed':'Mar 14 22:09:15 MET 2008'
	}
dic2 = {
	'title':'Lijie Web Site',
	'url':'http://www.lijie.org'
	}
dic1.update(dic2)
print(dic1)
print(dic2)
