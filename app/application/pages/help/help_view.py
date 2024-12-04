import tkinter as tk
from utils.page_view import PageView
from tkinter import PhotoImage

class HelpPageView(PageView):
    def __init__(self, parent):
        # Initialize the HelpPageView with specified dimensions and background color
        super().__init__(parent, height = 1701, width = 892.5, bg="#F5F5F5", bd=0, highlightthickness=0, relief="ridge")
        
        # Set the path to images for the help view
        self.image_path = self.image_path / "help/images/"
        
        # Create a canvas to hold images
        self.canvas = tk.Canvas(self, height = 1701, width = 892.5, bg="#F5F5F5", bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack(fill="both", expand=True)
    
    def render(self):
        # Load and display images on the canvas at specified coordinates
        self.image_image_1 = PhotoImage(file=self.image_path / "image_1.png")
        self.image_1 = self.canvas.create_image(89.25, 45.5, image=self.image_image_1)

        self.image_image_2 = PhotoImage(file=self.image_path / "image_2.png")
        self.image_2 = self.canvas.create_image(599.25, 45.75, image=self.image_image_2)

        self.image_image_3 = PhotoImage(file=self.image_path / "image_3.png")
        self.image_3 = self.canvas.create_image(444.75, 243.0, image=self.image_image_3)

        self.image_image_4 = PhotoImage(file=self.image_path / "image_4.png")
        self.image_4 = self.canvas.create_image(444.75, 564.5, image=self.image_image_4)

        self.image_image_5 = PhotoImage(file=self.image_path / "image_5.png")
        self.image_5 = self.canvas.create_image(444.75, 1194.0, image=self.image_image_5)

        self.image_image_6 = PhotoImage(file=self.image_path / "image_6.png")
        self.image_6 = self.canvas.create_image(444.75, 1505.5, image=self.image_image_6)

        self.image_image_7 = PhotoImage(file=self.image_path / "image_7.png")
        self.image_7 = self.canvas.create_image(444.75, 884.75, image=self.image_image_7)
        
        # Set the current frame in the parent container to this view
        self.parent.set_frame(self)
    
    def update(self):
        pass