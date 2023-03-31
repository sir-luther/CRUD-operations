import sqlite3

connect = sqlite3.connect("employee.db")
print("Connected successfully")
connect.execute("""CREATE TABLE Staff2(
ID INT PRIMARY KEY NOT NULL,
FIRSTNAME TEXT NOT NULL,
LASTNAME TEXT OT NULL,
AGE INT ,
SALARY REAL,
TASK TEXT CHAR(65))""")

print("Successfully created Staff Table")
connect.close()