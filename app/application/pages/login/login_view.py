# pages/login/login_view.py

import tkinter as tk
from ..page_view import PageView

class LoginPageView(PageView):
    def __init__(self, parent):
        super().__init__(parent, height = 1024, width = 1440, bg="#F5F5F5", bd=0, highlightthickness=0, relief="ridge")
        self.image_path = self.image_path / "main_page/images/"
        
        self.canvas = tk.Canvas(self, height = 1024, width = 1440, bg="#F5F5F5", bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack(fill="both", expand=True)
        self.create_widgets()
    
    def create_widgets(self):
        # 創建 "Login" 按鈕
        self.login_button = tk.Button(
            self.canvas,
            text="Login",
            command=lambda: self.controller.login("123", "123")  # 使用 lambda 傳遞參數
        )
        self.canvas.create_window(720, 600, window=self.login_button, width=200, height=50)
        
        # 創建 "Register" 按鈕
        self.register_button = tk.Button(
            self.canvas,
            text="Register",
            command=lambda: self.controller.go_to_register()
        )
        self.canvas.create_window(720, 700, window=self.register_button, width=200, height=50)
    
    def render(self):
        self.pack(fill='both', expand=True)
    
    def clear_content(self):
        self.canvas.delete("all")
    
    def update(self):
        pass
