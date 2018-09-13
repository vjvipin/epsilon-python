address = "Epsilon Hub 2 replicator 2 Karle. .town Center 560012, 8840796501"
##print (address)
#words = address.split()
##print (words)
#
#for word in words:
#	word = word.strip(",./t ")
#	#print(word, len(word))
#	if word.isnumeric():
#		if(len(word) == 6):
#			pincode = word
#	#else:
#	#	print(word)
#
#print("found pincode: ", pincode)
#
#def printaddress(myaddress):
#	a = 5 +2 
#	print ("This is my address")
#	print (myaddress)
#
def getpincode (myaddress):
	words = myaddress.split()
	for word in words:
		word = word.strip(",./t ")
		if word.isnumeric():
			if(len(word) == 6):
				pincode = word
	return pincode

#printaddress(address)
#mypincode = getpincode(address)
#print(mypincode)	

zekeaddress = "zekeLabs AECS layout near McD 560037 8095465880 Bangalore"
#zekepincode = getpincode(zekeaddress)
#print(zekepincode)	
