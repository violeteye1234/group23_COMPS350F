import tkinter as tk
from ..page_view import PageView
from utils.canvas_button import CanvasButton # type: ignore
from tkinter import PhotoImage

class MainPageView(PageView):
    def __init__(self, parent):
        super().__init__(parent, height = 1024, width = 1440, bg="#F5F5F5", bd=0, highlightthickness=0, relief="ridge")
        self.image_path = self.image_path / "main_page/images/"
        
        self.canvas = tk.Canvas(self, height = 1024, width = 1440, bg="#F5F5F5", bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack(fill="both", expand=True)
    
    def render(self):
        self.image_image_1 = PhotoImage(file=self.image_path / "image_1.png")
        image_1 = self.canvas.create_image(720.0, 36.0, image=self.image_image_1)

        button_2 = CanvasButton(self.canvas,  128.0, 37.0, self.image_path / "image_2.png", lambda: self.controller.switch_page("dashboard"))

        self.canvas.create_text(527.5, 17.0, anchor="nw", text="12:57", fill="#EBEBEB", font=("Roboto Black", 48 * -1))

        button_3 = CanvasButton(self.canvas,  1348.0, 37.0, self.image_path / "image_3.png", lambda: self.controller.switch_page("profile"))
        button_4 = CanvasButton(self.canvas,  1257.0, 37.0, self.image_path / "image_4.png", lambda: self.controller.switch_page("help"))
        button_5 = CanvasButton(self.canvas,  1159.0, 37.0, self.image_path / "image_5.png", lambda: self.controller.switch_page("about"))

        self.image_image_6 = PhotoImage(file=self.image_path / "image_6.png")
        image_6 = self.canvas.create_image(125.0, 548.0, image=self.image_image_6)

        button_7 = CanvasButton(self.canvas,  125.0, 121.0, self.image_path / "image_7.png", lambda: self.controller.switch_page("dashboard"))
        button_8 = CanvasButton(self.canvas,  125.0, 261.0, self.image_path / "image_8.png", lambda: self.controller.switch_page("boarding_information"))
        button_9 = CanvasButton(self.canvas,  125.0, 331.0, self.image_path / "image_9.png", lambda: self.controller.switch_page("my_flight"))
        button_10 = CanvasButton(self.canvas,  125.0, 401.0, self.image_path / "image_10.png", lambda: self.controller.switch_page("my_baggage"))
        button_12 = CanvasButton(self.canvas,  125.0, 471.0, self.image_path / "image_12.png", lambda: self.controller.logout())
        button_13 = CanvasButton(self.canvas,  125.0, 191.0, self.image_path / "image_13.png", lambda: self.controller.switch_page("notification_center"))
        

        self.content_frame = tk.Frame(self.canvas, width=1190, height=1015, bg="#FFF0F0")
        self.content_frame.pack_propagate(False)
        self.canvas.create_window(250, 75, window=self.content_frame, anchor='nw')

        # self.content_canvas = tk.Canvas(self.content_frame, height = 1190, width = 1015, bg="#F5F5F5", bd=0, highlightthickness=0, relief="ridge")
        # self.content_canvas.pack(fill="both", expand=True)
        # 
        # self.content_frame.create_text(212.5, 17.0, anchor="nw", text="12:57", fill="#EBEBEB", font=("Roboto Black", 48 * -1))
        

    def update(self):
        pass