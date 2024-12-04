import tkinter as tk
from utils.page_view import PageView

class MapPageView(PageView):
    def __init__(self, parent):
        # Initialize the MapPageView with specified dimensions and background color
        super().__init__(parent, height = 712.5, width = 892.5, bg="#F5F5F5", bd=0, highlightthickness=0, relief="ridge")
        
        # Set the path to images for the map page
        self.image_path = self.image_path / "main_page/images/"
        
        # Create a canvas to hold elements of the map page
        self.canvas = tk.Canvas(self, height = 712.5, width = 892.5, bg="#F5F5F5", bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack(fill="both", expand=True)
    
    def render(self):
        # Create a text label for the map title
        self.canvas.create_text(69, 32, anchor="nw", text="Map", fill="#282828", font=("Roboto Black", 36 * -1))
        # Set the current frame in the parent container to this view
        self.parent.set_frame(self)
    
    def update(self):
        pass