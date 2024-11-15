import tkinter as tk
from utils.page_view import PageView
from tkinter import PhotoImage
from utils.canvas_button import CanvasButton

class BoardingInformationPageView(PageView):
    def __init__(self, parent):
        super().__init__(parent, height = 800.5, width = 892.5, bg="#F5F5F5", bd=0, highlightthickness=0, relief="ridge")
        self.image_path = self.image_path / "boarding_information/images/"
        
        self.canvas = tk.Canvas(self, height = 800.5, width = 892.5, bg="#F5F5F5", bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack(fill="both", expand=True)
    
    def render(self):
        self.image_image_1 = PhotoImage(file=self.image_path / "image_1.png")
        self.image_1 = self.canvas.create_image(201.75, 45.0, image=self.image_image_1)

        self.image_image_2 = PhotoImage(file=self.image_path / "image_2.png")
        self.image_2 = self.canvas.create_image(599.25, 45.75, image=self.image_image_2)

        self.image_image_3 = PhotoImage(file=self.image_path / "image_3.png")
        self.image_3 = self.canvas.create_image(444.75, 269.25, image=self.image_image_3)

        self.image_image_4 = PhotoImage(file=self.image_path / "image_4.png")
        self.image_4 = self.canvas.create_image(444.75, 579.25, image=self.image_image_4)

        self.image_image_5 = PhotoImage(file=self.image_path / "image_5.png")
        self.image_5 = self.canvas.create_image(444.75, 752.25, image=self.image_image_5)

        CanvasButton(self.canvas, 178.75, 666.75, self.image_path / "image_6.png", lambda: self.controller.root.page_controller.switch_page("boarding_information"))
        CanvasButton(self.canvas, 178.75, 374.25, self.image_path / "image_7.png", lambda: self.controller.root.page_controller.switch_page("boarding_information"))

        self.parent.set_frame(self)
    
    def update(self):
        pass