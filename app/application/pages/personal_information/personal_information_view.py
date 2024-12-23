import tkinter as tk
from utils.page_view import PageView
from tkinter import PhotoImage
from utils.canvas_button import CanvasButton
from models.sharedata import SharedData

class PersonalInformationPageView(PageView):
    def __init__(self, parent):
        super().__init__(parent, height=712.5, width=892.5, bg="#F5F5F5", bd=0, highlightthickness=0, relief="ridge")
        self.image_path = self.image_path / "personal_information/images/"

        # Create a canvas to hold images and entry fields
        self.canvas = tk.Canvas(self, height=712.5, width=892.5, bg="#F5F5F5", bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack(fill="both", expand=True)

        # Current content controller (not yet set)
        self.current_content_controller = None

        # Load and display images on the canvas
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

        # Store default user data in a list
        self.default_data = [fullname, email, phone_number]
    
        
    def render(self):
        # Create a button to switch to the profile page
        button_1 = CanvasButton(self.canvas, 400, 400, self.image_path / "image_3.png",
                                lambda: self.controller.root.page_controller.switch_page("profile"))
        
        # Create entry fields for user data
        self.entries = []
        # Positions for entry fields
        positions = [(580, 193), (643, 232), (649, 269)]

        for i, data in enumerate(self.default_data):
            entry = tk.Entry(self.canvas) # Create an entry widget
            entry.insert(0, data) # Insert default data into the entry
            entry_window = self.canvas.create_window(positions[i][0], positions[i][1], window=entry) # Place entry on the canvas
            self.entries.append(entry) # Store entry in the list
        
        # Set the current frame in the parent container to this view
        self.parent.set_frame(self)
    

    def update(self):
        pass