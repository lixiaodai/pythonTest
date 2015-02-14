
#这个例子用来实现列表的基本操作：给元素赋值、删除元素以及分片替换
#从lijie这个字符串转化为liuxiaoyang这个字符串
src="lijie"
print (src)
#list(字符串)，函数是将字符串转化为列表
dest=list(src)
print (dest)
#将输入转化为要替换的字符串的索引
resetIndex = int(input("Please input index that which you want to rest: "))-1
#将输入作为要换成的字符
resetValue = input("Please input what you want to reset: ")
dest[resetIndex]=resetValue
print (dest)
#分片赋值第一种方式：替换目标分片中的值，可以将不等量替换，当然也可以等量替换，即多个替换一个.注意：分片使用的是:而不是,
srcIndex = int(input("Please input srcIndex that which you want to rest: "))-1
destIndex = int(input("Please input destIndex that which you want to rest: "))-1
resetValue = list(input("Please input what you want to reset: "))
dest[srcIndex:destIndex]=resetValue
print (dest)
#分片赋值第二种方式：利用分片进行列表的插入，即分片的开始索引与结束索引相同.注意：分片使用的是:而不是,
insertIndex = int(input("Please input insertIndex that which you want to rest: "))-1
insertValue = list(input("Please input what you want to insert: "))
dest[insertIndex:insertIndex]=insertValue
print (dest)
#同时分片都可以使用步长，这里使用了默认的1
#分片中的删除，使用del 列表[index]
deleteIndex = int(input("Please input delIndex that which is you want to delete: "))-1
del dest[deleteIndex]
print (dest)
#使用join函数，将列表转化为字符串
print (''.join(dest))