#encoding:utf-8
#this test is used to test append/count/extend/index/insert/pop/remove/reverse method for sequece
src=list('lijie')
print (src)
#the append
app = input('please input which word you want to append to src : ')
src.append(app);
print (src)
#the count
find = input('please input which word you want to count it`s number in src : ')
print (src.count(find))
#extend
ext = input('please input what word you want to extend to src : ')
src.extend(list(ext)) 
print (src)
#index 
ind = input('please input which word you want to know the index of it : ')
print (src.index(ind))
#insert
#这里的insert的第一个参数是要将数字插入到哪个索引，然后如果索引大于长度，那么就插入到索引=索引-长度的位置
ins = list(input('please input which word you want to insert and where (e.g a,3): '))
src.insert(int(ins[2])-1,ins[0])
print (src)
#pop,this method can return which is poped
ins = input('please input where word you want to pop and : ')
src.pop(int(ins)-1)
print (src)
#remove
rem = input('please input which word you want to remove from src: ')
src.remove(rem);
print (src)
#reverse
input('the src will reverse now!')
src.reverse()
print (src)