import sqlite3
connect = sqlite3.connect('employee.db')
print("Successfully connected to database")

connect.execute("UPDATE Staff2 set SALARY=50000 where ID=1")
connect.commit()

data = connect.execute("SELECT * FROM Staff2")
for rows in data:
    print("ID :", rows[0])
    print("FIRSTNAME:", rows[1])
    print("LASTNAME:", rows[2])
    print("AGE:", rows[3])
    print("SALARY", rows[4])
    print("TASK", rows[5])

print("Successfully updated")
connect.close()

