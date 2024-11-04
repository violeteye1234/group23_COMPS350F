import tkinter as tk
from pages.page_view import PageView

class BoardingInformationPageView(PageView):
    def __init__(self, parent):
        super().__init__(parent, height = 1024, width = 1440, bg="#F5F5F5", bd=0, highlightthickness=0, relief="ridge")
        self.image_path = self.image_path / "main_page/images/"
        
        self.canvas = tk.Canvas(self, height = 1024, width = 1440, bg="#F5F5F5", bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack(fill="both", expand=True)
    
    def render(self):
        self.canvas.create_text(69, 32, anchor="nw", text="Boarding Information", fill="#282828", font=("Roboto Black", 48 * -1))
        self.pack(fill="both",expand=True)
    
    def update(self):
        pass