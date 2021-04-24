import psycopg2

con = psycopg2.connect(
                host = "localhost",
                database = "dbernar",
                user = "postgres",
                password = "KBTUstudent03")

print("DB CONNECTED!")


curs = con.cursor()
curs.execute("""

SELECT * FROM Employee
ORDER BY ID ASC

""")

rows = curs.fetchall()

for data in rows:
    print("ID: " + str(data[0]))
    print("NAME: " + str(data[1]))
    print("SALARY: " + str(data[2]))

con.commit()
print("DATA SELECTED!")
con.close()
