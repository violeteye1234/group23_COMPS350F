from utils.page_controller import PageController
from .login1_view import Login1PageView
from models.user_model import UserModel  # 导入UserModel
import tkinter as tk
from tkinter import messagebox

class Login1PageController(PageController):
    def __init__(self, root, parent_container):
        super().__init__(root, parent_container)
        self.view = Login1PageView(parent_container)
        self.view.set_controller(self)
        self.view.render()
        
        # 创建UserModel实例
        self.user_model = UserModel()

    def login(self, email: str, password: str):
        self.root.logger.info(f"Attempting to login with email: {email}, password: {password}")
        
        # 从数据库中检索用户信息
        user = self.user_model.get_user_by_email_and_password(email, password)
        
        if user:
            self.root.logger.info("Login successful!")
            # 这里添加跳转到主页面的逻辑
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
        self.user_model.close()
