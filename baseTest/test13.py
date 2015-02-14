#encoding:utf-8
#使用给定的宽度打印格式化后的价格列表
#这里使用用户输入的宽度，宽度在format字符串中使用*表示，必须使用元组来格式化字符串
width=int(input('Please enter width: '))
price_width = 10
item_width = width - price_width
#使用*代表要代替的数字部分，可以从元组中取到;
#python中格式化的字符串默认是右对齐
header_format = '%-*s%*s'
format = '%-*s%*.2f'
print ('='*width)
print (header_format % (item_width,'Item',price_width,'Price'))
print ('-'*width)
#%表示要对前一个字符串进行格式化操作
print (format % (item_width,'Apples',price_width,0.4))
print (format % (item_width,'Pears',price_width,0.5))
print (format % (item_width,'Cantaloupes',price_width,1.92))
print (format % (item_width,'Dried Apricots (16 oz.)',price_width,8))
print (format % (item_width,'Prunes (4 lbs.)',price_width,12))
print (format % (item_width,'Bananas',price_width,231))
#Python中，字符串的格式化完全解析：%[-/+/ /0][宽度/*].[精度/*]转换类型
#其中%表示格式化开始，-表示左对齐，+表示带有正负号，" "正数之前保留空格，0表示当位数不够使用0填充
#宽度，当为*号时，从元组中读入宽度，精度也是。
print ('='*width)
