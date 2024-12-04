from utils.page_controller import PageController
from .login1_view import Login1PageView
from models.user_model import UserModel
from models.database import Database
import tkinter as tk
from tkinter import messagebox
from models.sharedata import SharedData

class Login1PageController(PageController):
    
    def __init__(self, root, parent_container):
        super().__init__(root, parent_container)
        self.parent_container = parent_container
        self.view = Login1PageView(parent_container)
        self.view.set_controller(self)
        self.view.render()

        # Add a variable so that other pages can get it
        self.user_data = None


        # Creating a UserModel Instance
        self.user_model = UserModel()

    def login(self, email: str, password: str):
        self.root.logger.info(f"Attempting to login with email: {email}, password: {password}")
        
        # Retrieving user information from the database
        user = self.user_model.get_user_by_email_and_password(email, password)
        
        if user:
            self.root.logger.info("Login successful!")
            # pass email to method
            self.user_data = Database().get_user_data(email)
            # pass user_data to sharedata model
            SharedData.user_data = self.user_data

            # Add the logic of jumping to the main page here
            self.root.show_page('Main')
        else:
            self.root.logger.error("Login failed! Invalid email or password.")
            # Pop-up window displays error message
            messagebox.showerror("Login Failed", "Invalid email or password. Please try again.")

    def register(self):
        self.root.show_page('Register')

    def forgot_password(self):
        self.root.show_page('ForgotPassword')

    def cleanup(self):
        self.view.destroy()
        self.view = None
        self.user_model.close()
