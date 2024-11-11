import cx_Oracle


# Use the provided connection details
dsn = cx_Oracle.makedsn('oracleacademy.ouhk.edu.hk', 8998, sid='db1011')
connection = cx_Oracle.connect(user='s1305732', password='13057320', dsn=dsn)

# If the connection is successful, print a message
print("Successfully connected to Oracle database!")

# Perform your database operations here

# Close connection
connection.close()
