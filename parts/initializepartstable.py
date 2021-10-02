#!/usr/bin/env python3
#
# This is used to initialize the "parts" table (part_id is PRIMARY KEY)
#
import mysql.connector
import datetime

mydb = mysql.connector.connect(
        host = "localhost",
        user = "testapp1",
        passwd = "Pwd4Testapp1!",
        database = "testapp1",  # already exists/created
        )

my_cursor = mydb.cursor()

# Create a database: testapp1 (if it does not exist)
try:
    my_cursor.execute("CREATE DATABASE testapp1")
except mysql.connector.errors.DatabaseError:  # just for example
    print("Ignore exception == testapp1 database exists")
    pass

# Show database
my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
#    print(db[0]) # prints as bytearray
    print(db[0].decode("utf-8"))

# Create parts table
tbl_name = "parts"
# Table for parts description, with part_id as PRIMARY KEY AUTO INCREMENT
sqlCmd = "CREATE TABLE " + tbl_name + \
    (" (part_id INTEGER AUTO_INCREMENT PRIMARY KEY,"
     " description VARCHAR(255), "
     " datecreated TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")
#print(sqlCmd)
try:
    my_cursor.execute(sqlCmd)
except:
    print("Ignore " + tbl_name + " table creation error == already exists")
    pass

# Show tables
my_cursor.execute("SHOW TABLES")
for tbl in my_cursor:
    print(tbl[0].decode("utf-8"))  # decode bytearray as utf-8 string


# Insert a record in users table
sqlInsertCmd = "INSERT INTO " + tbl_name + " (description) VALUES (%s)"
#ts_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
row1Values = ("Part1 electronics",)  # INTEGER values not in quotes

# Insert row into table, then commit changes using mydb
my_cursor.execute(sqlInsertCmd, row1Values) # inserts into table
mydb.commit()  # commit table changes

my_cursor.execute("SELECT * FROM " + tbl_name)
for prt in my_cursor:
    print(prt)

multipleRows = [
        ("Foo part",), # Need comma in end for single value tuple
        ("Bar part",), # Need comma in end for single value tuple
        ("FooBar part",), # Need comma in end for single value tuple
        ("Fooz part",), # Need comma in end for single value tuple
        ]
my_cursor.executemany(sqlInsertCmd, multipleRows)
mydb.commit() # COMMIT!!
my_cursor.execute("SELECT * FROM " + tbl_name)
resultSet = my_cursor.fetchall()
for row in resultSet:
    print(row)

