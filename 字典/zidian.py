#!/usr/bin/env python3
data = {'kushal':'Fedora','kart_':'Debian','Jace':'Mac'}
print(data)
print(data['kushal'])
data['parthan'] = 'Ubuntu'
print(data)
del data['kushal']
print(data)
print('shiyanlou' in data)
b = dict((('Indian','Delhi'),('Bangladesh','Dhaka')))
print(b)
for x,y in b.items():
	print("{} users {}".format(x,y))
