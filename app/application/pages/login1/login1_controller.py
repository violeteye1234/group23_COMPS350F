from utils.page_controller import PageController
from .login1_view import Login1PageView
import tkinter as tk
from tkinter import messagebox

class Login1PageController(PageController):
    def __init__(self, root, parent_container):
        super().__init__(root, parent_container)
        self.view = Login1PageView(parent_container)
        self.view.set_controller(self)
        self.view.render()

    def login(self, email: str, password: str):
        self.root.logger.info(f"Attempting to login with email: {email}, password: {password}")
        
        # 固定的电子邮件和密码
        correct_email = "123"
        correct_password = "123"
        
        if email == correct_email and password == correct_password:
            self.root.logger.info("Login successful!")
            # 可以在这里添加跳转到主页面的逻辑，例如：
            self.root.show_page('Main')
        else:
            self.root.logger.error("Login failed! Invalid email or password.")
            # 弹窗显示错误信息
            messagebox.showerror("Login Failed", "Invalid email or password. Please try again.")

    def register(self):
        self.root.show_page('Register')

    def forgot_password(self):
        self.root.show_page('ForgotPassword')

    def cleanup(self):
        self.view.destroy()
        self.view = None