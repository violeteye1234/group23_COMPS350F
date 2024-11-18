import cx_Oracle

class UserModel:
    def __init__(self):
        self.connection = None
        self.cursor = None
        self.set_database()

    def set_database(self):
        if not self.connection:
            dsn = cx_Oracle.makedsn('oracleacademy.ouhk.edu.hk', 8998, sid='db1011')
            self.connection = cx_Oracle.connect(user='s1305732', password='13057320', dsn=dsn)
            self.cursor = self.connection.cursor()

    def add_user(self, full_name, phone, email, password):
        self.set_database()
        query = "INSERT INTO Users (FullName, PhoneNumber, Email, PassWord) VALUES (:1, :2, :3, :4)"
        values = (full_name, phone, email, password)
        self.cursor.execute(query, values)
        self.connection.commit()

    def get_user_by_email(self, email):
        self.set_database()
        query = "SELECT * FROM Users WHERE Email = :1"
        self.cursor.execute(query, (email,))
        return self.cursor.fetchone()

    def get_user_by_email_and_password(self, email, password):
        self.set_database()
        query = "SELECT * FROM Users WHERE Email = :1 AND PassWord = :2"
        self.cursor.execute(query, (email, password))
        return self.cursor.fetchone()

    def update_password(self, email, new_password):
        self.set_database()
        query = "UPDATE Users SET PassWord = :1 WHERE Email = :2"
        self.cursor.execute(query, (new_password, email))
        self.connection.commit()

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        self.connection = None
        self.cursor = None
