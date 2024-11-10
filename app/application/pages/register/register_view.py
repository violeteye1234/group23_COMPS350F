import tkinter as tk
from utils.page_view import PageView
from tkinter import PhotoImage
from pathlib import Path
from utils import CanvasButton, ScrollableFrame

class RegisterPageView(PageView):
    def __init__(self, parent):
        super().__init__(parent, height=768, width=1080, bg="#F5F5F5", bd=0, highlightthickness=0, relief="ridge")
        self.image_path = self.image_path / "register/images/"
        
        self.canvas = tk.Canvas(self, height=768, width=1080, bg="#F5F5F5", bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack(fill="both", expand=True)
    
    def render(self):
        self.image_image_1 = PhotoImage(file=self.image_path / "image_1.png")
        self.canvas.create_image(540.0, 360.0, image=self.image_image_1)

        self.image_image_2 = PhotoImage(file=self.image_path / "image_2.png")
        self.canvas.create_image(539.0, 156.0, image=self.image_image_2)

        self.image_image_3 = PhotoImage(file=self.image_path / "image_3.png")
        self.canvas.create_image(338.0, 387.21728515625, image=self.image_image_3)

        self.image_image_4 = PhotoImage(file=self.image_path / "image_4.png")
        self.canvas.create_image(733.0, 281.0, image=self.image_image_4)

        self.image_image_5 = PhotoImage(file=self.image_path / "image_5.png")
        self.canvas.create_image(733.0, 334.0, image=self.image_image_5)

        self.image_image_6 = PhotoImage(file=self.image_path / "image_6.png")
        self.canvas.create_image(733.0, 387.0, image=self.image_image_6)

        self.image_image_7 = PhotoImage(file=self.image_path / "image_7.png")
        self.canvas.create_image(733.0, 440.0, image=self.image_image_7)

        self.image_image_8 = PhotoImage(file=self.image_path / "image_8.png")
        self.canvas.create_image(733.0, 493.0, image=self.image_image_8)

        self.image_image_9 = PhotoImage(file=self.image_path / "image_9.png")
        self.canvas.create_image(553.0, 627.0, image=self.image_image_9)

        # 创建输入框和按钮
        self.create_widgets()

    def create_widgets(self):
        # 创建 "Full Name" 输入框
        self.full_name_entry = tk.Entry(self.canvas, bd=0, bg="#D9D9D9", highlightthickness=0)
        self.canvas.create_window(733.0, 281.0, window=self.full_name_entry, width=362, height=22.5)
        
        # 创建 "Phone Number" 输入框
        self.phone_entry = tk.Entry(self.canvas, bd=0, bg="#D9D9D9", highlightthickness=0)
        self.canvas.create_window(733.0, 334.0, window=self.phone_entry, width=362, height=22.5)
        
        # 创建 "Email" 输入框
        self.email_entry = tk.Entry(self.canvas, bd=0, bg="#D9D9D9", highlightthickness=0)
        self.canvas.create_window(733.0, 387.0, window=self.email_entry, width=362, height=22.5)
        
        # 创建 "Password" 输入框
        self.password_entry = tk.Entry(self.canvas, bd=0, bg="#D9D9D9", highlightthickness=0, show="*")
        self.canvas.create_window(733.0, 440.0, window=self.password_entry, width=362, height=22.5)
        
        # 创建 "Confirm Password" 输入框
        self.confirm_password_entry = tk.Entry(self.canvas, bd=0, bg="#D9D9D9", highlightthickness=0, show="*")
        self.canvas.create_window(733.0, 493.0, window=self.confirm_password_entry, width=362, height=22.5)
        
        # 创建 "Register" 按钮
        self.register_button = CanvasButton(
            self.canvas,
            553.0, 627.0,
            self.image_path / "image_9.png",  
            lambda: self.controller.register(
                self.full_name_entry.get(),
                self.phone_entry.get(),
                self.email_entry.get(),
                self.password_entry.get(),
                self.confirm_password_entry.get()
            )
        )

    def update(self):
        pass
    
    def set_controller(self, controller):
        self.controller = controller