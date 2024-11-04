import tkinter as tk
from pages.page_view import PageView

class ProfilePageView(PageView):
    def __init__(self, parent):
        super().__init__(parent, height = 1015, width = 1190, bg="#F5F5F5", bd=0, highlightthickness=0, relief="ridge")
        self.image_path = self.image_path / "main_page/images/"
        
        self.canvas = tk.Canvas(self, height = 1015, width = 1190, bg="#F5F5F5", bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack(fill="both", expand=True)
    
    def render(self):
        self.canvas.create_text(69, 32, anchor="nw", text="Profile", fill="#282828", font=("Roboto Black", 48 * -1))
        self.pack(fill="both",expand=True)
    
    def update(self):
        pass