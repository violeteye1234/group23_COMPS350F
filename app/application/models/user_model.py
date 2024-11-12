# user_model.py

# keep terry work here.

'''
import sqlite3
from pathlib import Path

class UserModel:
    def __init__(self, db_path):
        self.db_path = db_path
        self._create_user_table()

    def _create_user_table(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    full_name TEXT NOT NULL,
                    phone TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL
                )
            )
            conn.commit()

    def add_user(self, full_name, phone, email, password):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                INSERT INTO users (full_name, phone, email, password)
                VALUES (?, ?, ?, ?)
            , (full_name, phone, email, password))
            conn.commit()

    def get_user_by_email(self, email):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                SELECT * FROM users WHERE email = ?
            , (email,))
            return cursor.fetchone()
'''