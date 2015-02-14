#encoding:utf-8
#pop method and popitem method is very likely
#but pop is return the value of key , that pop method must have one parameter, 
#popitem is return a entry(key and value), popitem hasn't parameter
#so popitem is quickly than pop,because popitem not need find the parameter
dic = {'name':'lijie','age':23}
print(dic.pop('name'))
print(dic)
dic = {'name':'lijie','age':23}
print(dic.popitem())
print(dic)