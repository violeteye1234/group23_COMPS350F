#import tkinter as tk
#from utils.page_view import PageView
import tkinter as tk
from tkinter import PhotoImage
from utils.page_view import PageView
from utils.canvas_button import CanvasButton
from PIL import Image, ImageTk  # 导入Pillow库
from models.sharedata import SharedData

class FlightDetailPageView(PageView):
    def __init__(self, parent):
        super().__init__(parent, height = 712.5, width = 892.5, bg="#F5F5F5", bd=0, highlightthickness=0, relief="ridge")
        self.image_path = self.image_path / "flight_detail/image/"
        
        self.canvas = tk.Canvas(self, height = 712.5, width = 892.5, bg="#F5F5F5", bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack(fill="both", expand=True)
    
        self.user_data = SharedData.user_data
        self.flightnumber = self.user_data['flights'][0]['flightnumber']
        self.departuretime = self.user_data['flights'][0]['departuretime']
        self.landingtime = self.user_data['flights'][0]['arrivaltime']#.date()       
        self.departureairport = self.user_data['flights'][0]['departureairport']
        self.arrivalairport = self.user_data['flights'][0]['arrivalairport']
        self.seat = self.user_data['flightseats'][0]['seatnumber']
        self.departuretime_date = self.user_data['flights'][0]['departuretime'].date()
        self.landingtime_date = self.user_data['flights'][0]['arrivaltime'].date()

    def render(self):
        #self.canvas.create_text(69, 32, anchor="nw", text="Flight Detail", fill="#282828", font=("Roboto Black", 36 * -1))
        self.image_image_1 = PhotoImage(file=self.image_path / "image_1.png")
        self.image_1 = self.canvas.create_image(150, 40, image=self.image_image_1)
  
        self.image_image_2 = PhotoImage(file=self.image_path / "image_21.png")
        self.image_2 = self.canvas.create_image(150, 300, image=self.image_image_2)        
       
        CanvasButton(self.canvas, 250, 600, self.image_path / "image_3.png", lambda: self.controller.root.page_controller.switch_page("my_baggage"))        

        
        self.flightnumber_label = tk.Label(self, text= self.flightnumber, font=('Helvetica', 35, 'bold'), bg="#D9D9D9", fg="blue")
        self.flightnumber_label.place(x=350, y= 10)
        
        self.departuretime_date = tk.Label(self, text= self.departuretime_date, font=('Helvetica', 14, 'bold'), bg="#D9D9D9")
        self.departuretime_date.place(x=120, y=140)

        self.landingtime_date_label0 = tk.Label(self, text= self.landingtime_date, font=('Helvetica', 14, 'bold'), bg="#D9D9D9")
        self.landingtime_date_label0.place(x=250, y=140)
        
        self.flightnumber_label = tk.Label(self, text= self.flightnumber, font=('Helvetica', 14, 'bold'), bg="#D9D9D9", )
        self.flightnumber_label.place(x=250, y= 165) 

        self.flightnumber_label = tk.Label(self, text= self.flightnumber, font=('Helvetica', 14, 'bold'), bg="#D9D9D9", )
        self.flightnumber_label.place(x=250, y= 200) 

        self.departureairport_label = tk.Label(self, text= self.departureairport, font=('Helvetica', 14, 'bold'), bg="#D9D9D9")
        self.departureairport_label.place(x=250, y=230)

        self.departuretime_label = tk.Label(self, text= self.departuretime, font=('Helvetica', 14, 'bold'), bg="#D9D9D9" )
        self.departuretime_label.place(x=250, y=260)

        self.arrivalairport_label = tk.Label(self, text= self.arrivalairport, font=('Helvetica', 14, 'bold'), bg="#D9D9D9")
        self.arrivalairport_label.place(x=250, y=290)

        self.landingtime_label = tk.Label(self, text= self.landingtime, font=('Helvetica', 14, 'bold'), bg="#D9D9D9")
        self.landingtime_label.place(x=250, y=320)

        self.seat_label = tk.Label(self, text= self.seat, font=('Helvetica', 14, 'bold'), bg="#D9D9D9")
        self.seat_label.place(x=250, y=430)










        self.parent.set_frame(self)
        
    def update(self):
        pass