from utils.page_controller import PageController
from .forgotpassword_view import ForgotPasswordPageView
from models.user_model import UserModel  # 导入UserModel
import tkinter as tk
from tkinter import messagebox

class ForgotPasswordPageController(PageController):
    def __init__(self, root, parent_container):
        super().__init__(root, parent_container)
        self.view = ForgotPasswordPageView(parent_container)
        self.view.set_controller(self)
        self.view.render()
        
        # Creating a UserModel Instance
        self.user_model = UserModel()

    def submit_forgot_password(self, email: str, new_password: str, confirm_password: str):
        self.root.logger.info(f"Attempting to reset password for email: {email}")
        
        if new_password != confirm_password:
            self.root.logger.error("Reset password failed! Passwords do not match.")
            messagebox.showerror("Reset Password Failed", "Passwords do not match. Please try again.")
            return
        
        # Check if the mailbox exists
        user = self.user_model.get_user_by_email(email)
        if not user:
            self.root.logger.error("Reset password failed! Invalid email address.")
            messagebox.showerror("Reset Password Failed", "Invalid email address. Please try again.")
            return

        # Update User Password
        self.user_model.update_password(email, new_password)
        self.root.logger.info("Reset password successful!")
        messagebox.showinfo("Password Reset", "Your password has been reset successfully.")
        self.root.show_page('Login')

    def back_to_login(self):
        self.root.show_page('Login1')

    def cleanup(self):
        self.view.destroy()
        self.view = None
        self.user_model.close()
