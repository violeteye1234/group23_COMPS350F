import tkinter as tk  # Import tkinter for GUI components
from utils.page_view import PageView  # Import base class for page views

# Define the MapPageView class, inheriting from PageView
class MapPageView(PageView):
    def __init__(self, parent):
        # Initialize the parent class with specified dimensions and background color
        super().__init__(parent, height=712.5, width=892.5, bg="#F5F5F5", bd=0, highlightthickness=0, relief="ridge")
        
        # Set the path for images used in the map page
        self.image_path = self.image_path / "main_page/images/"
        
        # Create a canvas for the layout of the map page
        self.canvas = tk.Canvas(self, height=712.5, width=892.5, bg="#F5F5F5", bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack(fill="both", expand=True)  # Pack the canvas to fill the parent container
    
    def render(self):
        # Create a text label on the canvas to display "Map"
        self.canvas.create_text(69, 32, anchor="nw", text="Map", fill="#282828", font=("Roboto Black", 36 * -1))
        self.parent.set_frame(self)  # Set this view as the current frame in the parent
    
    def update(self):
        # Placeholder for update logic (currently does nothing)
        pass