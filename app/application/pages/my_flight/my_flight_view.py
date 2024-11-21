import tkinter as tk
from tkinter import PhotoImage
from utils.page_view import PageView
from utils.canvas_button import CanvasButton
from PIL import Image, ImageTk  # 导入Pillow库

class MyFlightPageView(PageView):
    def __init__(self, parent):
        super().__init__(parent, height = 712.5, width = 892.5, bg="#F5F5F5", bd=0, highlightthickness=0, relief="ridge")
        self.image_path = self.image_path / "my_flight/image/"
        
        self.canvas = tk.Canvas(self, height = 712.5, width = 892.5, bg="#F5F5F5", bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack(fill="both", expand=True)
    
    def render(self):

        #self.canvas.create_text(69, 32, anchor="nw", text="My Flight", fill="#282828", font=("Roboto Black", 36 * -1))
        #self.parent.set_frame(self)
        
        self.image_image_1 = PhotoImage(file=self.image_path / "image_11.png")
        self.image_1 = self.canvas.create_image(150, 40, image=self.image_image_1)

        self.image_image_2 = PhotoImage(file=self.image_path / "image_66.png")
        self.image_2 = self.canvas.create_image(350, 200, image=self.image_image_2)
    #123@abc.com
        self.image_image_3 = PhotoImage(file=self.image_path / "image_66.png")
        self.image_3 = self.canvas.create_image(350, 400, image=self.image_image_3)
    
        self.image_image_4 = PhotoImage(file=self.image_path / "image_66.png")
        self.image_4 = self.canvas.create_image(350, 600, image=self.image_image_4)
        
        CanvasButton(self.canvas, 600, 200, self.image_path / "image_55.png", lambda: self.controller.root.page_controller.switch_page("flight_detail"))        
        CanvasButton(self.canvas, 600, 400, self.image_path / "image_55.png", lambda: self.controller.root.page_controller.switch_page("flight_detail"))         
        CanvasButton(self.canvas, 600, 600, self.image_path / "image_55.png", lambda: self.controller.root.page_controller.switch_page("flight_detail"))         
        self.parent.set_frame(self)
    

    def update(self):
        pass