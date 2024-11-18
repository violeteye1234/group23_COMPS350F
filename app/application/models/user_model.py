import cx_Oracle
import hashlib
import logging

class UserModel:
    def __init__(self):
        self.connection = None
        self.cursor = None
        self.set_database()
        self.logger = logging.getLogger(__name__)

    def set_database(self):
        try:
            if not self.connection:
                dsn = cx_Oracle.makedsn('oracleacademy.ouhk.edu.hk', 8998, sid='db1011')
                self.connection = cx_Oracle.connect(user='s1305732', password='13057320', dsn=dsn)
                self.cursor = self.connection.cursor()
        except cx_Oracle.DatabaseError as e:
            self.logger.error(f"Database connection error: {e}")
            raise

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def add_user(self, full_name, phone, email, password):
        try:
            self.set_database()
            hashed_password = self.hash_password(password)
            query = "INSERT INTO Users (FullName, PhoneNumber, Email, PassWord) VALUES (:1, :2, :3, :4)"
            values = (full_name, phone, email, hashed_password)
            self.cursor.execute(query, values)
            self.connection.commit()
        except cx_Oracle.DatabaseError as e:
            self.logger.error(f"Error adding user: {e}")
            raise

    def get_user_by_email(self, email):
        try:
            self.set_database()
            query = "SELECT * FROM Users WHERE Email = :1"
            self.cursor.execute(query, (email,))
            return self.cursor.fetchone()
        except cx_Oracle.DatabaseError as e:
            self.logger.error(f"Error fetching user by email: {e}")
            raise

    def get_user_by_email_and_password(self, email, password):
        try:
            self.set_database()
            hashed_password = self.hash_password(password)
            query = "SELECT * FROM Users WHERE Email = :1 AND PassWord = :2"
            self.cursor.execute(query, (email, hashed_password))
            return self.cursor.fetchone()
        except cx_Oracle.DatabaseError as e:
            self.logger.error(f"Error fetching user by email and password: {e}")
            raise

    def update_password(self, email, new_password):
        try:
            self.set_database()
            hashed_password = self.hash_password(new_password)
            query = "UPDATE Users SET PassWord = :1 WHERE Email = :2"
            self.cursor.execute(query, (hashed_password, email))
            self.connection.commit()
        except cx_Oracle.DatabaseError as e:
            self.logger.error(f"Error updating password: {e}")
            raise

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        self.connection = None
        self.cursor = None

