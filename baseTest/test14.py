#encoding:utf-8
#the string method test
#1,find() param is which to find ,back is the first index of the find,if no find return -1
#atention, in like find ,but in is only use one letter,find is use for word
str1 = 'With a moo-moo here, and a moo-moo there'
print(str1.find('moo'))
str2 = 'Monty Python\'s Flying Circus'
print(str2.find('Monty'))
print(str2.find('Python'))
print(str2.find('Flying'))
print(str2.find('Zirquss'))
#find method can accept params,second is startIndex third is endIndex
str3 = '$$$ Get rich Now !!! $$$'
print(str3.find('$$$'))
print(str3.find('$$$',1))
print(str3.find('!!!'))
print(str3.find('!!!',0,16))
