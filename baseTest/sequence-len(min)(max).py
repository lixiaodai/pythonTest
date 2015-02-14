#encoding:utf-8
charValues = ['a','b','A','Z']
numberValues = [1,43,54,77,23,123]
#两点：
#第一点：python中数字不能像java中一样和字符串利用+直接连接为一个新的字符串，只能通过str()内建函数转化后相连
#第二点：python内的默认排序与java一样都是自然排序法，即unicode编码的大小
print ('charValues max : '+str(max(charValues)) +',charValues min: '+str(min(charValues)) + ',charValues len: '+str(len(charValues)))
print ('numberValues max : '+str(max(numberValues)) +',numberValues min: '+str(min(numberValues)) + ',numberValues len: '+str(len(numberValues)))
