import psycopg2


try:
    con = psycopg2.connect(
                host = "localhost",
                database = "dbernar",
                user = "postgres",
                password = "KBTUstudent03")
    print("DB connected")
except:
    print("ERROR!")
