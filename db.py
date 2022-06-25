import mysql.connector
#creating database
mydb = mysql.connector.connect(host="localhost",user="root",passwd="1234")
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABSE STUDENT")
#CREATING TABLE - we have to pass databasename name
import mysql.connector
.............................#creating database
import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",passwd="1234",database="student")
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE studentdetails(ROLLNO INT PRIMARY KEY,NAME VARCHAR(20) NOT NULL,CLASS VARCHAR(20) NOT NULL,AGE INT)")

..............................creating menu
