#encoding:utf-8
#translate method is like replace,but only use for one letter.it's quickly than replace method
a = 'Hello!World!'
t = str.maketrans('l','a')
a.translate(t)
print(a)
print(a.translate(t))