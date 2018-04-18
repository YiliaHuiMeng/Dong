#!/usr/bin/env python3
import sys
def Hours():
	minute = int(input("enter the number of minute: "))
	try:
		minute = int(input("enter the number of minute: "))
		hour = int(minute / 60)
		minutes = minute % 60
		print("{} H,{} M".format(hour,minutes))		
	except ValueError:
		raise ValueError("Input number cannot be negative.")
		print("ValueError:",ValueError)

if __name__ == "__main__":
	Hours()
