
#mystring = "I work at Epsilon !!!"

def getvowelsconsonants(mystring):
	vowels = "aeiou"
	myvowels = ""
	myconsonants = ""

	for i in mystring.lower():
		if(i.isalpha()):
			if(i in vowels):
				myvowels += i
			else:
				myconsonants +=i
	#print ("vowels = ", myvowels)
	#print ("consonants = ", myconsonants)
	return myvowels,myconsonants

#v,c = getvowelsconsonants(mystring)
#print(v,c)
