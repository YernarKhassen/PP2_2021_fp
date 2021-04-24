import psycopg2

con = psycopg2.connect(
                host = "localhost",
                database = "dbernar",
                user = "postgres",
                password = "KBTUstudent03")

print("DB CONNECTED!")


curs = con.cursor()
curs.execute("""

CREATE TABLE Employee

(

ID INT PRIMARY KEY NOT NULL,
NAME TEXT NOT NULL,
SALARY INT NOT NULL

)


""")

con.commit()
print("TABLE CREATED!")