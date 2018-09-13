#!/usr/bin/python

import MySQLdb
import csv
# Open database connection
db = MySQLdb.connect("zekeserver.ctxzguosahx8.ap-south-1.rds.amazonaws.com","user","zeketraining","zekedb" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

sql = "SELECT * FROM EMPLOYEE"

try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   writer = csv.writer(open("outfile.csv", 'w'))
   for row in results:
      fname = row[0]
      lname = row[1]
      age = row[2]
      sex = row[3]
      income = row[4]
      writer.writerow(row)       
except:
   print "Error: unable to fecth data"

db.close()

