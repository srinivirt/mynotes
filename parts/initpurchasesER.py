#!/usr/bin/env python3
#
# This is used to initialize the "purchases" Entity-Relationship table
# between users and parts table (name_id => user_id Foreign Key
# part_id => part_id Foreign Key)
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
tbl_name = "purchases"
# Table for parts description, with part_id as PRIMARY KEY AUTO INCREMENT
sqlCmdER = ("CREATE TABLE purchases ("
    " name_id INT, FOREIGN KEY (name_id) REFERENCES users(user_id) ON UPDATE CASCADE, "
    " part_id INT, FOREIGN KEY (part_id) REFERENCES parts(part_id) ON UPDATE CASCADE "
    " )");
#print(sqlCmdER)
try:
    my_cursor.execute(sqlCmdER)
except:
    print("Ignore " + tbl_name + " table creation error == already exists")
    pass

# Show tables
my_cursor.execute("SHOW TABLES")
for tbl in my_cursor:
    print(tbl[0].decode("utf-8"))  # decode bytearray as utf-8 string


# Insert a record in users table
sqlInsertCmd = "INSERT INTO " + tbl_name + " (name_id, part_id) VALUES (%s, %s)"
#ts_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
row1Values = (1,1)  # INTEGER values not in quotes

# Insert row into table, then commit changes using mydb
my_cursor.execute(sqlInsertCmd, row1Values) # inserts into table
mydb.commit()  # commit table changes

my_cursor.execute("SELECT * FROM " + tbl_name)
for prt in my_cursor:
    print(prt)

multipleRows = [
        (2,2), # Need comma in end for single value tuple
        (22,3), # Need comma in end for single value tuple
        (23,4), # Need comma in end for single value tuple
        (24,1), # Need comma in end for single value tuple
        ]
my_cursor.executemany(sqlInsertCmd, multipleRows)
mydb.commit() # COMMIT!!
my_cursor.execute("SELECT * FROM " + tbl_name)
resultSet = my_cursor.fetchall()
for row in resultSet:
    print(row)

