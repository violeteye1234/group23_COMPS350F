from utils.page_controller import PageController  # Import base class for page controllers
from .login1_view import Login1PageView  # Import the view class for the login1 page
from models.user_model import UserModel  # Import the user model for handling user data
from models.database import Database  # Import the database class for data retrieval
import tkinter as tk  # Import tkinter for GUI components
from tkinter import messagebox  # Import messagebox for displaying alerts
from models.sharedata import SharedData  # Import shared data model for cross-page data sharing

# Define the Login1PageController class, inheriting from PageController
class Login1PageController(PageController):
    
    def __init__(self, root, parent_container):
        # Initialize the parent class with the root and parent container
        super().__init__(root, parent_container)
        self.parent_container = parent_container  # Store the parent container reference
        self.view = Login1PageView(parent_container)  # Create the login view
        self.view.set_controller(self)  # Set this controller as the controller for the view
        self.view.render()  # Render the view

        # Variable to hold user data accessible from other pages
        self.user_data = None

        # Create an instance of UserModel for user-related operations
        self.user_model = UserModel()

    def login(self, email: str, password: str):
        # Log the attempt to log in with the provided email and password
        self.root.logger.info(f"Attempting to login with email: {email}, password: {password}")
        
        # Retrieve user information from the database using the provided credentials
        user = self.user_model.get_user_by_email_and_password(email, password)
        
        if user:
            # Log successful login
            self.root.logger.info("Login successful!")
            # Get user data from the database using the email
            self.user_data = Database().get_user_data(email)
            # Store user data in the shared data model for access across pages
            SharedData.user_data = self.user_data

            # Logic to navigate to the main page after successful login
            self.root.show_page('Main')
        else:
            # Log failed login attempt
            self.root.logger.error("Login failed! Invalid email or password.")
            # Show an error message box to the user
            messagebox.showerror("Login Failed", "Invalid email or password. Please try again.")

    def register(self):
        # Navigate to the registration page
        self.root.show_page('Register')

    def forgot_password(self):
        # Navigate to the forgot password page
        self.root.show_page('ForgotPassword')

    def cleanup(self):
        # Clean up resources when done
        self.view.destroy()  # Destroy the view
        self.view = None  # Clear the view reference
        self.user_model.close()  # Close the user model