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

        self.image_image_2 = PhotoImage(file=self.image_path / "image_2(2).png")
        self.image_2 = self.canvas.create_image(446.5, 216.5, image=self.image_image_2)

        self.image_image_3 = PhotoImage(file=self.image_path / "image_3.png")
        self.image_3 = self.canvas.create_image(444.5, 504.5, image=self.image_image_3)

        # create button
        CanvasButton(self.canvas,  330.25, 615.75, self.image_path / "image_4.png", lambda: self.controller.root.page_controller.switch_page("my_flight"))
        CanvasButton(self.canvas,  731.5, 615.75, self.image_path / "image_5.png", lambda: self.controller.root.page_controller.switch_page("my_baggage"))
        CanvasButton(self.canvas,  722.5, 279.5, self.image_path / "image_6.png", lambda: self.controller.root.page_controller.switch_page("dashboard"))

        self.parent.set_frame(self)
    
    def update(self):
        pass


'''
import tkinter as tk
from PIL import Image, ImageTk

class ImagePlayer:
    def __init__(self, root, images, delay=2000):
        self.root = root
        self.images = [ImageTk.PhotoImage(Image.open(img)) for img in images]
        self.label = tk.Label(root)
        self.label.pack()
        self.index = 0
        self.delay = delay
        self.show_image()

    def show_image(self):
        self.label.config(image=self.images[self.index])
        self.index = (self.index + 1) % len(self.images)
        self.root.after(self.delay, self.show_image)

root = tk.Tk()
images = ["path_to_image1.jpg", "path_to_image2.jpg"]
player = ImagePlayer(root, images)
root.mainloop()
'''