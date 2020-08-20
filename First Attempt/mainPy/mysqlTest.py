#!/usr/bin/python
import mysql.connector
 
db = mysql.connector.connect(host="localhost",  # your host 
                     user="kasra",       # username
                     passwd="",     # password
                     db="pythontest_db")   # name of the database
 
# Create a Cursor object to execute queries.
cur = db.cursor()
 
# Select data from table using SQL query.
cur.execute("SELECT * FROM examples")
 
# print the first and second columns      
for row in cur.fetchall() :
    print (row[0], " ", row[1], "---->", row[2])
