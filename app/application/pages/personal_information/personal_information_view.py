import tkinter as tk
from utils.page_view import PageView
from tkinter import PhotoImage
from utils.canvas_button import CanvasButton

class PersonalInformationPageView(PageView):
    def __init__(self, parent):
        super().__init__(parent, height = 712.5, width = 892.5, bg="#F5F5F5", bd=0, highlightthickness=0, relief="ridge")
        self.image_path = self.image_path / "personal_information/images/"
        self.canvas = tk.Canvas(self, height = 712.5, width = 892.5, bg="#F5F5F5", bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack(fill="both", expand=True)
        self.current_content_controller = None

        self.image_image_1 = PhotoImage(file=self.image_path / "image_1.png")
        self.image_1 = self.canvas.create_image(185, 45, image=self.image_image_1)

        self.image_image_2 = PhotoImage(file=self.image_path / "image_2.png")
        self.image_2 = self.canvas.create_image(450, 230, image=self.image_image_2)

        self.image_image_5 = PhotoImage(file=self.image_path / "image_5.png")
        self.image_5 = self.canvas.create_image(185, 230, image=self.image_image_5)

    def render(self):
        button_1 = CanvasButton(self.canvas, 250, 400, self.image_path / "image_3.png",
                                lambda: self.controller.root.page_controller.switch_page(""))
        button_2 = CanvasButton(self.canvas, 600, 400, self.image_path / "image_4.png",
                                lambda: self.controller.root.page_controller.switch_page(""))
        self.parent.set_frame(self)
    
    def update(self):
        pass