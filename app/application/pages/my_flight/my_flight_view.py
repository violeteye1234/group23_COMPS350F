import tkinter as tk  # Import tkinter for GUI components
from tkinter import PhotoImage  # Import PhotoImage for handling images
from utils.page_view import PageView  # Import base class for page views
from utils.canvas_button import CanvasButton  # Import custom button class for canvas
from models.sharedata import SharedData  # Import SharedData model for accessing shared user data
from PIL import Image, ImageTk  # Import Image and ImageTk from Pillow for image handling
import re  # Import regex module (not used in the current code)

# Define the MyFlightPageView class, inheriting from PageView
class MyFlightPageView(PageView):
    def __init__(self, parent):
        # Initialize the parent class with specified dimensions and background color
        super().__init__(parent, height=712.5, width=892.5, bg="#F5F5F5", bd=0, highlightthickness=0, relief="ridge")
        
        # Set the path for images used in the My Flight page
        self.image_path = self.image_path / "my_flight/image/"
        
        # Create a canvas for the layout of the My Flight page
        self.canvas = tk.Canvas(self, height=712.5, width=892.5, bg="#F5F5F5", bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack(fill="both", expand=True)  # Pack the canvas to fill the parent container

        # Retrieve shared user data
        self.user_data = SharedData.user_data

        # Extract flight information from user data for the first flight
        self.flightnumber0 = self.user_data['flights'][0]['flightnumber']
        self.departuretime0 = self.user_data['flights'][0]['departuretime']
        self.landingtime0 = self.user_data['flights'][0]['arrivaltime']
        self.departureairport0 = self.user_data['flights'][0]['departureairport']
        self.arrivalairport0 = self.user_data['flights'][0]['arrivalairport']
        self.seat0 = self.user_data['flightseats'][0]['seatnumber']

        # Initialize variables for the second flight (if available)
        if len(self.user_data['flights']) > 1:  # Ensure there are at least two flights
            flight_number = self.user_data['flights'][1]['flightnumber']
            if flight_number is not None and flight_number != "":
                self.flightnumber1 = flight_number
                self.departuretime1 = self.user_data['flights'][1]['departuretime']
                self.landingtime1 = self.user_data['flights'][1]['arrivaltime']
                self.departureairport1 = self.user_data['flights'][1]['departureairport']
                self.arrivalairport1 = self.user_data['flights'][1]['arrivalairport']
                self.seat1 = self.user_data['flightseats'][1]['seatnumber']
            else:
                # Default values if flight number is not valid
                self.flightnumber1 = self.departuretime1 = self.landingtime1 = 0
                self.departureairport1 = self.arrivalairport1 = self.seat1 = 0
        else:
            # Default values if there is no second flight
            self.flightnumber1 = self.departuretime1 = self.landingtime1 = 0
            self.departureairport1 = self.arrivalairport1 = self.seat1 = 0

        # Initialize variables for the third flight (if available)
        if len(self.user_data['flights']) > 2:  # Ensure there are at least three flights
            flight_number = self.user_data['flights'][2]['flightnumber']
            if flight_number is not None and flight_number != "":
                self.flightnumber2 = flight_number
                self.departuretime2 = self.user_data['flights'][2]['departuretime']
                self.landingtime2 = self.user_data['flights'][2]['arrivaltime']
                self.departureairport2 = self.user_data['flights'][2]['departureairport']
                self.arrivalairport2 = self.user_data['flights'][2]['arrivalairport']
                self.seat2 = self.user_data['flightseats'][2]['seatnumber']
            else:
                # Default values if flight number is not valid
                self.flightnumber2 = self.departuretime2 = self.landingtime2 = 0
                self.departureairport2 = self.arrivalairport2 = self.seat2 = 0
        else:
            # Default values if there is no third flight
            self.flightnumber2 = self.departuretime2 = self.landingtime2 = 0
            self.departureairport2 = self.arrivalairport2 = self.seat2 = 0

    def render(self):
        # Load and display images on the canvas at specified positions
        self.image_image_1 = PhotoImage(file=self.image_path / "image_11.png")
        self.image_1 = self.canvas.create_image(150, 40, image=self.image_image_1)

        self.image_image_2 = PhotoImage(file=self.image_path / "image_66.png")
        self.image_2 = self.canvas.create_image(350, 200, image=self.image_image_2)
    
        self.image_image_3 = PhotoImage(file=self.image_path / "image_66.png")
        self.image_3 = self.canvas.create_image(350, 400, image=self.image_image_3)
    
        self.image_image_4 = PhotoImage(file=self.image_path / "image_66.png")
        self.image_4 = self.canvas.create_image(350, 600, image=self.image_image_4)
        
        # Create labels to display flight information for the first flight
        self.flightnumber_label0 = tk.Label(self, text=self.flightnumber0, font=('Helvetica', 12, 'bold'), bg="#D9D9D9")
        self.flightnumber_label0.place(x=120, y=160)

        self.departureairport0_label0 = tk.Label(self, text=self.departureairport0, font=('Helvetica', 17, 'bold'), bg="#D9D9D9")
        self.departureairport0_label0.place(x=90, y=200)

        self.arrivalairport_label0 = tk.Label(self, text=self.arrivalairport0, font=('Helvetica', 17, 'bold'), bg="#D9D9D9")
        self.arrivalairport_label0.place(x=450, y=200)

        self.departuretime_label0 = tk.Label(self, text=self.departuretime0, font=('Helvetica', 14, 'bold'), bg="#D9D9D9", fg="blue")
        self.departuretime_label0.place(x=90, y=240)

        self.landingtime_label0 = tk.Label(self, text=self.landingtime0, font=('Helvetica', 14, 'bold'), bg="#D9D9D9", fg="blue")
        self.landingtime_label0.place(x=450, y=240)

        # Create labels to display flight information for the second flight (if available)
        if len(self.user_data['flights']) > 1:  # Ensure there are at least two flights
            flight_number = self.user_data['flights'][1]['flightnumber']
            if flight_number is not None and flight_number != "":
                self.flightnumber_label1 = tk.Label(self, text=self.flightnumber1, font=('Helvetica', 12, 'bold'), bg="#D9D9D9")
                self.flightnumber_label1.place(x=120, y=360)

                self.departureairport_label1 = tk.Label(self, text=self.departureairport1, font=('Helvetica', 17, 'bold'), bg="#D9D9D9")
                self.departureairport_label1.place(x=90, y=400)

                self.arrivalairport_label1 = tk.Label(self, text=self.arrivalairport1, font=('Helvetica', 17, 'bold'), bg="#D9D9D9")
                self.arrivalairport_label1.place(x=450, y=400)

                self.departuretime_label1 = tk.Label(self, text=self.departuretime1, font=('Helvetica', 14, 'bold'), bg="#D9D9D9", fg="blue")
                self.departuretime_label1.place(x=90, y=440)

                self.landingtime_label1 = tk.Label(self, text=self.landingtime1, font=('Helvetica', 14, 'bold'), bg="#D9D9D9", fg="blue")
                self.landingtime_label1.place(x=450, y=440)

        # Create labels to display flight information for the third flight (if available)
        if len(self.user_data['flights']) > 2:  # Ensure there are at least three flights
            flight_number = self.user_data['flights'][2]['flightnumber']
            if flight_number is not None and flight_number != "":
                self.flightnumber_label2 = tk.Label(self, text=self.flightnumber2, font=('Helvetica', 12, 'bold'), bg="#D9D9D9")
                self.flightnumber_label2.place(x=120, y=560)

                self.departureairport_label2 = tk.Label(self, text=self.departureairport2, font=('Helvetica', 17, 'bold'), bg="#D9D9D9")
                self.departureairport_label2.place(x=90, y=600)

                self.arrivalairport_label2 = tk.Label(self, text=self.arrivalairport2, font=('Helvetica', 17, 'bold'), bg="#D9D9D9")
                self.arrivalairport_label2.place(x=450, y=600)

                self.departuretime_label2 = tk.Label(self, text=self.departuretime2, font=('Helvetica', 14, 'bold'), bg="#D9D9D9", fg="blue")
                self.departuretime_label2.place(x=90, y=640)

                self.landingtime_label2 = tk.Label(self, text=self.landingtime2, font=('Helvetica', 14, 'bold'), bg="#D9D9D9", fg="blue")
                self.landingtime_label2.place(x=450, y=640)

        # Create buttons for navigating to flight details
        CanvasButton(self.canvas, 600, 200, self.image_path / "image_55.png", lambda: self.controller.root.page_controller.switch_page("flight_detail"))        
        CanvasButton(self.canvas, 600, 400, self.image_path / "image_55.png", lambda: self.controller.root.page_controller.switch_page("flight_detail"))         
        CanvasButton(self.canvas, 600, 600, self.image_path / "image_55.png", lambda: self.controller.root.page_controller.switch_page("flight_detail"))         

        # Set this view as the current frame in the parent
        self.parent.set_frame(self)
    
    def update(self):
        # Placeholder for update logic (currently does nothing)
        pass