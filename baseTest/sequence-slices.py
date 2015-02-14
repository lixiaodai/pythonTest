#encoding:utf-8
url = input('Please enter the URL:')
#分片同样是包前不包后
domain = url[4:-4]
#输出域名
print ("Domain name : "+domain)
#输出前缀，利用分片的捷径，如果从头开始，那么使用[:终止索引]
print ("Prefix name : "+url[:3])
#输出后缀，利用分片的捷径，如果分片到末尾，那么使用[开始索引:]
print ("Last name : "+url[-3:])
#全部输出，利用捷径，如果是整个截取，那么[:]
print ("Total name : "+url[:])
