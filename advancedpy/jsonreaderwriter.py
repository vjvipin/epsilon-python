import json

# var=open("file.json", 'r')
content_dict = None
with open ("books.json", 'r') as var:
	content_dict= json.loads(var.read())
	print (content_dict['book'][0])
	content_dict['book'][0]['edition']= "fourth"
	print (content_dict['book'][0])
var.close()
# m={'key':'value'}
with open ("output.json", 'w') as outputFO:
	json.dump(content_dict,outputFO)
	#print(help(json.dump))
outputFO.close()
