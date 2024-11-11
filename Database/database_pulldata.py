import cx_Oracle

dsn = cx_Oracle.makedsn('oracleacademy.ouhk.edu.hk', 8998, sid='db1011')
connection = cx_Oracle.connect(user='s1305732', password='13057320', dsn=dsn)

print("Successfully connected to Oracle database!")

cursor = connection.cursor()

query = "SELECT * FROM table_name"  #change table_name

cursor.execute(query)

rows = cursor.fetchall()

for row in rows:
    print(row) 

cursor.close()
connection.close()