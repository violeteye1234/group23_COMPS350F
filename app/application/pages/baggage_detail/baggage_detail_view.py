import tkinter as tk
from tkinter import PhotoImage
from utils.page_view import PageView
from utils.canvas_button import CanvasButton
from PIL import Image

class BaggageDetailPageView(PageView):
    def __init__(self, parent):
        super().__init__(parent, height=712.5, width=892.5, bg="#F5F5F5", bd=0, highlightthickness=0, relief="ridge")
        self.image_path = self.image_path / "baggage_detail/image/"

        self.canvas = tk.Canvas(self, bg="#F5F5F5", height=712.5, width=892.5, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack(fill="both", expand=True)

    def render(self):
        self.image_image_1 = PhotoImage(file=self.image_path / "image_1.png")
        self.image_1 = self.canvas.create_image(130, 40, image=self.image_image_1)
    
        #self.image_image_2 = PhotoImage(file=self.image_path / "image_2.png")
        #self.image_2 = self.canvas.create_image(599.25, 45.75, image=self.image_image_2)

        self.image_image_3 = PhotoImage(file=self.image_path / "image_3.png")
        self.image_3 = self.canvas.create_image(420, 420, image=self.image_image_3)
        self.parent.set_frame(self)




    def update(self):
        pass