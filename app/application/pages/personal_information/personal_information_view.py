import tkinter as tk  # Import tkinter for GUI components
from utils.page_view import PageView  # Import base class for page views
from tkinter import PhotoImage  # Import PhotoImage for handling images
from utils.canvas_button import CanvasButton  # Import custom button class for canvas buttons
from models.sharedata import SharedData  # Import shared data model

# Define the PersonalInformationPageView class, inheriting from PageView
class PersonalInformationPageView(PageView):
    def __init__(self, parent):
        # Initialize the parent class with specified dimensions and background color
        super().__init__(parent, height=712.5, width=892.5, bg="#F5F5F5", bd=0, highlightthickness=0, relief="ridge")
        
        # Set the path for images used in the personal information page
        self.image_path = self.image_path / "personal_information/images/"
        
        # Create a canvas for the layout of the Personal Information page
        self.canvas = tk.Canvas(self, height=712.5, width=892.5, bg="#F5F5F5", bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack(fill="both", expand=True)  # Pack the canvas to fill the parent container
        
        self.current_content_controller = None  # Placeholder for content controller

        # Load images to display on the canvas
        self.image_image_1 = PhotoImage(file=self.image_path / "image_1.png")
        self.image_1 = self.canvas.create_image(185, 45, image=self.image_image_1)

        self.image_image_2 = PhotoImage(file=self.image_path / "image_2.png")
        self.image_2 = self.canvas.create_image(450, 230, image=self.image_image_2)

        self.image_image_5 = PhotoImage(file=self.image_path / "image_5.png")
        self.image_5 = self.canvas.create_image(185, 230, image=self.image_image_5)

        # Retrieve user data from shared data model
        self.user_data = SharedData.user_data
        fullname = self.user_data['users']['fullname']
        email = self.user_data['users']['email']
        phone_number = self.user_data['users']['phonenumber']
        self.default_data = [fullname, email, phone_number]  # Store user data in a list

    def render(self):
        # Create a button to navigate to the profile page
        button_1 = CanvasButton(self.canvas, 400, 400, self.image_path / "image_3.png",
                                lambda: self.controller.root.page_controller.switch_page("profile"))
        
        # List to hold entry widgets for user data
        self.entries = []
        positions = [(580, 193), (643, 232), (649, 269)]  # Define positions for entry widgets

        # Create entry widgets for user data and place them on the canvas
        for i, data in enumerate(self.default_data):
            entry = tk.Entry(self.canvas)  # Create an entry widget
            entry.insert(0, data)  # Insert default data into the entry
            entry_window = self.canvas.create_window(positions[i][0], positions[i][1], window=entry)  # Place entry on canvas
            self.entries.append(entry)  # Add entry to the list
        
        self.parent.set_frame(self)  # Set this view as the current frame in the parent

    def update(self):
        # Placeholder for update logic (currently does nothing)
        pass