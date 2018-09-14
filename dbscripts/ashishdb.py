#!/usr/bin/python
import MySQLdb

# Open database connection
db = MySQLdb.connect("zekeserver.ctxzguosahx8.ap-south-1.rds.amazonaws.com","user","zeketraining","ashishdb")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Create table as per requirement
#sql = """CREATE TABLE EMPLOYEE1 (
#         FIRST_NAME  CHAR(20) NOT NULL,
#         LAST_NAME  CHAR(20),
#         AGE INT,  
#         SEX CHAR(1),
#         INCOME FLOAT )"""
#cursor.execute(sql)
#
# execute SQL query using execute() method.
#sql = """INSERT INTO EMPLOYEE1(FIRST_NAME,
#         LAST_NAME, AGE, SEX, INCOME)
#         VALUES ('Prithvi', 'M', 25, 'M', 6000)"""

#sql = """ DELETE FROM EMPLOYEE1 WHERE FIRST_NAME = "Prithvi" """
#cursor.execute(sql)
#db.commit()

sql = "SELECT * FROM EMPLOYEE \
       WHERE INCOME > '%d'" % (1000)
#sql = getquery()

try:
	cursor.execute(sql)
	results = cursor.fetchall()
#	print(results)	
	outputfile = open("outfile.txt",'a')
	for i in results:
#		print (i)
		print("firstname = ", i[0], "lastname = ", i[1])
		outputfile.write(str(i)+"\n") 
	outputfile.close()
#	db.commit()
except:
	db.rollback()
	print "Error: unable to fecth data"

db.close()
#sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
#         LAST_NAME, AGE, SEX, INCOME)
#         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
# Fetch a single row using fetchone() method.
#data = cursor.fetchone()
#data = cursor.()
#print "Database version : %s " % data

# disconnect from server
#db.close()
