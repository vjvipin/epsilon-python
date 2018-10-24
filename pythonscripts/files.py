#!/bin/python3

myfileObj = open("myfile.txt", "w+") # r, w , a 
#l = [1,2,3,4]
#myfileObj.write("Hi This is the content in my file.\n")
#myfileObj.write("Adding some more things in file \n")

for i in range(5):
	myfileObj.write(" My line number is " + str(myfileObj.tell()) + "\n")

myfileObj.close()

#myfileObj = open("myfile.txt", "r") # r, w , a 
myfileObj = open("myfile.txt", "r") # r, w , a 

myfileObj.seek(5)
line1 = myfileObj.read(100)

print(line1)
#print(line1, str(myfileObj.tell()))
myfileObj.close()

#myfileObj.tell()
#print(help(myfileObj.read))
#content = myfileObj.readlines(70)
#for i in content:
#	print(i)

#print( myfileObj.tell())
#
#line2 = myfileObj.readline()
#print(line2)
#print( myfileObj.tell())
#
#line3 = myfileObj.readline()
#print(line3)
#print( myfileObj.tell())
#myfileObj.close()
