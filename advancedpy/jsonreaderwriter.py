import json

# var=open("file.json", 'r')
a = None
with open ("books.json", 'r') as var:
	a= json.loads(var.read())
# print (a['glossary']['title'])
var.close()
# m={'key':'value'}
with open ("output.json", 'w') as var:
 	json.dump(a,var, indent=4)
	print(help(json.dump))
var.close()
