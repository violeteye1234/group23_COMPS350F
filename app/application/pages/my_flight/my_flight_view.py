import tkinter as tk
from tkinter import PhotoImage
from utils.page_view import PageView
from utils.canvas_button import CanvasButton
from models.sharedata import SharedData
from PIL import Image, ImageTk  # 导入Pillow库
import re

class MyFlightPageView(PageView):
    def __init__(self, parent):
        # Initialize the MyFlightPageView with specified dimensions and background color
        super().__init__(parent, height = 712.5, width = 892.5, bg="#F5F5F5", bd=0, highlightthickness=0, relief="ridge")
        
        # Set the path to images for the flight page
        self.image_path = self.image_path / "my_flight/image/"
        
        # Create a canvas to hold images and labels
        self.canvas = tk.Canvas(self, height = 712.5, width = 892.5, bg="#F5F5F5", bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack(fill="both", expand=True)
    
        # Retrieve user data from shared data model
        self.user_data = SharedData.user_data

        # Extract information for the first flight
        self.flightnumber0 = self.user_data['flights'][0]['flightnumber']
        self.departuretime0 = self.user_data['flights'][0]['departuretime']#.date()
        self.landingtime0 = self.user_data['flights'][0]['arrivaltime']#.date()
        self.departureairport0 = self.user_data['flights'][0]['departureairport']
        self.arrivalairport0 = self.user_data['flights'][0]['arrivalairport']
        self.seat0 = self.user_data['flightseats'][0]['seatnumber']


        if len(self.user_data['flights']) > 1:  # Make sure there are at least two elements
            flight_number = self.user_data['flights'][1]['flightnumber']
            if flight_number is not None or flight_number != "":
           
                self.flightnumber1= self.user_data['flights'][1]['flightnumber']
                self.departuretime1 = self.user_data['flights'][1]['departuretime']#.date()
                self.landingtime1 = self.user_data['flights'][1]['arrivaltime']#.date()
                self.departureairport1 = self.user_data['flights'][1]['departureairport']
                self.arrivalairport1 = self.user_data['flights'][1]['arrivalairport']
                self.seat1 = self.user_data['flightseats'][1]['seatnumber']
            else:
                self.flightnumber1= 0
                self.departuretime1 = 0
                self.landingtime1 = 0
                self.departureairport1 = 0
                self.arrivalairport1 = 0
                self.seat1 = 0
        else:
                self.flightnumber1= 0
                self.departuretime1 = 0
                self.landingtime1 = 0
                self.departureairport1 = 0
                self.arrivalairport1 = 0
                self.seat1 = 0          


          
        if len(self.user_data['flights']) > 1:  # Make sure there are at least two elements
            flight_number = self.user_data['flights'][2]['flightnumber']
            if flight_number is not None or flight_number != "":
                self.flightnumber2 = self.user_data['flights'][2]['flightnumber']
                self.departuretime2 = self.user_data['flights'][2]['departuretime']#.date()
                self.landingtime2 = self.user_data['flights'][2]['arrivaltime']#.date()
                self.departureairport2 = self.user_data['flights'][2]['departureairport']
                self.arrivalairport2 = self.user_data['flights'][2]['arrivalairport']
                self.seat2 = self.user_data['flightseats'][2]['seatnumber']
            else:
                self.flightnumber2 = 0
                self.departuretime2 = 0
                self.landingtime2 = 0
                self.departureairport2 = 0
                self.arrivalairport2 = 0
                self.seat2 = 0
        else:
                self.flightnumber2 = 0
                self.departuretime2 = 0
                self.landingtime2 = 0
                self.departureairport2 = 0
                self.arrivalairport2 = 0
                self.seat2 = 0

  #      self.flightnumber1= self.user_data['flights'][1]['flightnumber']
  #     self.departuretime1 = self.user_data['flights'][1]['departuretime']#.date()
  #      self.landingtime1 = self.user_data['flights'][1]['arrivaltime']#.date()
  #      self.departureairport1 = self.user_data['flights'][1]['departureairport']
  #      self.arrivalairport1 = self.user_data['flights'][1]['arrivalairport']
  #      self.seat1 = self.user_data['flightseats'][1]['seatnumber']#
#
#        self.flightnumber2 = self.user_data['flights'][2]['flightnumber']
#       self.departuretime2 = self.user_data['flights'][2]['departuretime']#.date()
 #       self.landingtime2 = self.user_data['flights'][2]['arrivaltime']#.date()
  #      self.departureairport2 = self.user_data['flights'][2]['departureairport']
   ##     self.seat2 = self.user_data['flightseats'][2]['seatnumber']
    def render(self):

        #self.canvas.create_text(69, 32, anchor="nw", text="My Flight", fill="#282828", font=("Roboto Black", 36 * -1))
        #self.parent.set_frame(self)

        # Load and display images on the canvas at specified coordinates
        
        self.image_image_1 = PhotoImage(file=self.image_path / "image_11.png")
        self.image_1 = self.canvas.create_image(150, 40, image=self.image_image_1)

        self.image_image_2 = PhotoImage(file=self.image_path / "image_66.png")
        self.image_2 = self.canvas.create_image(350, 200, image=self.image_image_2)
    
        self.image_image_3 = PhotoImage(file=self.image_path / "image_66.png")
        self.image_3 = self.canvas.create_image(350, 400, image=self.image_image_3)
    
        self.image_image_4 = PhotoImage(file=self.image_path / "image_66.png")
        self.image_4 = self.canvas.create_image(350, 600, image=self.image_image_4)
        
#text
#0
        self.flightnumber_label0 = tk.Label(self, text= self.flightnumber0, font=('Helvetica', 12, 'bold'), bg="#D9D9D9")
        self.flightnumber_label0.place(x=120, y= 160)


        self.departureairport0_label0 = tk.Label(self, text= self.departureairport0, font=('Helvetica', 17, 'bold'), bg="#D9D9D9")
        self.departureairport0_label0.place(x=90, y=200)

        self.arrivalairport_label0 = tk.Label(self, text= self.arrivalairport0, font=('Helvetica', 17, 'bold'), bg="#D9D9D9")
        self.arrivalairport_label0.place(x=450, y=200)

    
        self.departuretime_label0 = tk.Label(self, text= self.departuretime0, font=('Helvetica', 14, 'bold'), bg="#D9D9D9", fg="blue")
        self.departuretime_label0.place(x=90, y=240)

        self.landingtime_label0 = tk.Label(self, text= self.landingtime0, font=('Helvetica', 14, 'bold'), bg="#D9D9D9",  fg="blue")
        self.landingtime_label0.place(x=450, y=240)
#1      
        if len(self.user_data['flights']) > 1:  # Make sure there are at least two elements
            flight_number = self.user_data['flights'][1]['flightnumber']
            if flight_number is not None or flight_number != "":
                self.flightnumber_label1 = tk.Label(self, text= self.flightnumber1, font=('Helvetica', 12, 'bold'), bg="#D9D9D9")
                self.flightnumber_label1.place(x=120, y= 360)


                self.departureairport_label1 = tk.Label(self, text= self.departureairport1, font=('Helvetica', 17, 'bold'), bg="#D9D9D9")
                self.departureairport_label1.place(x=90, y=400)

                self.arrivalairport_label = tk.Label(self, text= self.arrivalairport1, font=('Helvetica', 17, 'bold'), bg="#D9D9D9")
                self.arrivalairport_label.place(x=450, y=400)

    
                self.departuretime_label = tk.Label(self, text= self.departuretime1, font=('Helvetica', 14, 'bold'), bg="#D9D9D9", fg="blue")
                self.departuretime_label.place(x=90, y=440)

                self.landingtime_label1 = tk.Label(self, text= self.landingtime1, font=('Helvetica', 14, 'bold'), bg="#D9D9D9",  fg="blue")
                self.landingtime_label1.place(x=450, y=440)
#2
        if len(self.user_data['flights']) > 1:  # Make sure there are at least two elements
            flight_number = self.user_data['flights'][1]['flightnumber']
            if flight_number is not None or flight_number != "":
                self.flightnumber_label2 = tk.Label(self, text= self.flightnumber2, font=('Helvetica', 12, 'bold'), bg="#D9D9D9")
                self.flightnumber_label2.place(x=120, y= 560)


                self.departureairport_label2 = tk.Label(self, text= self.departureairport2, font=('Helvetica', 17, 'bold'), bg="#D9D9D9")
                self.departureairport_label2.place(x=90, y=600)

                self.arrivalairport_label2 = tk.Label(self, text= self.arrivalairport2, font=('Helvetica', 17, 'bold'), bg="#D9D9D9")
                self.arrivalairport_label2.place(x=450, y=600)

    
                self.departuretime_label2 = tk.Label(self, text= self.departuretime2, font=('Helvetica', 14, 'bold'), bg="#D9D9D9", fg="blue")
                self.departuretime_label2.place(x=90, y=640)

                self.landingtime_label2 = tk.Label(self, text= self.landingtime2, font=('Helvetica', 14, 'bold'), bg="#D9D9D9",  fg="blue")
                self.landingtime_label2.place(x=450, y=640)


        # Create buttons for navigating to flight details
        CanvasButton(self.canvas, 600, 200, self.image_path / "image_55.png", lambda: self.controller.root.page_controller.switch_page("flight_detail"))        
        CanvasButton(self.canvas, 600, 400, self.image_path / "image_55.png", lambda: self.controller.root.page_controller.switch_page("flight_detail"))         
        CanvasButton(self.canvas, 600, 600, self.image_path / "image_55.png", lambda: self.controller.root.page_controller.switch_page("flight_detail"))         
        
       # Flight_time = f" { self.takeoff_time,   self.landing_time } 


        # Set the current frame in the parent container to this view
        self.parent.set_frame(self)
    

    def update(self):
        pass