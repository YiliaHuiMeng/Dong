#!/usr/bin/env python3
def palindrome(s):
	return s == s[::-1]
if __name__ == '__main__':
	s = input("enter a String:")
	if palindrome(s):
		print("Yay a palindrome")
	else:
		print("oh no,not a palindrome")
