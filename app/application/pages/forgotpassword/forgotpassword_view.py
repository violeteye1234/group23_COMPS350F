import tkinter as tk
from utils.page_view import PageView
from tkinter import PhotoImage
from pathlib import Path
from utils import CanvasButton

class ForgotPasswordPageView(PageView):
    def __init__(self, parent):
        # Initialize the ForgotPasswordPageView with specified dimensions and background color
        super().__init__(parent, height=599, width=700, bg="#FFFFFF", bd=0, highlightthickness=0, relief="ridge")

        # Set the path to images for the forgot password view
        self.image_path = self.image_path / "forgotpassword/images/"
        
        # Create a canvas to hold images and input fields
        self.canvas = tk.Canvas(self, height=599, width=700, bg="#FFFFFF", bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack(fill="both", expand=True)
    
    def render(self):
        # Load and display images on the canvas
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

        # Create input fields and buttons
        self.create_widgets()

    def create_widgets(self):
        # Create "Email" input field
        self.email_entry = tk.Entry(self.canvas, bd=0, bg="#A9A9A9", highlightthickness=0)
        self.canvas.create_window(510.0, 224.0, window=self.email_entry, width=330, height=35)  
        
        # Create "New Password" input field
        self.new_password_entry = tk.Entry(self.canvas, bd=0, bg="#A9A9A9", highlightthickness=0, show="*")
        self.canvas.create_window(510.0, 336.0, window=self.new_password_entry, width=130, height=35)  
        
        # Create "Confirm New Password" input field
        self.confirm_password_entry = tk.Entry(self.canvas, bd=0, bg="#A9A9A9", highlightthickness=0, show="*")
        self.canvas.create_window(510.0, 448.0, window=self.confirm_password_entry, width=50, height=35)  
        
        # Create "Submit" button
        self.submit_button = CanvasButton(
            self.canvas,
            500.0, 574.0,  # Coordinates for the button
            self.image_path / "image_5.png",  
            self.on_submit_button_click
        )

        # create "Back" button
        self.register_button = tk.Button(
            self.canvas,
            text="Back",
            command=lambda: self.controller.back_to_login(),
            bg="#3399FF",
            fg="white"
        )
        self.canvas.create_window(100, 600, window=self.register_button, width=150, height=50)


    def on_submit_button_click(self):
        # Get values from input fields and call the controller method to handle submission
        email = self.email_entry.get()
        new_password = self.new_password_entry.get()
        confirm_password = self.confirm_password_entry.get()
        self.controller.submit_forgot_password(email, new_password, confirm_password)

    def update(self):
        pass
    
    def set_controller(self, controller):
        # Set the controller for handling events and actions
        self.controller = controller
