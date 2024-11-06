#pages/login_groundstaff/login_gs_view.py

import tkinter as tk
from tkinter import PhotoImage
from utils.page_view import PageView
from utils.canvas_button import CanvasButton 

class LoginPageViewGS(PageView):
    def __init__(self, parent):
        super().__init__(parent, bg = "#000000", height = 768, width = 1080, bd = 0, highlightthickness = 0, relief = "ridge")

    def render(self):
        self.image_image_1 = PhotoImage(file=self.image_path / "image_1.png")
        self.image_1 = self.canvas.create_image(539.5, 272.25, image=self.image_image_1)

        self.image_image_2 = PhotoImage(file=self.image_path / "image_2.png")
        self.image_2 = self.canvas.create_image(539.5, 388.5, image=self.image_image_2)

        self.image_image_3 = PhotoImage(file=self.image_path / "image_3.png")
        self.image_3 = self.canvas.create_image(539.5, 449.25, image=self.image_image_3)

        self.image_image_4 = PhotoImage(file=self.image_path / "image_4.png")
        self.image_4 = self.canvas.create_image(633.0, 510.0, image=self.image_image_4)
        
        #创建loginbutton
        self.login_button = CanvasButton(self.canvas, image = self.image_4, command = self.onclick1)
        self.login_button.place(x = 633.0, y = 510.0, anchor = "center")

        self.image_image_5 = PhotoImage(file=self.image_path / "image_5.png")
        self.image_5 = self.canvas.create_image(416.75, 510.0, image=self.image_image_5)

        #创建forgotpassward
        self.forgotpassword = CanvasButton(self.canvas, image = self.image_5, command = self.onclick2)
        self.login_button.place(x = 416.75, y = 510.0, anchor = "center")

        self.parent.set_frame(self)

    def onclick1(self):
        print("login clicked!")

    def onclick2(self):
        print("forgot clicked!")