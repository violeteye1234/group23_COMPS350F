from utils.page_controller import PageController
from .forgotpassword_view import ForgotPasswordPageView
import tkinter as tk
from tkinter import messagebox

class ForgotPasswordPageController(PageController):
    def __init__(self, root, parent_container):
        super().__init__(root, parent_container)
        self.view = ForgotPasswordPageView(parent_container)
        self.view.set_controller(self)
        self.view.render()

    def submit_forgot_password(self, email: str, new_password: str, confirm_password: str):
        self.root.logger.info(f"Attempting to reset password for email: {email}")
        
        # 固定的电子邮件
        correct_email = "123"
        
        if email != correct_email:
            self.root.logger.error("Reset password failed! Invalid email address.")
            messagebox.showerror("Reset Password Failed", "Invalid email address. Please try again.")
            return
        
        if new_password != confirm_password:
            self.root.logger.error("Reset password failed! Passwords do not match.")
            messagebox.showerror("Reset Password Failed", "Passwords do not match. Please try again.")
            return
        
        # 这里添加实际的密码重置逻辑，例如更新数据库中的密码
        self.root.logger.info("Reset password successful!")
        messagebox.showinfo("Password Reset", "Your password has been reset successfully.")
        self.root.show_page('Login')

    def back_to_login(self):
        self.root.show_page('Login')

    def cleanup(self):
        self.view.destroy()
        self.view = None