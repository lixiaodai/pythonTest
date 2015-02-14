# -*- coding: utf-8 -*-
#根据给定的年月日以数字形式打印出日期
months = ['January','February','March','April','May','June','July','August','Semptember','October','November','December']
#以1-31的数字作为结尾的列表,这里是最简单的将每个月的31天的显示方式存储起来
endings = ['st','nd','rd']+17*['th']+['st','nd','rd']+7*['th']+['st']
year = input('Year:')
month = input('Month(1-12):')
day = input('Day(1-31):')

month_number = int(month);
day_number = int(day)

#由于所有的序列(列表和元组)的索引都是从0开始的，所以需要将用户输入的值-1
month_name = months[month_number-1]
ordinal = day + endings[day_number-1]

print (month_name+' '+ordinal+','+year)