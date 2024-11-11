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
    def __init__(self, db_name='application.db'):
        self.database = None
        
    def get_user_info(self, email:str) -> User:
        pass
    
    def get_flights(self, email:str) -> list[MyFlight]:
        pass
    
    def get_baggages(self, email:str) -> list[MyBaggage]:
        pass
    
    def registration(self, user_info:dict[str, Any]) -> None:
        pass

    def set_database(self) -> None:
        pass
    
    def execute_sql(self, sql_command:str) -> str:
        pass
    
    def create_connection(self) -> None:
        pass
    
    def close_connection(self) -> None:
        pass
cursor.execute(query)

rows = cursor.fetchall()

for row in rows:
    print(row) 

cursor.close()
connection.close()
