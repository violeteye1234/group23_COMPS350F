import tkinter as tk
from utils.page_view import PageView
from utils import CanvasButton, ScrollableFrame
from tkinter import PhotoImage

class MainPageView(PageView):
    def __init__(self, parent):
        super().__init__(parent, height = 768, width = 768, bg="#F5F5F5", bd=0, highlightthickness=0, relief="ridge")
        self.image_path = self.image_path / "main_page/images/"
        
        self.canvas = tk.Canvas(self, height = 768, width = 768, bg="#F5F5F5", bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack(fill="both", expand=True)
    
    def render(self):
        self.image_image_1 = PhotoImage(file=self.image_path / "image_1.png")
        self.image_1 = self.canvas.create_image(540.0, 27.0, image=self.image_image_1)

        self.image_image_2 = PhotoImage(file=self.image_path / "image_2.png")
        self.image_2 = self.canvas.create_image(93.0, 435.5, image=self.image_image_2)
        
        self.canvas.create_text(443.0, 12.75, anchor="nw", text="12:57", fill="#EBEBEB", font=("Roboto Black", 36 * -1))

        button_3 = CanvasButton(self.canvas,  95.25, 27.0, self.image_path / "image_3.png",     lambda: self.controller.switch_page("dashboard"))
        button_4 = CanvasButton(self.canvas,  1021.0, 27.0, self.image_path / "image_4.png",    lambda: self.controller.switch_page("profile"))
        button_5 = CanvasButton(self.canvas,  964.0, 27.25, self.image_path / "image_5.png",    lambda: self.controller.switch_page("help"))
        button_6 = CanvasButton(self.canvas,  900.0, 27.25, self.image_path / "image_6.png",    lambda: self.controller.switch_page("about"))
        button_7 = CanvasButton(self.canvas,  93.5, 90.0, self.image_path / "image_7.png",      lambda: self.controller.switch_page("dashboard"))
        button_8 = CanvasButton(self.canvas,  93.5, 195.0, self.image_path / "image_8.png",     lambda: self.controller.switch_page("boarding_information"))
        button_9 = CanvasButton(self.canvas,  93.5, 247.5, self.image_path / "image_9.png",     lambda: self.controller.switch_page("my_flight"))
        button_10 = CanvasButton(self.canvas,  93.5, 300.0, self.image_path / "image_10.png",   lambda: self.controller.switch_page("my_baggage"))
        button_11 = CanvasButton(self.canvas,  93.5, 352.5, self.image_path / "image_11.png",   lambda: self.controller.logout())
        button_12 = CanvasButton(self.canvas,  93.5, 142.5, self.image_path / "image_12.png",   lambda: self.controller.switch_page("notification_center"))

        self.content_frame = ScrollableFrame(self.canvas, width=892.5, height=712.5, bg="#FFF0F0")
        self.content_frame.pack_propagate(False)
        self.canvas.create_window(187.5, 55.5, window=self.content_frame, anchor='nw')


    def update(self):
        pass