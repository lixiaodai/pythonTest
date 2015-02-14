#encoding:utf-8
#join method is an important method,it's reverse split
#join方法的意思是，将当前字符串添加到目标字符串或列表的各个字符之间
#如果目标是列表,那么列表中的各个元素必须是字符
#例如'aaaa'.join('ccccccb')的输出为caaacaaacaaacaaacaaacaaab
print('aaaa'.join('ccccccb'))
sep = '+'
seq = ['11','22','33','44','55']
print(sep.join(seq))
dirs = '','usr','bin','env'
print('/'.join(dirs))
print('C:'+'\\'.join(dirs))