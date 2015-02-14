#encoding:utf-8
#test for dictionary for string
phonebook = {'Beth':'9102','Alice':'2341','Cecil':'3258'}
print("Cecil's phone number is %(Cecil)s." % phonebook)
print("Beth's phone number is %(Beth)s." % phonebook)

template = '''<html>
<head><title>%(title)s</title></head>
<body>
<h1>%(title)s</h1>
<p>%(text)s</p>
</body>'''
data = {'title':'My Home Page','text':'Welcome to my home page!'}
print(template % data)