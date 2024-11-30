import tkinter as tk  # Import tkinter for GUI components
from tkinter import PhotoImage  # Import PhotoImage for handling images
from utils.page_view import PageView  # Import base class for page views
from utils.canvas_button import CanvasButton  # Import custom button class for canvas
from PIL import Image  # Import Image from Pillow for image handling
# from utils.scrollable_frame import ScrollableFrame  # Commented out import for a scrollable frame

# Define the NotificationCenterPageView class, inheriting from PageView
class NotificationCenterPageView(PageView):
    def __init__(self, parent):
        # Initialize the parent class with specified dimensions and background color
        super().__init__(parent, height=712.5, width=892.5, bg="#F5F5F5", bd=0, highlightthickness=0, relief="ridge")
        
        # Set the path for images used in the Notification Center
        self.image_path = self.image_path / "notification_center/images/"
        
        # Create a canvas for the layout of the Notification Center page
        self.canvas = tk.Canvas(self, bg="#F5F5F5", height=712.5, width=892.5, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack(fill="both", expand=True)  # Pack the canvas to fill the parent container

    def render(self):
        # Load and display the first image on the canvas
        self.image_image_1 = PhotoImage(file=self.image_path / "image_1.png")
        self.image_1 = self.canvas.create_image(150, 40, image=self.image_image_1)

        # Resize and save the second image
        original_image_path2 = self.image_path / "image_2.png"
        desired_size2 = (800, 100)  # Desired image size
        original_image2 = Image.open(original_image_path2)
        resized_image2 = original_image2.resize(desired_size2)
        resized_image2.save(original_image_path2)  # Overwrite the original image

        # Resize and save the third image
        original_image_path3 = self.image_path / "image_3.png"
        desired_size3 = (800, 100)  # Desired image size
        original_image3 = Image.open(original_image_path3)
        resized_image3 = original_image3.resize(desired_size3)
        resized_image3.save(original_image_path3)  # Overwrite the original image

        # Create notification messages based on flight times
        MYBAGGAGE_check = f"Your Baggage is checking at {self.controller.one_hour_ago}. Please go through security as soon as possible."
        MYBAGGAGE_arrive = f"Your Baggage arrived at {self.controller.a_quarter_later}. Please pick it up as soon as possible."
        MYFLIGHT_boarding = f"Your Flight is boarding at {self.controller.half_hour_ago}. Please board the plane as soon as possible."

        # Determine the notification state based on flight times
        if self.controller.time_until_takeoff > 60 or self.controller.time_until_takeoff < 0 or self.controller.time_later_landing < 0:
            i = 0  # No important notifications
        elif 30 < self.controller.time_until_takeoff <= 60:
            i = 1  # Notification for baggage check
        elif 0 < self.controller.time_until_takeoff <= 30:
            i = 2  # Notifications for baggage check and flight boarding
        elif self.controller.time_later_landing >= 15:
            i = 3  # Notifications for baggage check, flight boarding, and baggage arrival

        # Display messages based on the notification state
        if i == 0:
            label = tk.Label(self.canvas, text="No messages", font=("Arial", 16), bg="#F5F5F5")
            label.place(x=420, y=120)  # Center message
        elif i == 1:
            button1 = CanvasButton(self.canvas, 420, 120, self.image_path / "image_3.png",
                                   lambda: self.controller.root.page_controller.switch_page("my_baggage"),
                                   self.image_path / "image_2.png", text=MYBAGGAGE_check, font_size=16)
        elif i == 2:
            button1 = CanvasButton(self.canvas, 420, 220, self.image_path / "image_3.png",
                                   lambda: self.controller.root.page_controller.switch_page("my_baggage"),
                                   self.image_path / "image_2.png", text=MYBAGGAGE_check, font_size=16)

            button2 = CanvasButton(self.canvas, 420, 120, self.image_path / "image_3.png",
                                   lambda: self.controller.root.page_controller.switch_page("my_flight"),
                                   self.image_path / "image_2.png", text=MYFLIGHT_boarding, font_size=16)
        elif i == 3:
            button1 = CanvasButton(self.canvas, 420, 320, self.image_path / "image_3.png",
                                   lambda: self.controller.root.page_controller.switch_page("my_baggage"),
                                   self.image_path / "image_2.png", text=MYBAGGAGE_check, font_size=16)

            button2 = CanvasButton(self.canvas, 420, 220, self.image_path / "image_3.png",
                                   lambda: self.controller.root.page_controller.switch_page("my_flight"),
                                   self.image_path / "image_2.png", text=MYFLIGHT_boarding, font_size=16)

            button3 = CanvasButton(self.canvas, 420, 120, self.image_path / "image_3.png",
                                   lambda: self.controller.root.page_controller.switch_page("my_baggage"),
                                   self.image_path / "image_2.png", text=MYBAGGAGE_arrive, font_size=16)

        # Set this view as the current frame in the parent
        self.parent.set_frame(self)

    def update(self):
        # Placeholder for update logic (currently does nothing)
        pass