import sqlite3

connect=sqlite3.connect("employee.db")
print("Connected")
connect.execute("INSERT INTO Staff2(ID ,FIRSTNAME,LASTNAME,AGE,SALARY,TASK)\
               VALUES(1,'Jack','Harrison',21,99999.00, 'Employer')")
connect.execute("INSERT INTO Staff2(ID ,FIRSTNAME,LASTNAME,AGE,SALARY,TASK)\
              VALUES(2,'Helen','Wambui',24,696969.00, 'Secretary')")
connect.execute("INSERT INTO Staff2(ID ,FIRSTNAME,LASTNAME,AGE,SALARY,TASK)\
                VALUES(3,'Drew','Armstrong',42,12000.00, 'Plumber')")
connect.execute("INSERT INTO Staff2(ID ,FIRSTNAME,LASTNAME,AGE,SALARY,TASK)\
                VALUES(4,'Oliver','Queen',30,3000000.00, 'Vigilante')")

connect.commit()
print("Inserted successfully into Staff Table")
connect.close()