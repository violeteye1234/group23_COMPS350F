# pages/login/login_view.py

import tkinter as tk  # Import tkinter for GUI components
from utils.page_view import PageView  # Import base class for page views

# Define the LoginPageView class, inheriting from PageView
class LoginPageView(PageView):
    def __init__(self, parent):
        # Initialize the parent class with specified dimensions and background color
        super().__init__(parent, height=768, width=1080, bg="#F5F5F5", bd=0, highlightthickness=0, relief="ridge")
        
        # Set the path for images used in the main page
        self.image_path = self.image_path / "main_page/images/"
        
        # Create a canvas for the layout of the login page
        self.canvas = tk.Canvas(self, height=768, width=1080, bg="#F5F5F5", bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack(fill="both", expand=True)  # Pack the canvas to fill the parent container
        self.create_widgets()  # Call method to create widgets on the canvas
    
    def create_widgets(self):
        # Create the "Login" button
        self.login_button = tk.Button(
            self.canvas,
            text="Login",  # Text displayed on the button
            command=lambda: self.controller.login_default()  # Function to call on button click
        )
        self.canvas.create_window(540, 300, window=self.login_button, width=200, height=50)  # Position the button on the canvas
        
        # Create the "Register" button
        self.register_button = tk.Button(
            self.canvas,
            text="Register",  # Text displayed on the button
            command=lambda: self.controller.go_to_register()  # Function to call on button click
        )
        self.canvas.create_window(540, 350, window=self.register_button, width=200, height=50)  # Position the button on the canvas

        # Create a "Test" button
        self.test_button = tk.Button(
            self.canvas,
            text="test",  # Text displayed on the button
            command=lambda: self.controller.jump_to_main()  # Function to call on button click
        )
        self.canvas.create_window(540, 400, window=self.test_button, width=200, height=50)  # Position the button on the canvas
    
    def render(self):
        # Pack the canvas to fill the available space
        self.pack(fill='both', expand=True)
    
    def clear_content(self):
        # Clear all content from the canvas
        self.canvas.delete("all")
    
    def update(self):
        pass