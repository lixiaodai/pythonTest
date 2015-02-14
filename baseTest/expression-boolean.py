#encoding:utf-8
#python中对boolean类型的处理和JS很相似，以下类型python都会解析为False
#False None 0 "" () [] {}
print('True: '+str(True))
print('False: '+str(False))
print('True==1: '+str(True == 1))
print('Flase==0: '+str(False == 0))
print('True+False+42: '+str(True + False +42))

#method bool(value) 可以将value值转化为boolean类型的值
print("bool('I think, therefore I am'): "+ str(bool('I think, therefore I am')))
print("bool(42): "+str(bool(42)))
print("bool(''): "+str(bool('')))
print("bool(0): "+str(bool(0)))
#要注意的是，都是控制的值不相等
print("bool([])==bool(''): "+str(bool([])==bool('')))
print("bool([]==''): "+str(bool([]=='')))