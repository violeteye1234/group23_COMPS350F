import tkinter as tk
from tkinter import PhotoImage
from utils.page_view import PageView
from utils.canvas_button import CanvasButton
from PIL import Image
from models.sharedata import SharedData

class BaggageDetailPageView(PageView):
    def __init__(self, parent):
        # Initialize the BaggageDetailPageView with specified dimensions and background color
        super().__init__(parent, height=712.5, width=892.5, bg="#F5F5F5", bd=0, highlightthickness=0, relief="ridge")
        self.image_path = self.image_path / "baggage_detail/image/" # Set the path for baggage detail images

        # Create a canvas to hold images and labels
        self.canvas = tk.Canvas(self, bg="#F5F5F5", height=712.5, width=892.5, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack(fill="both", expand=True) # Pack the canvas to fill the parent frame

        # Access shared user data
        self.user_data = SharedData.user_data

        # Extract baggage and flight details from user data
        self.baggagenumber = self.user_data['baggages'][0]['baggagenumber']
        self.baggagestatus = self.user_data['baggages'][0]['status']
        self.baggageflightnumber = self.user_data['flights'][0]['flightnumber']
        self.baggagedepartureairport = self.user_data['flights'][0]['departureairport']
        self.baggagearrivalairport = self.user_data['flights'][0]['arrivalairport']
        self.baggageweight = self.user_data['baggages'][0]['baggageweight']
        self.baggageID = self.user_data['baggages'][0]['baggageid']
        self.baggagepersonnalname = self.user_data['users']['fullname']



    def render(self):
        # Load and display images and labels on the canvas
        
        # Load and place the first image
        self.image_image_1 = PhotoImage(file=self.image_path / "image_1.png")
        self.image_1 = self.canvas.create_image(130, 40, image=self.image_image_1)

        # Load and place the third image (second image is commented out)
        self.image_image_3 = PhotoImage(file=self.image_path / "image_3.png")
        self.image_3 = self.canvas.create_image(420, 420, image=self.image_image_3)

        # Create and place labels for baggage details
        self.baggagenumber_label = tk.Label(self, text= self.baggagenumber, font=('Helvetica', 12, 'bold'), bg="#D9D9D9")
        self.baggagenumber_label.place(x=160, y=95)

        self.baggagepersonnalname_label = tk.Label(self, text= self.baggagepersonnalname, font=('Helvetica', 12, 'bold'), bg="#D9D9D9")
        self.baggagepersonnalname_label.place(x=200, y=160)
        
        self.baggageflightnumber_label = tk.Label(self, text= self.baggageflightnumber, font=('Helvetica', 12, 'bold'), bg="#D9D9D9")
        self.baggageflightnumber_label.place(x=160, y=205)

        self.baggageweight_label = tk.Label(self, text= self.baggageweight, font=('Helvetica', 12, 'bold'), bg="#D9D9D9")
        self.baggageweight_label.place(x=110, y=245)

        self.baggageID_label = tk.Label(self, text= self.baggageID, font=('Helvetica', 12, 'bold'), bg="#D9D9D9")
        self.baggageID_label.place(x=195, y=287)

        self.baggagedepartureairport_label = tk.Label(self, text= self.baggagedepartureairport, font=('Helvetica', 12, 'bold'), bg="#D9D9D9")
        self.baggagedepartureairport_label.place(x=120, y=375)
        
        self.baggagearrivalairport_label = tk.Label(self, text= self.baggagearrivalairport, font=('Helvetica', 12, 'bold'), bg="#D9D9D9")
        self.baggagearrivalairport_label.place(x=145, y=420)
        
        self.baggagestatus_label = tk.Label(self, text= self.baggagestatus, font=('Helvetica', 12, 'bold'), bg="#D9D9D9")
        self.baggagestatus_label.place(x=90, y=540)

        # Set this frame as the current frame in the parent container
        self.parent.set_frame(self)

    def update(self):
        # Placeholder method for future updates to the view
        pass