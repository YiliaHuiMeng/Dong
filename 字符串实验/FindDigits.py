#!/usr/bin/env python3
file = open('/home/shiyanlou/Code/String.txt')
for i in file:
	if(i.isdigit()):
		print(i)
	else:
		continue
