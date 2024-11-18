import tkinter as tk
from utils.page_view import PageView
from tkinter import PhotoImage
from pathlib import Path
from utils import CanvasButton

class ForgotPasswordPageView(PageView):
    def __init__(self, parent):
        super().__init__(parent, height=599, width=700, bg="#FFFFFF", bd=0, highlightthickness=0, relief="ridge")
        self.image_path = self.image_path / "forgotpassword/images/"
        
        self.canvas = tk.Canvas(self, height=599, width=700, bg="#FFFFFF", bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack(fill="both", expand=True)
    
    def render(self):
        self.image_image_1 = PhotoImage(file=self.image_path / "image_1.png")
        self.canvas.create_image(500.0, 100.0, image=self.image_image_1)  

        self.image_image_2 = PhotoImage(file=self.image_path / "image_2.png")
        self.canvas.create_image(510.0, 224.0, image=self.image_image_2)  

        self.image_image_3 = PhotoImage(file=self.image_path / "image_3.png")
        self.canvas.create_image(510.0, 336.0, image=self.image_image_3)  

        self.image_image_4 = PhotoImage(file=self.image_path / "image_4.png")
        self.canvas.create_image(510.0, 448.0, image=self.image_image_4)  

        self.image_image_5 = PhotoImage(file=self.image_path / "image_5.png")
        self.canvas.create_image(500.0, 574.0, image=self.image_image_5)  

        # 创建输入框和按钮
        self.create_widgets()

    def create_widgets(self):
        # 创建 "Email" 输入框
        self.email_entry = tk.Entry(self.canvas, bd=0, bg="#A9A9A9", highlightthickness=0)
        self.canvas.create_window(510.0, 224.0, window=self.email_entry, width=330, height=35)  
        
        # 创建 "New Password" 输入框
        self.new_password_entry = tk.Entry(self.canvas, bd=0, bg="#A9A9A9", highlightthickness=0, show="*")
        self.canvas.create_window(510.0, 336.0, window=self.new_password_entry, width=130, height=35)  
        
        # 创建 "Confirm New Password" 输入框
        self.confirm_password_entry = tk.Entry(self.canvas, bd=0, bg="#A9A9A9", highlightthickness=0, show="*")
        self.canvas.create_window(510.0, 448.0, window=self.confirm_password_entry, width=50, height=35)  
        
        # 创建 "Submit" 按钮
        self.submit_button = CanvasButton(
            self.canvas,
            500.0, 574.0,  # x 坐标增加 150 (70 + 80)
            self.image_path / "image_5.png",  
            self.on_submit_button_click
        )

    def on_submit_button_click(self):
        email = self.email_entry.get()
        new_password = self.new_password_entry.get()
        confirm_password = self.confirm_password_entry.get()
        self.controller.submit_forgot_password(email, new_password, confirm_password)

    def update(self):
        pass
    
    def set_controller(self, controller):
        self.controller = controller
