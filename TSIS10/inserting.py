import psycopg2

con = psycopg2.connect(
                host = "localhost",
                database = "dbernar",
                user = "postgres",
                password = "KBTUstudent03")

print("DB CONNECTED!")


curs = con.cursor()
curs.execute("""

INSERT INTO Employee (ID,NAME,SALARY) 
VALUES (2,'Eldar','20000')

""")

con.commit()
con.close()
print("NEW EMPLOYEE ADDED!")