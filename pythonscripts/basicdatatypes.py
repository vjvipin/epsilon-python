#!/bin/python3
import math 
#from math import *

var = 1 #int
var = "string" #str 
#print(dir("zekeLabs"))
#print(help("zekeLabs".startswith))

# string class

var1 = "zekeLabs"
#print(var)
var2 = 'zeke"Labs'
#var3 = '''zeke
#Labs'''
#print(var1,"\t",var2,var3)

# Operator
# +   Concatenation
# * 
#print (var1+" "+var2)
#print (2*var2)

# len
#print (len(var1))
# string methods 
#print(dir(var1))
#print(var1.isupper())
#print(var1.upper())
#var1 = var1.upper()
#print(dir(var1))
#islower()
#print( dir(math))
#print(math.pi)
#num = 100
#pi = 2
#print(math.sin (math.pi/2))
##print(math.log10(num))
##print(math.factorial(10))

var1 = "zekeLabs1"
#indexing
print(var1[-4])
#slicing
# stringname[startindex:stopindex+1:step]

print(len(var1))
print(var1[2:6:2])
var2 = var1[0:4]
mystring = "I come from zekeLabs"
# index 
i = mystring.index("zeke")
print(mystring[i:])
filepath = "D://Desktop/os/unix/python/files/python/scripts"
print(len(filepath))
#i = filepath.index("python", 25)
i = filepath.count("python")
i = filepath.find("python")
#print(filepath.find("python", filepath.find("python")+1))
#print(i)
#print(help(filepath.count))
print (filepath.replace("python","Jython"))

print(mystring.split())
mydirs = filepath.split("/")
print(mydirs)
print("/".join(mydirs))

#print(help(str.partition))

print(filepath.partition("unix"))

