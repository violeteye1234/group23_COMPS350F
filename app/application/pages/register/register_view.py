import tkinter as tk  # Import tkinter for GUI components
from utils.page_view import PageView  # Import base class for page views
from tkinter import PhotoImage  # Import PhotoImage for handling images
from pathlib import Path  # Import Path for file path handling
from utils import CanvasButton, ScrollableFrame  # Import custom button and scrollable frame classes

# Define the RegisterPageView class, inheriting from PageView
class RegisterPageView(PageView):
    def __init__(self, parent):
        # Initialize the parent class with specified dimensions and background color
        super().__init__(parent, height=768, width=1080, bg="#F5F5F5", bd=0, highlightthickness=0, relief="ridge")
        
        # Set the path for images used in the registration page
        self.image_path = self.image_path / "register/images/"
        
        # Create a canvas for the layout of the Register page
        self.canvas = tk.Canvas(self, height=768, width=1080, bg="#F5F5F5", bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack(fill="both", expand=True)  # Pack the canvas to fill the parent container

    def render(self):
        # Load and display images on the canvas
        self.image_image_1 = PhotoImage(file=self.image_path / "image_1.png")
        self.canvas.create_image(540.0, 360.0, image=self.image_image_1)

        self.image_image_2 = PhotoImage(file=self.image_path / "image_2.png")
        self.canvas.create_image(539.0, 156.0, image=self.image_image_2)

        self.image_image_3 = PhotoImage(file=self.image_path / "image_3.png")
        self.canvas.create_image(338.0, 387.2, image=self.image_image_3)

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

        # Call the method to create input fields and buttons
        self.create_widgets()

    def create_widgets(self):
        # Create input fields and buttons for the registration form

        # Full Name input field
        self.full_name_entry = tk.Entry(self.canvas, bd=0, bg="#D9D9D9", highlightthickness=0)
        self.canvas.create_window(733.0, 281.0, window=self.full_name_entry, width=362, height=22.5)
        
        # Phone Number input field
        self.phone_entry = tk.Entry(self.canvas, bd=0, bg="#D9D9D9", highlightthickness=0)
        self.canvas.create_window(733.0, 334.0, window=self.phone_entry, width=362, height=22.5)
        
        # Email input field
        self.email_entry = tk.Entry(self.canvas, bd=0, bg="#D9D9D9", highlightthickness=0)
        self.canvas.create_window(733.0, 387.0, window=self.email_entry, width=362, height=22.5)
        
        # Password input field (hidden input)
        self.password_entry = tk.Entry(self.canvas, bd=0, bg="#D9D9D9", highlightthickness=0, show="*")
        self.canvas.create_window(733.0, 440.0, window=self.password_entry, width=362, height=22.5)
        
        # Confirm Password input field (hidden input)
        self.confirm_password_entry = tk.Entry(self.canvas, bd=0, bg="#D9D9D9", highlightthickness=0, show="*")
        self.canvas.create_window(733.0, 493.0, window=self.confirm_password_entry, width=362, height=22.5)
        
        # Register button that triggers the registration process
        self.register_button = CanvasButton(
            self.canvas,
            553.0, 627.0,
            self.image_path / "image_9.png",  # Button image
            lambda: self.controller.register(
                self.full_name_entry.get(),  # Get full name
                self.phone_entry.get(),       # Get phone number
                self.email_entry.get(),       # Get email
                self.password_entry.get(),    # Get password
                self.confirm_password_entry.get()  # Get confirm password
            )
        )

    def update(self):
        # Placeholder for update logic (currently does nothing)
        pass
    
    def set_controller(self, controller):
        # Set the controller for this view
        self.controller = controller