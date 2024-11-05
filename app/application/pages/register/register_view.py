import tkinter as tk
from utils.page_view import PageView

class RegisterPageView(PageView):
    def __init__(self, parent):
        super().__init__(parent, height = 768, width = 1080, bg="#F5F5F5", bd=0, highlightthickness=0, relief="ridge")
        self.image_path = self.image_path / "main_page/images/"
        
        self.canvas = tk.Canvas(self, height = 768, width = 1080, bg="#F5F5F5", bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack(fill="both", expand=True)
    
    def render(self):
        self.canvas.create_text(69, 32, anchor="nw", text="Register", fill="#282828", font=("Roboto Black", 36 * -1))
        self.pack(fill="both",expand=True)
        
    def update(self):
        pass