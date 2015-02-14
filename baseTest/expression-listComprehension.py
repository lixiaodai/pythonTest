#encoding:utf-8
#列表推导式，利用其它列表通过某种计算或限制条件创建新列表的一种方法
print('[x*x for x in range(10)]:'+str([x*x for x in range(10)]))

print('[x*x for x in range(10) if x%3 == 0]: '+str([x*x for x in range(10) if x%3 == 0]))

print('[(x,y) for x in range(3) for y in range(3)]: '+str([(x,y) for x in range(3) for y in range(3)]))

result = []
for x in range(3):
	for y in range(3):
		result.append((x,y))
print(result)

girls = ['alice','bernice','clarice']
boys = ['chirs','arnold','bob']
print(b+'+'+g for b in boys for g in girls if b[0]==g[0])