#pages/login_groundstaff/login_gs_view.py

import tkinter as tk
from tkinter import PhotoImage
from utils.page_view import PageView
from utils.canvas_button import CanvasButton 

class LoginPageViewGS(PageView):
    #def __init__(self, parent):
    def __init__(self, parent, login_command, forgot_command):
        super().__init__(parent, bg = "#000000", height = 768, width = 1080, bd = 0, highlightthickness = 0, relief = "ridge")
        #try
        self.login_command = login_command
        self.forgot_command = forgot_command
        self.image_path = self.image_path / "login_groundstaff/images/"

        self.canvas = tk.Canvas(self, bg="#000000", height=768, width=1080, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack(fill="both", expand=True)

    def render(self):
        self.image_image_1 = PhotoImage(file=self.image_path / "image_1.png")
        self.image_1 = self.canvas.create_image(539.5, 272.25, image=self.image_image_1)

        self.image_image_2 = PhotoImage(file=self.image_path / "image_2.png")
        self.image_2 = self.canvas.create_image(539.5, 388.5, image=self.image_image_2)

        self.image_image_3 = PhotoImage(file=self.image_path / "image_3.png")
        self.image_3 = self.canvas.create_image(539.5, 449.25, image=self.image_image_3)

        #self.image_image_4 = PhotoImage(file=self.image_path / "image_4.png")
        #self.image_4 = self.canvas.create_image(633.0, 510.0, image=self.image_image_4)

        #self.image_image_5 = PhotoImage(file=self.image_path / "image_5.png")
        #self.image_5 = self.canvas.create_image(416.75, 510.0, image=self.image_image_5)
        
        #创建input box
        self.entry_user_name = tk.Entry(self.canvas, width = 30)
        self.entry_user_name.place(x = 539.5, y = 388.5, anchor = "center")

        self.entry_password = tk.Entry(self.canvas, show = "*", width = 30)
        self.entry_password.place(x = 539.5, y=449.25, anchor="center")

        #创建loginbutton
        #from pages.login_groundstaff.login_gs_controller import LoginGS_PageController
        #self.login_button = CanvasButton(self.canvas, image = self.image_4, command = LoginGS_PageController.onclick1)
        self.login_button = CanvasButton(self.canvas, 633.0, 510.0, self.image_path / "image_4.png", lambda: self.login_command)

        #创建forgotpassward
        #self.forgotpassword = CanvasButton(self.canvas, 416.75, 510.0, r".image/image_5", self.forgot_command)

        self.login_button = CanvasButton(self.canvas, 416.75, 510.0, self.image_path / "image_5.png", lambda: self.forgot_command)

    def update(self):
        pass