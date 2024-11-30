import tkinter as tk  # Import tkinter for GUI components
from utils.page_view import PageView  # Import base class for page views
from tkinter import PhotoImage  # Import PhotoImage for handling images in tkinter
from utils.canvas_button import CanvasButton  # Import custom button class for canvas
from models.sharedata import SharedData  # Import shared data model for accessing user data

# Define the DashboardPageView class, inheriting from PageView
class DashboardPageView(PageView):
    def __init__(self, parent):
        # Initialize the parent class with specified dimensions and background color
        super().__init__(parent, height=712.5, width=892.5, bg="#F5F5F5", bd=0, highlightthickness=0, relief="ridge")
        
        # Set the path for images used in the dashboard
        self.image_path = self.image_path / "dashboard/images/"
        
        # Create a canvas for the dashboard layout
        self.canvas = tk.Canvas(self, height=712.5, width=892.5, bg="#F5F5F5", bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack(fill="both", expand=True)  # Pack the canvas to fill the parent container

        # Retrieve user data from the shared data model
        self.user_data = SharedData.user_data
        
        # Extract flight and baggage details from user data
        self.flightnumber = self.user_data['flights'][0]['flightnumber']
        self.status = self.user_data['flights'][0]['status']
        self.gate = self.user_data['flights'][0]['gate']
        self.departuretime = self.user_data['flights'][0]['departuretime']
        self.baggagenumber = self.user_data['baggages'][0]['baggagenumber']
        self.baggagestatus = self.user_data['baggages'][0]['status']

    def render(self):
        # Load and display images on the canvas
        self.image_image_1 = PhotoImage(file=self.image_path / "image_1.png")
        self.image_1 = self.canvas.create_image(138.5, 52.5, image=self.image_image_1)

        self.image_image_2 = PhotoImage(file=self.image_path / "image_2(2).png")
        self.image_2 = self.canvas.create_image(446.5, 216.5, image=self.image_image_2)

        self.image_image_3 = PhotoImage(file=self.image_path / "image_3.png")
        self.image_3 = self.canvas.create_image(444.5, 504.5, image=self.image_image_3)

        # Create buttons for navigation to different pages
        CanvasButton(self.canvas, 330.25, 615.75, self.image_path / "image_4.png", lambda: self.controller.root.page_controller.switch_page("my_flight"))
        CanvasButton(self.canvas, 731.5, 615.75, self.image_path / "image_5.png", lambda: self.controller.root.page_controller.switch_page("my_baggage"))
        CanvasButton(self.canvas, 722.5, 279.5, self.image_path / "image_6.png", lambda: self.controller.root.page_controller.switch_page("dashboard"))

        # Create labels to display flight information
        self.flightnumber_label = tk.Label(self, text=self.flightnumber, font=('Helvetica', 12, 'bold'), bg="#D9D9D9")
        self.flightnumber_label.place(x=250, y=430)
        
        self.flightstatus_label = tk.Label(self, text=self.status, font=('Helvetica', 12, 'bold'), bg="#D9D9D9")
        self.flightstatus_label.place(x=300, y=480)

        self.flightgate_label = tk.Label(self, text=self.gate, font=('Helvetica', 12, 'bold'), bg="#D9D9D9")
        self.flightgate_label.place(x=340, y=512)

        self.departure_time_label = tk.Label(self, text=self.departuretime, font=('Helvetica', 12, 'bold'), bg="#D9D9D9")
        self.departure_time_label.place(x=245, y=540)

        self.baggagenumber_label = tk.Label(self, text=self.baggagenumber, font=('Helvetica', 12, 'bold'), bg="#D9D9D9")
        self.baggagenumber_label.place(x=715, y=430)

        self.baggagestatus_label = tk.Label(self, text=self.baggagestatus, font=('Helvetica', 12, 'bold'), bg="#D9D9D9")
        self.baggagestatus_label.place(x=700, y=480)
        
        self.baggageflynum_label = tk.Label(self, text=self.flightnumber, font=('Helvetica', 12, 'bold'), bg="#D9D9D9")
        self.baggageflynum_label.place(x=715, y=512)

        # Set the current frame to the parent container
        self.parent.set_frame(self)

        # Ensure parent is correctly set before calling set_frame (commented out error handling)
        '''
        if hasattr(self.parent, 'set_frame'):
            self.parent.set_frame(self)
        else:
            print("Error: Parent does not have set_frame method")
        '''

    def update(self):
        # Placeholder for update logic (currently does nothing)
        pass