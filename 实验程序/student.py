#!/usr/bin/env python3
num = int(input("输入学生的数量："))
data = {}
Subject = ('Physics','Maths','History')
for i in range(0,num):
	name = input("输入学生的名字：{}".format(i + 1))
	marks = []
	for x in Subject:
		marks.append(int(input("enter marks of {}").format(x)))
	data[name] = marks
for x,y in data.items():
	total = sum(y)
	print("{}'s total marks {}".format(x,total))
	if total < 120:
		print(x,"failed:(")
	else:
		print(x,"passed:)")

