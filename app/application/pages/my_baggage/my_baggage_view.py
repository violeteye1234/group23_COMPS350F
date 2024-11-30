import tkinter as tk  # Import tkinter for GUI components
from tkinter import PhotoImage  # Import PhotoImage for handling images
from utils.page_view import PageView  # Import base class for page views
from utils.canvas_button import CanvasButton  # Import custom button class for canvas
from PIL import Image  # Import Image from PIL for image handling (not used in the current code)
from models.sharedata import SharedData  # Import SharedData model for accessing shared user data

# Define the MyBaggagePageView class, inheriting from PageView
class MyBaggagePageView(PageView):
    def __init__(self, parent):
        # Initialize the parent class with specified dimensions and background color
        super().__init__(parent, height=712.5, width=892.5, bg="#F5F5F5", bd=0, highlightthickness=0, relief="ridge")
        
        # Set the path for images used in the My Baggage page
        self.image_path = self.image_path / "my_baggage/image/"

        # Create a canvas for the layout of the My Baggage page
        self.canvas = tk.Canvas(self, height=712.5, width=892.5, bg="#F5F5F5", bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack(fill="both", expand=True)  # Pack the canvas to fill the parent container

        # Retrieve shared user data
        self.user_data = SharedData.user_data

        # Extract baggage information from user data
        self.baggagenumber = self.user_data['baggages'][0]['baggagenumber']
        self.baggagestatus = self.user_data['baggages'][0]['status']
        self.baggageflightnumber = self.user_data['flights'][0]['flightnumber']
        self.baggagecurrentlocation = self.user_data['flights'][0]['departureairport']
    
    def render(self):
        # Load and display images on the canvas at specified positions
        self.image_image_1 = PhotoImage(file=self.image_path / "image_1.png")
        self.image_1 = self.canvas.create_image(150, 40, image=self.image_image_1)

        self.image_image_3 = PhotoImage(file=self.image_path / "image_3.png")
        self.image_3 = self.canvas.create_image(200, 250, image=self.image_image_3)

        self.image_image_4 = PhotoImage(file=self.image_path / "image_4.png")
        self.image_4 = self.canvas.create_image(600, 250, image=self.image_image_4)

        # Create buttons for navigating to baggage details
        CanvasButton(self.canvas, 185, 320, self.image_path / "image_5.png", lambda: self.controller.root.page_controller.switch_page("baggage_detail"))
        CanvasButton(self.canvas, 600, 320, self.image_path / "image_6.png", lambda: self.controller.root.page_controller.switch_page("baggage_detail"))

        # Create labels to display baggage information
        self.baggagenumber_label = tk.Label(self, text=self.baggagenumber, font=('Helvetica', 12, 'bold'), bg="#D9D9D9")
        self.baggagenumber_label.place(x=150, y=150)

        self.baggagestatus_label = tk.Label(self, text=self.baggagestatus, font=('Helvetica', 12, 'bold'), bg="#D9D9D9")
        self.baggagestatus_label.place(x=100, y=195)
        
        self.baggageflightnumber_label = tk.Label(self, text=self.baggageflightnumber, font=('Helvetica', 12, 'bold'), bg="#D9D9D9")
        self.baggageflightnumber_label.place(x=120, y=228)

        self.baggagecurrentlocation_label = tk.Label(self, text=self.baggagecurrentlocation, font=('Helvetica', 12, 'bold'), bg="#D9D9D9")
        self.baggagecurrentlocation_label.place(x=170, y=260)

        # Set this view as the current frame in the parent
        self.parent.set_frame(self)

    def update(self):
        # Placeholder for update logic (currently does nothing)
        pass