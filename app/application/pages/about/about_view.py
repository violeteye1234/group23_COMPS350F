import tkinter as tk
from utils.page_view import PageView
from tkinter import PhotoImage
from utils.canvas_button import CanvasButton # type: ignore

class AboutPageView(PageView):
    def __init__(self, parent):
        super().__init__(parent, height = 712.5, width = 892.5, bg="#F5F5F5", bd=0, highlightthickness=0, relief="ridge")
        self.image_path = self.image_path / "about/images/"
        
        self.canvas = tk.Canvas(self, height = 712.5, width = 892.5, bg="#F5F5F5", bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack(fill="both", expand=True)

    def render(self):
        self.canvas.create_text(69, 32, anchor="nw", text="About", fill="#282828", font=("Roboto Black", 36 * -1))
        for i in range(60):
            tk.Label(self.canvas, text=f"Frame 1 - Item {i + 1}", bg="lightblue").pack(anchor="w", padx=10, pady=2)
        self.parent.set_frame(self)
    
    def update(self):
        pass