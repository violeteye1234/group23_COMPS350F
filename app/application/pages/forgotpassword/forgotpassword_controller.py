from utils.page_controller import PageController  # Import base class for page controllers
from .forgotpassword_view import ForgotPasswordPageView  # Import the view class for the forgot password page
from models.user_model import UserModel  # Import the user model for user data handling
import tkinter as tk  # Import tkinter for GUI components
from tkinter import messagebox  # Import messagebox for displaying alerts

# Define the ForgotPasswordPageController class, inheriting from PageController
class ForgotPasswordPageController(PageController):
    def __init__(self, root, parent_container):
        # Initialize the parent class with the root and parent container
        super().__init__(root, parent_container)
        
        # Create an instance of the ForgotPasswordPageView, passing the parent container
        self.view = ForgotPasswordPageView(parent_container)
        
        # Set this controller as the controller for the view
        self.view.set_controller(self)
        
        # Render the view
        self.view.render()
        
        # Create an instance of UserModel for handling user-related operations
        self.user_model = UserModel()

    def submit_forgot_password(self, email: str, new_password: str, confirm_password: str):
        # Log the attempt to reset the password for the given email
        self.root.logger.info(f"Attempting to reset password for email: {email}")
        
        # Check if the new password and confirmation password match
        if new_password != confirm_password:
            # Log an error if the passwords do not match
            self.root.logger.error("Reset password failed! Passwords do not match.")
            # Show an error message to the user
            messagebox.showerror("Reset Password Failed", "Passwords do not match. Please try again.")
            return
        
        # Check if the email exists in the system
        user = self.user_model.get_user_by_email(email)
        if not user:
            # Log an error if the email is invalid
            self.root.logger.error("Reset password failed! Invalid email address.")
            # Show an error message to the user
            messagebox.showerror("Reset Password Failed", "Invalid email address. Please try again.")
            return

        # Update the user's password in the database
        self.user_model.update_password(email, new_password)
        # Log a success message
        self.root.logger.info("Reset password successful!")
        # Show a success message to the user
        messagebox.showinfo("Password Reset", "Your password has been reset successfully.")
        # Navigate to the login page
        self.root.show_page('Login')

    def back_to_login(self):
        # Navigate back to the login page
        self.root.show_page('Login1')

    def cleanup(self):
        # Clean up resources when done
        self.view.destroy()  # Destroy the view
        self.view = None  # Clear the view reference
        self.user_model.close()  # Close the user model