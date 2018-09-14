
import xmltodict
def getloglevel():
	with open ("server.xml", 'r') as fileobj:
		a=xmltodict.parse(fileobj.read())
		print (a['server']['log']['log-file'])
		print(a['server']['log']['log-level'])
		return a['server']['log']['log-level']

