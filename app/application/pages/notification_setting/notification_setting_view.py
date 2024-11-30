import tkinter as tk  # Import tkinter for GUI components
from utils.page_view import PageView  # Import base class for page views
from tkinter import PhotoImage  # Import PhotoImage for handling images
from utils.canvas_button import CanvasButton  # Import custom button class for canvas buttons
from PIL import Image  # Import Image from Pillow for image handling

# Define the NotificationSettingPageView class, inheriting from PageView
class NotificationSettingPageView(PageView):
    def __init__(self, parent):
        # Initialize the parent class with specified dimensions and background color
        super().__init__(parent, height=1023, width=892.5, bg="#F5F5F5", bd=0, highlightthickness=0, relief="ridge")
        
        # Set the path for images used in the notification settings
        self.image_path = self.image_path / "notification_setting/images/"
        
        # Create a canvas for the layout of the Notification Setting page
        self.canvas = tk.Canvas(self, height=1023, width=892.5, bg="#F5F5F5", bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack(fill="both", expand=True)  # Pack the canvas to fill the parent container
        
        # Load button images
        self.button_images = [
            tk.PhotoImage(file=self.image_path / "image_14.png"),
            tk.PhotoImage(file=self.image_path / "image_13.png")
        ]
        
        # Initialize image index for toggle buttons
        self.current_image_index_button1 = 0
        self.current_image_index_button2 = 0
        self.current_image_index_button3 = 0
        self.current_image_index_button4 = 0
        self.current_image_index_button5 = 0
        self.current_image_index_button6 = 0
        self.current_image_index_button7 = 0
        self.current_image_index_button8 = 0
        self.current_image_index_button9 = 0

        # Create buttons with toggle functionality
        self.button1 = tk.Button(self.canvas, image=self.button_images[self.current_image_index_button1], bd=0, highlightthickness=0, relief="flat", command=self.toggle_image_button1)
        self.button1.place(x=750, y=130)
        
        self.button2 = tk.Button(self.canvas, image=self.button_images[self.current_image_index_button2], bd=0, highlightthickness=0, relief="flat", command=self.toggle_image_button2)
        self.button2.place(x=750, y=220)
        
        self.button3 = tk.Button(self.canvas, image=self.button_images[self.current_image_index_button3], bd=0, highlightthickness=0, relief="flat", command=self.toggle_image_button3)
        self.button3.place(x=750, y=310)
        
        self.button4 = tk.Button(self.canvas, image=self.button_images[self.current_image_index_button4], bd=0, highlightthickness=0, relief="flat", command=self.toggle_image_button4)
        self.button4.place(x=750, y=400)
        
        self.button5 = tk.Button(self.canvas, image=self.button_images[self.current_image_index_button5], bd=0, highlightthickness=0, relief="flat", command=self.toggle_image_button5)
        self.button5.place(x=750, y=490)
        
        self.button6 = tk.Button(self.canvas, image=self.button_images[self.current_image_index_button6], bd=0, highlightthickness=0, relief="flat", command=self.toggle_image_button6)
        self.button6.place(x=750, y=610)
        
        self.button7 = tk.Button(self.canvas, image=self.button_images[self.current_image_index_button7], bd=0, highlightthickness=0, relief="flat", command=self.toggle_image_button7)
        self.button7.place(x=750, y=700)
        
        self.button8 = tk.Button(self.canvas, image=self.button_images[self.current_image_index_button8], bd=0, highlightthickness=0, relief="flat", command=self.toggle_image_button8)
        self.button8.place(x=750, y=790)
        
        self.button9 = tk.Button(self.canvas, image=self.button_images[self.current_image_index_button9], bd=0, highlightthickness=0, relief="flat", command=self.toggle_image_button9)
        self.button9.place(x=750, y=880)

        # Load and display images on the canvas
        self.image_image_1 = PhotoImage(file=self.image_path / "image_1.png")
        self.image_1 = self.canvas.create_image(240, 45, image=self.image_image_1)

        self.image_image_2 = PhotoImage(file=self.image_path / "image_9.png")
        self.image_2 = self.canvas.create_image(420, 90, image=self.image_image_2)

        # Resize and save images for consistent display
        original_image_path2 = self.image_path / "image_2.png"
        desired_size2 = (850, 81)  # Desired image size
        original_image2 = Image.open(original_image_path2)
        resized_image2 = original_image2.resize(desired_size2)
        resized_image2.save(original_image_path2)  # Overwrite the original image
        
        self.image_image_3 = PhotoImage(file=self.image_path / "image_2.png")
        self.image_3 = self.canvas.create_image(440, 150, image=self.image_image_3)

        # Repeat the image resizing and saving process for additional images
        original_image_path3 = self.image_path / "image_3.png"
        desired_size3 = (850, 81)
        original_image3 = Image.open(original_image_path3)
        resized_image3 = original_image3.resize(desired_size3)
        resized_image3.save(original_image_path3)

        self.image_image_4 = PhotoImage(file=self.image_path / "image_3.png")
        self.image_4 = self.canvas.create_image(440, 240, image=self.image_image_4)

        # Continue for other images...
        original_image_path4 = self.image_path / "image_4.png"
        desired_size4 = (850, 81)
        original_image4 = Image.open(original_image_path4)
        resized_image4 = original_image4.resize(desired_size4)
        resized_image4.save(original_image_path4)

        self.image_image_5 = PhotoImage(file=self.image_path / "image_4.png")
        self.image_5 = self.canvas.create_image(440, 330, image=self.image_image_5)

        # Follow the same pattern for images 6 to 12
        # ...

    # Define toggle functions for button images
    def toggle_image_button1(self):
        self.current_image_index_button1 = (self.current_image_index_button1 + 1) % len(self.button_images)  # Cycle through button images
        self.button1.config(image=self.button_images[self.current_image_index_button1])

    def toggle_image_button2(self):
        self.current_image_index_button2 = (self.current_image_index_button2 + 1) % len(self.button_images)
        self.button2.config(image=self.button_images[self.current_image_index_button2])

    def toggle_image_button3(self):
        self.current_image_index_button3 = (self.current_image_index_button3 + 1) % len(self.button_images)
        self.button3.config(image=self.button_images[self.current_image_index_button3])

    def toggle_image_button4(self):
        self.current_image_index_button4 = (self.current_image_index_button4 + 1) % len(self.button_images)
        self.button4.config(image=self.button_images[self.current_image_index_button4])

    def toggle_image_button5(self):
        self.current_image_index_button5 = (self.current_image_index_button5 + 1) % len(self.button_images)
        self.button5.config(image=self.button_images[self.current_image_index_button5])

    def toggle_image_button6(self):
        self.current_image_index_button6 = (self.current_image_index_button6 + 1) % len(self.button_images)
        self.button6.config(image=self.button_images[self.current_image_index_button6])

    def toggle_image_button7(self):
        self.current_image_index_button7 = (self.current_image_index_button7 + 1) % len(self.button_images)
        self.button7.config(image=self.button_images[self.current_image_index_button7])

    def toggle_image_button8(self):
        self.current_image_index_button8 = (self.current_image_index_button8 + 1) % len(self.button_images)
        self.button8.config(image=self.button_images[self.current_image_index_button8])

    def toggle_image_button9(self):
        self.current_image_index_button9 = (self.current_image_index_button9 + 1) % len(self.button_images)
        self.button9.config(image=self.button_images[self.current_image_index_button9])

    def render(self):

        self.parent.set_frame(self)  # Set this view as the current frame in the parent

    def update(self):
        # Placeholder for update logic (currently does nothing)
        pass