#encoding:utf-8
#use Template object for format String
#must use $name like some shellscript language
from string import Template
s = Template('$x, glorious $x!')
re = s.substitute(x='slurm')
print (re)

#in word must use {} for mark start and end position
s = Template("It's ${x}tastic!")
re = s.substitute(x='slurm')
print (re)

#if need use $ in String can use $$ for display $
s = Template("Make $$ selling $x!")
re = s.substitute(x='slurm')
print (re)

#use dictionary to format ,dictionary in python like map in java
s = Template('A $thing must never $action')
d = {}
d['thing'] = 'gentleman'
d['action'] = 'show his socks'
re = s.substitute(d)
print (re)
