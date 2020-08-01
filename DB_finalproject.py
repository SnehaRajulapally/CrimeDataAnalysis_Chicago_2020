#Name: Sneha Rajulapally
#CWID: A20457266
#Date: 07/27/2020
#Filename :DB_finalproject.py
#Description: Python file which has the functions for login credentials(SQLite3 DB)

#importing statements
import sqlite3
import csv
import hashlib

#Method to create DB table which consists of username and login details
def createTabledb():
    try:
        conn = sqlite3.connect("finalproject.db")   #create a connection to SQLite db
        cursor = conn.cursor()
        print("Connection to database successful!")
    except:                 #throw an error message of connection fails
        print("Error:Connection to database unsuccessful!")
    try:
        cursor.execute('DROP TABLE IF EXISTS USERSDATA')
        #creating table name sneha with below columns
        query = '''CREATE TABLE IF NOT EXISTS USERSDATA
         (ID INTEGER PRIMARY KEY AUTOINCREMENT,
         USERNAME TEXT NOT NULL,
         PASSWRD CHAR(64) NOT NULL )''' #creating table name sneha if it doesn't exists
        cursor.execute(query)
        conn.commit() #commiting the changes to db
        print("Table sneha created successfully!")
    except:
        print("Error: Table creation unsuccessful!")
        conn.rollback() #roll back changes if there are errors
    conn.close()  #closing connection after changes   

#method to insert initial login details to DB from CSV file
def inserttodb():
    try:
        conn = sqlite3.connect("finalproject.db")   #create a connection to SQLite db
        cursor = conn.cursor()
    except:                 #throw an error message of connection fails
        print("Error:Connection to database unsuccessful!")
    try:   
        # read recs from users.csv file
        filename = "usersdata.csv" # csv file name
        # initializing the titles and rows list
        row = []
        # reading csv file
        with open(filename, 'r') as csvfile:
        # creating a csv reader object
            csvreader = csv.reader(csvfile)
        # extracting each data row one by one
            for data in csvreader:
                row.append(data)
        # leaving indent closes out block, thus file
        # extracting each column by row one by one
        for col in row[:]:
        # retrieve hashed password
            hashed_password = hashlib.sha256(col[1].encode('utf-8')).hexdigest()
            cursor.execute("INSERT INTO USERSDATA (USERNAME,PASSWRD) VALUES (?, ?)" , (col[0],hashed_password));
        conn.commit()
        print ("Records inserted successfully from CSV file to DB!")
    except:
        print("Error: Inserting records from CSV file to DB unsuccessful!")
    conn.close()

#method to insert new signed up login credentials to database
def newuserdb(newuser,newpswrd):
    try:
        conn = sqlite3.connect("finalproject.db")   #create a connection to SQLite db
        cursor = conn.cursor()
    except:                 #throw an error message of connection fails
        print("Error:Connection to database unsuccessful!")
    try:
        # retrieve hashed password
        hashed_password = hashlib.sha256(newpswrd.encode('utf-8')).hexdigest()
        cursor.execute("INSERT INTO USERSDATA (USERNAME,PASSWRD) VALUES (?, ?)" , (newuser,hashed_password));
        conn.commit()
        print ("Inserted new record successfully to DB!")
    except:
        print("Error: Inserting new record to DB unsuccessful!")
    conn.close()