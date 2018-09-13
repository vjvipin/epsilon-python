#!/bin/python3

#a = "4th Training in "
#
#for i in a.lower():
#	if i in "aeiou":
#		print(i, "is a vowel")
#	elif i.isalpha():
#		print(i, "is a consonant")
#	elif i.isdigit():
#		print(i, "is a digit")
##	else:
##		print(i, "seems to be a special charecter or white space")
#print("end of for loop")

#a = "4th Training in "
#index = 0
##for i in a.lower():
#while index < len(a):
#	i = a[index]
#	
#	if i in "aeiou":
#		print(i, "is a vowel")
#	elif i.isalpha():
#		print(i, "is a consonant")
#	elif i.isdigit():
#		print(i, "is a digit")
##	else:
##		print(i, "seems to be a special charecter or white space")
#	index +=1
#print("end of while loop")

a = "4th Training"
index = 0
#for i in a.lower():
while index < len(a):
	i = a[index]
	if i in "aeiou":
		print(i, "is a vowel so continue with the next iteration")
		index +=1
		continue;
	elif i.isalpha():
		print(i, "is a consonant")
	elif i.isdigit():
		print(i, "is a digit")
	else:
		pass
#		print(i, "seems to be a special charecter or white space")
	index +=1
	print("loop number ", index )
print("end of while loop")

