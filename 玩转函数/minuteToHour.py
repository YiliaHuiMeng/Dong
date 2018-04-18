#!/usr/bin/env python3
import sys
def Hours():
	try:
		minute = int(sys.argv[1])
		if minute < 0:
			raise ValueError
		else:
			hour = minute // 60
			minutes = minute % 60
			print("{} H,{} M".format(hour,minutes))
	except ValueError:
		print("Input number cannot be negatibe.")

Hours()
		
