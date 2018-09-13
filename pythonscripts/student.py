#!/bin/python3


myfileObj = open("studentrecord.txt", "r") # r, w , a 
mylocFile = open("location.txt", "w")
content = myfileObj.readlines()
for i in content:
	#print(i)
	record = i.split(",")
	mylocFile.write(record[2] + "\n")
	print(record[2])
mylocFile.close()
myfileObj.close()
