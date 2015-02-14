#encoding:utf-8
#test for simple format string
format = "Hello,%s.%s enough for ya?"
values = tuple("li")
print (format)
print (format % values)
#test for format number
format = "format pi %.9f"
from math import pi
print (format % pi)