import tkinter as tk  # Import tkinter for GUI components
from utils.page_view import PageView  # Import base class for page views
from tkinter import PhotoImage  # Import PhotoImage for handling images
from utils.canvas_button import CanvasButton  # Import custom button class for canvas buttons

# Define the ProfilePageView class, inheriting from PageView
class ProfilePageView(PageView):
    def __init__(self, parent):
        # Initialize the parent class with specified dimensions and background color
        super().__init__(parent, height=712.5, width=892.5, bg="#F5F5F5", bd=0, highlightthickness=0, relief="ridge")
        
        # Set the path for images used in the profile page
        self.image_path = self.image_path / "profile/images/"
        
        # Create a canvas for the layout of the Profile page
        self.canvas = tk.Canvas(self, height=712.5, width=892.5, bg="#F5F5F5", bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack(fill="both", expand=True)  # Pack the canvas to fill the parent container
        
        self.current_content_controller = None  # Placeholder for content controller

        # Load the first image to display on the canvas
        self.image_image_1 = PhotoImage(file=self.image_path / "image_1.png")
        self.image_1 = self.canvas.create_image(185, 45, image=self.image_image_1)

        # Duplicate image loading (likely intended to be different images)
        self.image_image_ = PhotoImage(file=self.image_path / "image_1.png")
        self.image_1 = self.canvas.create_image(185, 45, image=self.image_image_1)

    def render(self):
        # Create buttons to navigate to different pages
        button_1 = CanvasButton(self.canvas, 335, 120, self.image_path / "image_2.png",
                                lambda: self.controller.root.page_controller.switch_page("personal_information"), self.image_path / "image_4.png")
        button_2 = CanvasButton(self.canvas, 335, 200, self.image_path / "image_3.png",
                                lambda: self.controller.root.page_controller.switch_page("notification_setting"), self.image_path / "image_5.png")
        
        # Set this view as the current frame in the parent
        self.parent.set_frame(self)

    def update(self):
        # Placeholder for update logic (currently does nothing)
        pass