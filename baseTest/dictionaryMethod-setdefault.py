#encoding:utf-8
#setdefault方法类似于get,但是get方法是利用第二个参数来设定取值的时候第一个参数代表的key没有值时候的返回值
#而setdefault方法是在定义的时候就设定了当取某些key且该key不存在的时候的返回值，setdefault和[]结合起来使用起到get方法的效果
#但是，setdefault设置的值优先级比get方法设置的值优先级高，同时又setdefault和get时，返回的是setdefault设置的值

dic = {}
dic.setdefault('name','N/A')
print(dic)
print(dic['name'])
print(dic.get('name','name is not aviable'))#说明setdefault设置的值优先级比get方法设置的值优先级高
dic['name']='Lijie'
dic.setdefault('name','N/A')#setdefault的值不会覆盖实际的值
print(dic)

dic = {}
dic.setdefault('name')
print(dic)
print(dic['name'])#当setdefault没有第二个参数时，和get一样默认都是None