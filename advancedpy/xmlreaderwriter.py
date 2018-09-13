
import xmltodict
import dicttoxml

import json

print(dir(dicttoxml))
with open ("server.xml", 'r') as var:
	a=xmltodict.parse(var.read())
	print (a['server'])

	with open ("outxmlfileforserver.json", 'w') as jsonfile:
        	json.dump(a,jsonfile,indent=4)
	jsonfile.close()
var.close()

import urllib
import dicttoxml
page = urllib.urlopen('http://quandyfactory.com/api/example')
content = page.read()
obj = json.loads(content)
print(obj)
{u'mylist': [u'foo', u'bar', u'baz'], u'mydict': {u'foo': u'bar', u'baz': 1}, u'ok': True}
xml = dicttoxml.dicttoxml(obj)
with open ("outxmlfile.xml", 'w') as xmlout:
	xmlout.write(xml)
xmlout.close()

import xml.etree.cElementTree as ET 
#
root= ET.Element("myelement")
sub1=ET.SubElement(root, "sub1")
sub2=ET.SubElement(root, "sub2")
ET.SubElement(sub1, "sub-sub1", attr="some value").text="some text"
a= ET.ElementTree(root)
a.write("test.xml")

