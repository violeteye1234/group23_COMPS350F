import tkinter as tk
from tkinter import PhotoImage
from utils.page_view import PageView
from utils.canvas_button import CanvasButton

class MyBaggagePageView(PageView):
    def __init__(self, parent):
        super().__init__(parent, height = 712.5, width = 892.5, bg="#F5F5F5", bd=0, highlightthickness=0, relief="ridge")
        self.image_path = self.image_path / "my_baggage/image/"

        self.canvas = tk.Canvas(self, height = 712.5, width = 892.5, bg="#F5F5F5", bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack(fill="both", expand=True)
    
    def render(self):
        self.image_image_1 = PhotoImage(file=self.image_path / "image_1.png")
        self.image_1 = self.canvas.create_image(150, 40, image=self.image_image_1)

        #self.image_image_2 = PhotoImage(file=self.image_path / "image_2.png")
        #self.image_2 = self.canvas.create_image(599.25, 45.75, image=self.image_image_2)

        self.image_image_3 = PhotoImage(file=self.image_path / "image_3.png")
        self.image_3 = self.canvas.create_image(200, 250, image=self.image_image_3)

        self.image_image_4 = PhotoImage(file=self.image_path / "image_4.png")
        self.image_4 = self.canvas.create_image(600, 250, image=self.image_image_4)

        CanvasButton(self.canvas, 185, 320, self.image_path / "image_5.png", lambda: self.controller.root.page_controller.switch_page("baggage_detail"))
        CanvasButton(self.canvas, 600, 320, self.image_path / "image_6.png", lambda: self.controller.root.page_controller.switch_page("baggage_detail"))






        self.parent.set_frame(self)

    def update(self):
        pass