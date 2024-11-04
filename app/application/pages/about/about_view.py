import tkinter as tk
from pages.page_view import PageView
from tkinter import PhotoImage
from utils.canvas_button import CanvasButton # type: ignore

class AboutPageView(PageView):
    def __init__(self, parent):
        super().__init__(parent, height = 1024, width = 1440, bg="#F5F5F5", bd=0, highlightthickness=0, relief="ridge")
        self.image_path = self.image_path / "about/images/"
        
        self.canvas = tk.Canvas(self, height = 1024, width = 1440, bg="#F5F5F5", bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack(fill="both", expand=True)

    
    def render(self):
        button_1 = CanvasButton(self.canvas,  526.0, 100.0, self.image_path / "image_1.png", lambda: self.controller.log("pressed"))

        self.canvas.create_text(0.0, 246.0, anchor="nw", text="About Us", fill="#282828", font=("Roboto Black", 48 * -1))

        self.canvas.create_text(8.0, 336.0, anchor="nw", text="Welcome to Flight Status Notification System! We are a dedicated team of professionals committed to providing top-notch services and solutions to our valued passengers. Our mission is to enhance your travel experience through innovation, reliability, and exceptional customer service.", fill="#282828", font=("Roboto Regular", 24 * -1))

        self.canvas.create_text(0.0, 510.0, anchor="nw", text="Our Team", fill="#282828", font=("Roboto Black", 48 * -1))

        self.image_image_2 = PhotoImage(file=self.image_path / "image_2.png")
        self.image_2 = self.canvas.create_image(250.0, 530.0, image=self.image_image_2)

        button_3 = CanvasButton(self.canvas,  245.0, 725.0, self.image_path / "image_3.png", lambda: self.controller.log("pressed"))

        self.image_image_4 = PhotoImage(file=self.image_path / "image_4.png")
        self.image_4 = self.canvas.create_image(812.0, 989.0, image=self.image_image_4)

        self.image_image_5 = PhotoImage(file=self.image_path / "image_5.png")
        self.image_5 = self.canvas.create_image(812.0, 725.0, image=self.image_image_5)

        self.image_image_6 = PhotoImage(file=self.image_path / "image_6.png")
        self.image_6 = self.canvas.create_image(812.0, 1253.0, image=self.image_image_6)

        self.image_image_7 = PhotoImage(file=self.image_path / "image_7.png")
        self.image_7 = self.canvas.create_image(245.0, 989.0, image=self.image_image_7)

        self.image_image_8 = PhotoImage(file=self.image_path / "image_8.png")
        self.image_8 = self.canvas.create_image(812.0, 1517.0, image=self.image_image_8)

        self.image_image_9 = PhotoImage(file=self.image_path / "image_9.png")
        self.image_9 = self.canvas.create_image(245.0, 1253.0, image=self.image_image_9)

        self.image_image_10 = PhotoImage(file=self.image_path / "image_10.png")
        self.image_10 = self.canvas.create_image(245.0, 1781.0, image=self.image_image_10)

        self.image_image_11 = PhotoImage(file=self.image_path / "image_11.png")
        self.image_11 = self.canvas.create_image(245.0, 1517.0, image=self.image_image_11)

        self.canvas.create_text(0.0, 2001.0, anchor="nw", text="Committed to Excellence", fill="#282828", font=("Roboto Black", 48 * -1))

        self.canvas.create_text(0.0, 2080.0, anchor="nw", text="Our team combines expertise, passion, and dedication to ensure every aspect of your journey is seamless and enjoyable. From flight tracking to personalized assistance, we are here to support you every step of the way.", fill="#282828", font=("Roboto Regular", 24 * -1))

        self.pack(fill="both",expand=True)
    
    def update(self):
        pass