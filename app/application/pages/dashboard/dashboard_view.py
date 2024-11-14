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
        self.image_2 = self.canvas.create_image(446.5, 216.5, image=self.image_image_2)

        self.image_image_3 = PhotoImage(file=self.image_path / "image_3.png")
        self.image_3 = self.canvas.create_image(201.5, 379.5, image=self.image_image_3)

        self.image_image_4 = PhotoImage(file=self.image_path / "image_4.png")
        self.image_4 = self.canvas.create_image(244.5, 531.5, image=self.image_image_4)

        self.image_image_5 = PhotoImage(file=self.image_path / "image_5.png")
        self.image_5 = self.canvas.create_image(645.75, 531.5, image=self.image_image_5)

        CanvasButton(self.canvas,  731.5, 615.75, self.image_path / "image_6.png", lambda: self.controller.root.page_controller.switch_page("my_baggage"))
        CanvasButton(self.canvas,  330.25, 615.75, self.image_path / "image_7.png", lambda: self.controller.root.page_controller.switch_page("my_flight"))
        CanvasButton(self.canvas,  722.5, 279.5, self.image_path / "image_8.png", lambda: self.controller.root.page_controller.switch_page("dashboard"))# 不知道干什么
        
        self.parent.set_frame(self)
    
    def update(self):
        pass