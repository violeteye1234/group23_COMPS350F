import tkinter as tk
from utils.page_view import PageView
from tkinter import PhotoImage
from models.sharedata import SharedData

class BoardingInformationPageView(PageView):
    def __init__(self, parent):
        # Initialize the BoardingInformationPageView with specified dimensions and background color
        super().__init__(parent, height = 829, width = 892.5, bg="#F5F5F5", bd=0, highlightthickness=0, relief="ridge")
        # Set the path to the images for the boarding information page
        self.image_path = self.image_path / "boarding_information/images/"
        
        # Create a canvas to hold the images and labels
        self.canvas = tk.Canvas(self, height = 829, width = 892.5, bg="#F5F5F5", bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack(fill="both", expand=True)

        # Access user data from the shared data model
        self.user_data = SharedData.user_data
        #self.data = self.controller.data
        
        # Extract flight and seat details from the user data
        self.flightnumber = self.user_data['flights'][0]['flightnumber']
        self.status = self.user_data['flights'][0]['status']
        self.gate = self.user_data['flights'][0]['gate']
        self.departuretime = self.user_data['flights'][0]['departuretime']
        self.departureairport = self.user_data['flights'][0]['departureairport']
        self.arrivalairport = self.user_data['flights'][0]['arrivalairport']
        self.seat = self.user_data['flightseats'][0]['seatnumber']
    
    def render(self):
        # Load and display images on the canvas
        self.image_image_1 = PhotoImage(file=self.image_path / "image_1.png")
        self.image_1 = self.canvas.create_image(201.75, 45.0, image=self.image_image_1)

        self.image_image_2 = PhotoImage(file=self.image_path / "image_2.png")
        self.image_2 = self.canvas.create_image(599.25, 45.75, image=self.image_image_2)

        self.image_image_3 = PhotoImage(file=self.image_path / "image_3.png")
        self.image_3 = self.canvas.create_image(444.75, 269.25, image=self.image_image_3)



        # Create labels to display flight information
        self.flightnumber_label = tk.Label(self, text= self.flightnumber, font=('Helvetica', 12, 'bold'), bg="#D9D9D9")
        self.flightnumber_label.place(x=132.5, y=135.5)

        self.flightstatus_label = tk.Label(self, text= self.status, font=('Helvetica', 12, 'bold'), bg="#D9D9D9")
        self.flightstatus_label.place(x=234.25, y=135.5)

        self.departureairport_label = tk.Label(self, text= self.departureairport, font=('Helvetica', 12, 'bold'), bg="#D9D9D9")
        self.departureairport_label.place(x=450.25, y=120.5)

        self.arrivalairport_label = tk.Label(self, text= self.arrivalairport, font=('Helvetica', 12, 'bold'), bg="#D9D9D9")
        self.arrivalairport_label.place(x=636.25, y=120.5)

        self.gate_label = tk.Label(self, text= self.gate, font=('Helvetica', 12, 'bold'), bg="#D9D9D9")
        self.gate_label.place(x=263.25, y=184.5)

        self.departuretime_label = tk.Label(self, text= self.departuretime, font=('Helvetica', 12, 'bold'), bg="#D9D9D9")
        self.departuretime_label.place(x=215.25, y=213.5)

        self.seat_label = tk.Label(self, text= self.seat, font=('Helvetica', 12, 'bold'), bg="#D9D9D9")
        self.seat_label.place(x=263.25, y=241.5)

        # Set the current frame in the parent container to this view
        self.parent.set_frame(self)
    
    def update(self):
        pass