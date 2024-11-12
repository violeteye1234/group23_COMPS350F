from utils.page_controller import PageController
from .register_view import RegisterPageView
from models.user_model import UserModel  # 导入UserModel
import tkinter as tk

class RegisterPageController(PageController):
    def __init__(self, root, parent_container):
        super().__init__(root, parent_container)
        self.view = RegisterPageView(parent_container)
        self.view.set_controller(self)
        self.view.render()
        
        # 创建UserModel实例
        self.user_model = UserModel(db_path="path/to/your/database.db")

    def register(self, full_name: str, phone: str, email: str, password: str, confirm_password: str):
        self.root.logger.info(f"Attempting to register with full name: {full_name}, phone: {phone}, email: {email}, password: {password}, confirm password: {confirm_password}")
        
        if password != confirm_password:
            self.root.logger.error("Passwords do not match!")
            return
        
        # 添加注册逻辑，例如将用户信息保存到数据库
        self.root.logger.info("Registration successful!")
        self.root.show_page('Login')
    

        # 检查邮箱是否已存在
        if self.user_model.get_user_by_email(email):
            self.root.logger.error("Email already exists!")
            return

        # 将用户信息保存到数据库
        self.user_model.add_user(full_name, phone, email, password)
        self.root.logger.info("Registration successful!")
        self.root.show_page('Login')


    def go_to_login(self):
        self.root.show_page('Login')
    
    def cleanup(self):
        self.view.destroy()
        self.view = None

