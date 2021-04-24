import psycopg2

con = psycopg2.connect(
                host = "localhost",
                database = "dbernar",
                user = "postgres",
                password = "KBTUstudent03")

print("DB CONNECTED!")


curs = con.cursor()
curs.execute("""

UPDATE Employee set SALARY = '30000'
WHERE ID = '1'  

""")

con.commit()
print("DATA UPDATED!")
print("TOTAL ROW AFFECTED:" + str(curs.rowcount))
con.close()
