#encoding:utf-8
#easy test for format 
print ('Price of eggs: $%d' % 42)
print ('Hexadecimal price of eggs: %x' % 42)
from math import pi
print ('Pi: %f...' %pi)
print ('Very inexact estimate of pi: %i' % pi)
print ('Using str: %s' % 42)
print ('Using repr %r' % 42)
#the width(宽度) and the accuracy(精度) config for the format
print ('%10f' % pi)
print ('%10.2f' % pi)
print ('%.2f' %pi)
print ('%.5s' % 'Guido van Rossum')