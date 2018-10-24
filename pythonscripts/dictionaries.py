# key value pairs
# ordered
# fast access 

address = {"fname":"ashish", "lname":"Pandey", "fname":"Awi"}
#address2 = {"name": { "fname":"ashish", "lname":"Pandey"}}

'''
print(address2["name"])
'''
address["pincode"] = "227807"
print(address)
if "fname" not in address.keys():
	address["fname"] = "Ashish"
print(list(address.keys()))
print(list(address.values()))
print(list(address.items()))
for k,v in address.items():
	print(k + v)
i = address.pop("fname")
v = address["fname"]
#print(help(address.pop))
print(i)
print(address)
#print(dir(address))


