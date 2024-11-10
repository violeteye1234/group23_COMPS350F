import tkinter as tk
from tkinter import PhotoImage
from utils.page_view import PageView
from utils.canvas_button import CanvasButton
from PIL import Image

class NotificationCenterPageView(PageView):
    def __init__(self, parent):
        super().__init__(parent, height=712.5, width=892.5, bg="#F5F5F5", bd=0, highlightthickness=0, relief="ridge")
        self.image_path = self.image_path / "notification_center/images/"
        self.canvas = tk.Canvas(self, bg="#F5F5F5", height=712.5, width=892.5, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack(fill="both", expand=True)
        self.current_content_controller = None
        

        self.image_image_1 = PhotoImage(file=self.image_path / "image_1.png")
        self.image_1 = self.canvas.create_image(150, 40, image=self.image_image_1)

        original_image_path2 = self.image_path / "image_2.png"
        desired_size2 = (800, 100)  # 期望的图片大小
        original_image2 = Image.open(original_image_path2)
        resized_image2 = original_image2.resize(desired_size2)

        original_image_path3 = self.image_path / "image_3.png"
        desired_size3 = (800, 100)  # 期望的图片大小
        original_image3 = Image.open(original_image_path3)
        resized_image3 = original_image3.resize(desired_size3)

        # 覆盖原始图片
        resized_image2.save(original_image_path2)
        resized_image3.save(original_image_path3)

    def render(self):
        button_1 = CanvasButton(self.canvas, 420, 120, self.image_path / "image_3.png",
                                lambda: self.controller.go_to_my_baggage(),self.image_path / "image_2.png")
        button_2 = CanvasButton(self.canvas, 420, 220, self.image_path / "image_3.png",
                                lambda: self.controller.go_to_my_baggage(),self.image_path / "image_2.png")
        self.parent.set_frame(self)

    def update(self):
        pass