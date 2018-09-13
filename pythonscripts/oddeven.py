#!/bin/python3

numlist = [3,2,5,45,67,78]

def oddeven(numlist):
	oddlist = []
	evenlist = []
	for i in numlist:
		if(i%2 == 0):
			print(i, "is even")
			evenlist.append(i)
		else:
			print(i, "is odd")
			oddlist.append(i)
	print(evenlist)
	print(oddlist)
	return oddlist,evenlist

odd,even = oddeven(numlist)		
