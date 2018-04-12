#!/usr/bin/env python3
amount = float(input("enter amount:"))
inrate = float(input("enter interest rate:"))

period = int(input("enter period:"))
value = 0
year = 1
while year <= period:  //当year的值小于等于period的值时，下面的语句会循环执行
	value = amount + (inrate * amount)
	print("year {} Rs.{:.2f}".format(year,value)) //字符串格式化，｛｝中的内容会被format里面的参数替换
	amount = value
	year = year + 1

