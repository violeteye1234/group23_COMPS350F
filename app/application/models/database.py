# models/database.py
'''
from models.user import User
from models.my_flight import MyFlight
from models.my_baggage import MyBaggage
from models.notification import Notification
from typing import Any
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


# for coding part test there program on window system, please common all of this file.
# keep sandeep work here

from models.user import User
from models.my_flight import MyFlight
from models.my_baggage import MyBaggage
from models.notification import Notification
from typing import Any


import cx_Oracle 
import os

# please write your own Oracle client path
# os.environ["PATH"] = r"C:\oracle client\instantclient-basic-windows.x64-23.6.0.24.10\instantclient_23_6" + ";" + os.environ["PATH"]

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
        row = self.cursor.fetchone() #fetch the first row from result set
        user = User(row[0], row[1], row[2]) if row else None #user object created if row returned else none
        return user
    
    def get_flights(self, email:str) -> list[MyFlight]:
        self.set_database()#connected
        query = "SELECT flight_id, flight_details FROM flights WHERE user_email = :email" #SQL
        self.cursor.execute(query, email=email) #execute query with email
        flights = [MyFlight(row[0], row[1]) for row in self.cursor.fetchall()] #fetch all rows and create mybaggage objects
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
#example 
db = Database()  #create oinstance

# Execute SQL 
result = db.execute_sql("UPDATE users SET status = 'active' WHERE user_id = __")
print(result) #"SQL command executed successfully."

# Close the connection
db.close_connection()
'''

from models.user import User
from models.my_flight import MyFlight
from models.my_baggage import MyBaggage
from models.notification import Notification
from typing import Any
import cx_Oracle 
import os

# Please replace with your own Oracle client path
# os.environ["PATH"] = r"C:\oracle client\instantclient-basic-windows.x64-23.6.0.24.10\instantclient_23_6" + ";" + os.environ["PATH"]

dsn = cx_Oracle.makedsn('oracleacademy.ouhk.edu.hk', 8998, sid='db1011')
connection = cx_Oracle.connect(user='s1305732', password='13057320', dsn=dsn)
print("Successfully connected to Oracle database!")
cursor = connection.cursor()
query = "SELECT * FROM table_name"  # Change table_name

class Database:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def set_database(self):
        if not self.connection:
            dsn = cx_Oracle.makedsn('oracleacademy.ouhk.edu.hk', 8998, sid='db1011')
            self.connection = cx_Oracle.connect(user='s1305732', password='13057320', dsn=dsn)
            self.cursor = self.connection.cursor()

    def get_user_info(self, email: str) -> User:
        self.set_database()  # Ensure database is connected
        query = "SELECT userid, fullname, email FROM users WHERE email = :email"  # SQL query to select user information by email
        self.cursor.execute(query, email=email)  # Execute query with email
        row = self.cursor.fetchone()  # Fetch the first row from result set
        user = User(row[0], row[1], row[2]) if row else None  # Create user object if row returned, else None
        return user
    
    def execute_sql(self, sql_command: str, **bind_vars) -> str:
        self.set_database()
        self.cursor.execute(sql_command, bind_vars)
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
    
    # Create library to store the user data
    def get_user_data(self, email: str) -> dict:
        self.set_database()
        user_data = {}

        # get data from users table
        query = "SELECT userid, fullname, email, phonenumber, status FROM users WHERE email = :email"
        self.cursor.execute(query, email = email)
        user_row = self.cursor.fetchone()
        if user_row:
            user_data['users'] = {
                'userid': user_row[0],
                'fullname': user_row[1],
                'email': user_row[2],
                'phonenumber': user_row[3],
                'status': user_row[4]
            }

            # get data from bookings table
            query = "SELECT bookingid, flightid, bookingdate FROM bookings WHERE userid = :userid"
            self.cursor.execute(query, userid = user_row[0])
            bookings = self.cursor.fetchall()
            user_data['bookings'] = []
            flight_ids = []
            for booking in bookings:
                user_data['bookings'].append({
                    'bookingid': booking[0],
                    'flightid': booking[1],
                    'bookingdata': booking[2]
                })
                flight_ids.append(booking[1])

            # get data from flights table
            user_data['flights'] = []
            for filght_id in flight_ids:
                query = "SELECT flightnumber, departureairport, arrivalairport,  departuretime, arrivaltime, gate, status FROM flights WHERE flightid = :flightid"
                self.cursor.execute(query, flightid = filght_id)
                flight = self.cursor.fetchone()
                if flight:
                    user_data['flights'].append({
                        'flightnumber': flight[0],
                        'departureairport': flight[1],
                        'arrivalairport': flight[2],
                        'departuretime': flight[3],
                        'arrivaltime': flight[4],
                        'gate': flight[5],
                        'status': flight[6]
                    })

            # get data form baggage table
            query = "SELECT baggageid, flightid, userid, baggageweight, baggagenumber, status FROM baggage WHERE userid = :userid"
            self.cursor.execute(query, userid=user_row[0])
            baggages = self.cursor.fetchall()
            user_data['baggages'] = []
            for baggage in baggages:
                user_data['baggages'].append({
                    'baggageid': baggage[0],
                    'flightid': baggage[1],
                    'userid': baggage[2],
                    'baggageweight': baggage[3],
                    'baggagenumber': baggage[4],
                    'status': baggage[5]
                })

            #get data from flightseats table
            user_data['flightseats'] = []
            for flight_id in flight_ids:
                query = "SELECT seatid, seatnumber, seatstatus FROM flightseats WHERE flightid = :flightid"
                self.cursor.execute(query, flightid=flight_id)
                seats = self.cursor.fetchall()
                for seat in seats:
                    user_data['flightseats'].append({
                        'seatid': seat[0],
                        'seatnumber': seat[1],
                        'seatstatus': seat[2]
                    })
        return user_data