import tkinter as tk
from utils.page_view import PageView
from tkinter import PhotoImage
from utils.canvas_button import CanvasButton

class DashboardPageView(PageView):
    def __init__(self, parent):
        super().__init__(parent, height = 712.5, width = 892.5, bg="#F5F5F5", bd=0, highlightthickness=0, relief="ridge")
        self.image_path = self.image_path / "dashboard/images/"
        
        self.canvas = tk.Canvas(self, height = 712.5, width = 892.5, bg="#F5F5F5", bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack(fill="both", expand=True)
    
    def render(self):
        self.image_image_1 = PhotoImage(file=self.image_path / "image_1.png")
        self.image_1 = self.canvas.create_image(138.5, 52.5, image=self.image_image_1)

        self.image_image_2 = PhotoImage(file=self.image_path / "image_2.png")
        self.image_2 = self.canvas.create_image(450.5, 216.5, image=self.image_image_2)

        self.image_image_3 = PhotoImage(file=self.image_path / "image_3.png")
        self.image_3 = self.canvas.create_image(362.0, 446.0, image=self.image_image_3)

        self.image_image_4 = PhotoImage(file=self.image_path / "image_4.png")
        self.image_4 = self.canvas.create_image(435.0, 598.0, image=self.image_image_4)

        self.image_image_5 = PhotoImage(file=self.image_path / "image_5.png")
        self.image_5 = self.canvas.create_image(521.0, 684.0, image=self.image_image_5)

        self.image_image_6 = PhotoImage(file=self.image_path / "image_6.png")
        self.image_6 = self.canvas.create_image(836.25, 598.0, image=self.image_image_6)

        self.image_image_7 = PhotoImage(file=self.image_path / "image_7.png")
        self.image_7 = self.canvas.create_image(922.0, 684.0, image=self.image_image_7)

        self.image_image_8 = PhotoImage(file=self.image_path / "image_8.png")
        self.image_8 = self.canvas.create_image(922.0, 345.0, image=self.image_image_8)

        self.parent.set_frame(self)
    
    def update(self):
        pass