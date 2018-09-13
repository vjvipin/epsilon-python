#/bin/python3

#web_server_dict = {}   #empty dictionary
web_server_dict = {"servername":"Ep-Web-01", "memory":8, "cpu":5.4}
db_server_dict = {"servername":"Ep-DB-01", "memory":4, "cpu":2.7}

serverlist = [web_server_dict, db_server_dict]
print(serverlist)

print(web_server_dict["memory"])
print(len(web_server_dict))

print(web_server_dict.keys())
print(web_server_dict.items())

for i in web_server_dict.values():
	print(i)

#insert
web_server_dict["ip_addr"] = "172.31.2.1"

#update 
web_server_dict["servername"] = "Ep-Web-02"
web_server_dict.clear()

#del web_server_dict
print(web_server_dict)
print(dir(web_server_dict))

#help(dict)

