import tkinter as tk
from utils.page_view import PageView

class MyBaggagePageView(PageView):
    def __init__(self, parent):
        super().__init__(parent, height = 712.5, width = 892.5, bg="#F5F5F5", bd=0, highlightthickness=0, relief="ridge")
        self.image_path = self.image_path / "main_page/images/"
        
        self.canvas = tk.Canvas(self, height = 712.5, width = 892.5, bg="#F5F5F5", bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack(fill="both", expand=True)
    
    def render(self):
        self.canvas.create_text(69, 32, anchor="nw", text="My Baggage", fill="#282828", font=("Roboto Black", 36 * -1))
        self.parent.set_frame(self)
    
    def update(self):
        pass