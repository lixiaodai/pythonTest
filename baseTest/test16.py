#encoding:utf-8
#this test is used for lower/replace/split/strip methods
#lower is like lower in java
str='LiJie'
arr = ['gumby','smith','jones']
print(str.lower())
if ('Gumby' in arr):print('Found it!')
else:print("Can't found!")
if('Gumby'.lower() in arr):
	print('Found it!')
else:
	print("Can't found it!")
	
#replace like replace in java
str = 'This is a test'
print(str.replace('is','aa'))

#split like split in java
str = 'a+2+c+3+f'
print(str.split('+'))
print(list(str))

#strip is an important method ,it's not only trim whitespace two sides of the string ,but also can trim special letter both sides of the string
str = '              internal whitespace is                 kept          '
print(str)
print(str.strip())            
str = input('please input your name:')
if(str.strip().lower() in arr):
	print('Found it!')
else:
	print("Can't found it!")

print('****    SPAM * for * everyone !!!! aaaa !!!!!      *****')
print('****    SPAM * for * everyone !!!! aaaa !!!!!      *****'.strip(' *!'))