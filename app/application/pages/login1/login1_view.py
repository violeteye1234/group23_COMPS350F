import tkinter as tk
from utils.page_view import PageView
from tkinter import PhotoImage
from pathlib import Path
from utils import CanvasButton

class Login1PageView(PageView):
    def __init__(self, parent):
        super().__init__(parent, height=609, width=783, bg="#FFFFFF", bd=0, highlightthickness=0, relief="ridge")
        self.image_path = self.image_path / "login1/images/"
        
        self.canvas = tk.Canvas(self, height=609, width=783, bg="#FFFFFF", bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack(fill="both", expand=True)
    
    def render(self):
        self.image_image_1 = PhotoImage(file=self.image_path / "image_1.png")
        self.canvas.create_image(520.75, 75.0, image=self.image_image_1)

        self.image_image_2 = PhotoImage(file=self.image_path / "image_2.png")
        self.canvas.create_image(520.75, 191.25, image=self.image_image_2)

        self.image_image_3 = PhotoImage(file=self.image_path / "image_3.png")
        self.canvas.create_image(520.75, 252.0, image=self.image_image_3)

        self.image_image_4 = PhotoImage(file=self.image_path / "image_4.png")
        self.canvas.create_image(614.25, 312.75, image=self.image_image_4)

        self.image_image_5 = PhotoImage(file=self.image_path / "image_5.png")
        self.canvas.create_image(93.0, 680.5, image=self.image_image_5)

        self.image_image_6 = PhotoImage(file=self.image_path / "image_6.png")
        self.canvas.create_image(398.0, 312.75, image=self.image_image_6)

        # 创建输入框和按钮
        self.create_widgets()

    def create_widgets(self):
        # 创建 "Email" 输入框
        self.email_entry = tk.Entry(self.canvas, bd=0, bg="#A9A9A9", highlightthickness=0)
        self.canvas.create_window(520.75, 191.25, window=self.email_entry, width=240, height=18)
        
        # 创建 "Password" 输入框
        self.password_entry = tk.Entry(self.canvas, bd=0, bg="#A9A9A9", highlightthickness=0, show="*")
        self.canvas.create_window(520.75, 252.0, window=self.password_entry, width=178, height=18)
        
        # 创建 "Login" 按钮
        self.login_button = CanvasButton(
            self.canvas,
            614.25, 312.75,
            self.image_path / "image_4.png",  
            self.on_login_button_click
        )

        # 创建 "Register" 按钮
        self.register_button = CanvasButton(
            self.canvas,
            93.0, 680.5,
            self.image_path / "image_5.png",  
            self.controller.register
        )

        # 创建 "Forgot Password" 按钮
        self.forgot_password_button = CanvasButton(
            self.canvas,
            398.0, 312.75,
            self.image_path / "image_6.png",  
            self.controller.forgot_password
        )

    def on_login_button_click(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        self.controller.login(email, password)

    def update(self):
        pass
    
    def set_controller(self, controller):
        self.controller = controller
