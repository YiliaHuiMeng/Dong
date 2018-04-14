#!/usr/bin/env python3
num = int(input("enter the value of num:"))
print("enter values of the Matrix A")
a = []
for i in range(num):
	a.append([int(x) for x in input().split()])
print("enter values of the Matrix B")
b=[]
for i in range(num):
	b.append([int(x) for x in input().split()])
c = []
for i in range(num):
	c.append([a[i][j] * b[i][j] for j in range(num)])
print("after matrix multiplication")
print("-" * 7 * num)
for x in c:
	for y in x:
		print(str(y).rjust(5),end=' ')
	print()
print("-" * 7 * num)
