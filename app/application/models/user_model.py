import cx_Oracle
from .config import Config

class UserModel:
    def __init__(self):
        dsn_tns = cx_Oracle.makedsn(Config.ORACLE_HOST, Config.ORACLE_PORT, service_name=Config.ORACLE_SID)
        self.conn = cx_Oracle.connect(user=Config.ORACLE_USER, password=Config.ORACLE_PASSWORD, dsn=dsn_tns)
        self.cursor = self.conn.cursor()

    def add_user(self, full_name, phone, email, password):
        query = "INSERT INTO Users (FullName, PhoneNumber, Email, PassWord) VALUES (:1, :2, :3, :4)"
        values = (full_name, phone, email, password)
        self.cursor.execute(query, values)
        self.conn.commit()

    def get_user_by_email(self, email):
        query = "SELECT * FROM Users WHERE Email = :1"
        self.cursor.execute(query, (email,))
        return self.cursor.fetchone()

    def get_user_by_email_and_password(self, email, password):
        query = "SELECT * FROM Users WHERE Email = :1 AND PassWord = :2"
        self.cursor.execute(query, (email, password))
        return self.cursor.fetchone()

    def update_password(self, email, new_password):
        query = "UPDATE Users SET PassWord = :1 WHERE Email = :2"
        self.cursor.execute(query, (new_password, email))
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()
