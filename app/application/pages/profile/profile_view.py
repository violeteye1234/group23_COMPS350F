import tkinter as tk
from utils.page_view import PageView
from tkinter import PhotoImage
from utils.canvas_button import CanvasButton

class ProfilePageView(PageView):
    def __init__(self, parent):
        super().__init__(parent, height = 712.5, width = 892.5, bg="#F5F5F5", bd=0, highlightthickness=0, relief="ridge")
        self.image_path = self.image_path / "profile/images/"
        self.canvas = tk.Canvas(self, height = 712.5, width = 892.5, bg="#F5F5F5", bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack(fill="both", expand=True)
        self.current_content_controller = None

        self.image_image_1 = PhotoImage(file=self.image_path / "image_1.png")
        self.image_1 = self.canvas.create_image(185, 45, image=self.image_image_1)

        
    
    def render(self):
        button_1 = CanvasButton(self.canvas, 335, 120, self.image_path / "image_2.png",
                                lambda: self.controller.root.page_controller.switch_page("personal_information"),self.image_path / "image_4.png")
        button_2 = CanvasButton(self.canvas, 335, 200, self.image_path / "image_3.png",
                                lambda: self.controller.root.page_controller.switch_page("notification_setting"),self.image_path / "image_5.png")
        self.parent.set_frame(self)

    
    def update(self):
        pass