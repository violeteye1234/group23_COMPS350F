# register_page_controller.py

from utils.page_controller import PageController  # Import base class for page controllers
from .register_view import RegisterPageView  # Import the view class for the registration page
from models.user_model import UserModel  # Import UserModel for user data handling
import tkinter as tk  # Import tkinter for GUI components

# Define the RegisterPageController class, inheriting from PageController
class RegisterPageController(PageController):
    def __init__(self, root, parent_container):
        # Initialize the parent class with the root and parent container
        super().__init__(root, parent_container)
        
        # Create the registration page view
        self.view = RegisterPageView(parent_container)
        self.view.set_controller(self)  # Set this controller for the view
        self.view.render()  # Render the view
        
        # Create an instance of UserModel to handle user data
        self.user_model = UserModel()

    def register(self, full_name: str, phone: str, email: str, password: str, confirm_password: str):
        # Log the registration attempt
        self.root.logger.info(f"Attempting to register with full name: {full_name}, phone: {phone}, email: {email}, password: {password}, confirm password: {confirm_password}")
        
        # Check if passwords match
        if password != confirm_password:
            self.root.logger.error("Passwords do not match!")
            return
        
        # Check if the email already exists in the database
        if self.user_model.get_user_by_email(email):
            self.root.logger.error("Email already exists!")
            return

        # Save the user information to the database
        self.user_model.add_user(full_name, phone, email, password)
        self.root.logger.info("Registration successful!")  # Log successful registration
        self.root.show_page('Login')  # Navigate to the login page

    def go_to_login(self):
        # Navigate to the login page
        self.root.show_page('Login')
    
    def cleanup(self):
        # Clean up resources when the controller is no longer needed
        self.view.destroy()  # Destroy the view
        self.view = None  # Remove reference to the view
        self.user_model.close()  # Close the user model