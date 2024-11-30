import tkinter as tk  # Import tkinter for GUI components
from utils.page_view import PageView  # Import base class for page views
from tkinter import PhotoImage  # Import PhotoImage for handling images
from pathlib import Path  # Import Path for handling file paths
from utils import CanvasButton  # Import custom button class for canvas

# Define the Login1PageView class, inheriting from PageView
class Login1PageView(PageView):
    def __init__(self, parent):
        # Initialize the parent class with specified dimensions and background color
        super().__init__(parent, height=609, width=783, bg="#FFFFFF", bd=0, highlightthickness=0, relief="ridge")
        
        # Set the path for images used in the login1 page
        self.image_path = self.image_path / "login1/images/"
        
        # Create a canvas for the layout of the login page
        self.canvas = tk.Canvas(self, height=609, width=783, bg="#FFFFFF", bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack(fill="both", expand=True)  # Pack the canvas to fill the parent container
    
    def render(self):
        # Load and display images on the canvas at specified positions
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

        # Create input fields and buttons
        self.create_widgets()

    def create_widgets(self):
        # Create the "Email" input field
        self.email_entry = tk.Entry(self.canvas, bd=0, bg="#A9A9A9", highlightthickness=0)
        self.canvas.create_window(520.75, 191.25, window=self.email_entry, width=240, height=18)
        
        # Create the "Password" input field
        self.password_entry = tk.Entry(self.canvas, bd=0, bg="#A9A9A9", highlightthickness=0, show="*")
        self.canvas.create_window(520.75, 252.0, window=self.password_entry, width=178, height=18)
        
        # Create the "Login" button
        self.login_button = CanvasButton(
            self.canvas,
            614.25, 312.75,  # Position of the button
            self.image_path / "image_4.png",  # Image for the button
            self.on_login_button_click  # Function to call on button click
        )

        # Create the "Register" button
        self.register_button = CanvasButton(
            self.canvas,
            93.0, 680.5,  # Position of the button
            self.image_path / "image_5.png",  # Image for the button
            self.controller.register  # Function to call on button click
        )

        # Create the "Forgot Password" button
        self.forgot_password_button = CanvasButton(
            self.canvas,
            398.0, 312.75,  # Position of the button
            self.image_path / "image_6.png",  # Image for the button
            self.controller.forgot_password  # Function to call on button click
        )

    def on_login_button_click(self):
        # Retrieve email and password from input fields
        email = self.email_entry.get()
        password = self.password_entry.get()
        # Call the controller's login method with the retrieved credentials
        self.controller.login(email, password)

    def update(self):
        pass
    
    def set_controller(self, controller):
        # Set the controller for this view
        self.controller = controller