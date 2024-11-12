# models/database.py
from models.user import User
from models.my_flight import MyFlight
from models.my_baggage import MyBaggage
from models.notification import Notification
from typing import Any
import cx_Oracle

dsn = cx_Oracle.makedsn('oracleacademy.ouhk.edu.hk', 8998, sid='db1011')
connection = cx_Oracle.connect(user='s1305732', password='13057320', dsn=dsn)
print("Successfully connected to Oracle database!")
cursor = connection.cursor()
query = "SELECT * FROM table_name"  #change table_name


class Database:
    def __init__(self):
        self.connection = None
        self.cursor = None


    def set_database(self):
        if not self.connection:
            dsn = cx_Oracle.makedsn('oracleacademy.ouhk.edu.hk', 8998, sid='db1011')
            self.connection = cx_Oracle.connect(user='s1305732', password='13057320', dsn=dsn)
            self.cursor = self.connection.cursor()

    #def __init__(self, db_name='application.db'):
       # self.database = None
        
    def get_user_info(self, email:str) -> User:
        self.set_database() #ensure database connected
        query = "SELECT user_id, username, email FROM users WHERE email = :email" #SQL query to select user information by email
        self.cursor.execute(query, email=email) #execute email 
        row = self.cursor.fetchone() #fetch the first row
        user = User(row[0], row[1], row[2]) if row else None
        return user
    
    def get_flights(self, email:str) -> list[MyFlight]:
        self.set_database()
        query = "SELECT flight_id, flight_details FROM flights WHERE user_email = :email"
        self.cursor.execute(query, email=email)
        flights = [MyFlight(row[0], row[1]) for row in self.cursor.fetchall()]
        return flights
    
    def get_baggages(self, email:str) -> list[MyBaggage]:
        self.set_database()
        query = "SELECT baggage_id, baggage_details FROM baggages WHERE user_email = :email"
        self.cursor.execute(query, email=email)
        baggages = [MyBaggage(row[0], row[1]) for row in self.cursor.fetchall()]
        return baggages
    
    def registration(self, user_info:dict[str, Any]) -> None:
        self.set_database()
        query = "INSERT INTO users (full_name, phone, email, password) VALUES (:full_name, :phone, :email, :password)"
        self.cursor.execute(query, full_name=user_info['full_name'], phone=user_info['phone'], email=user_info['email'], password=user_info['password'])
        self.connection.commit()

    def execute_sql(self, sql_command:str) -> str:
        self.set_database()
        self.cursor.execute(sql_command)
        self.connection.commit()
        return "SQL command executed successfully."
    
    def create_connection(self) -> None:
        self.set_database()
    
    def close_connection(self) -> None:
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        self.connection = None
        self.cursor = None

db = Database()

# Execute a custom SQL command
result = db.execute_sql("UPDATE users SET status = 'active' WHERE user_id = 123")
print(result)

# Close the connection
db.close_connection()
