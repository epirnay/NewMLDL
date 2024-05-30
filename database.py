import psycopg2 

# Veritabanına bağlanmak için bir fonksiyon tanımlayalım.
def connect_to_db():
    conn = psycopg2.connect(database="postgres", user="postgres", host="localhost", password="123456")
    return conn


def createtable(sql):

    conn = psycopg2.connect(database="postgres", user="postgres", host="localhost", password="123456") #connect to database

    cur = conn.cursor()

    cur.execute(sql)

    conn.commit()

    cur.close()
    conn.close()
