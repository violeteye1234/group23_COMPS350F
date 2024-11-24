import tkinter as tk
from utils.page_view import PageView
from tkinter import PhotoImage
from utils.canvas_button import CanvasButton # type: ignore

class AboutPageView(PageView):
    def __init__(self, parent):
        # Initialize the AboutPageView with specified dimensions and background color
        super().__init__(parent, height = 1701, width = 892.5, bg="#F5F5F5", bd=0, highlightthickness=0, relief="ridge")
        self.image_path = self.image_path / "about/images/"
        
        # Create a canvas to hold images and text
        self.canvas = tk.Canvas(self, height = 1701, width = 892.5, bg="#F5F5F5", bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack(fill="both", expand=True) # Pack the canvas to fill the parent frame

    def render(self):
        # Load and display images and text on the canvas
        
        # Load and place the first image
        self.image_image_1 = PhotoImage(file=self.image_path / "image_1.png")
        self.image_1 = self.canvas.create_image(445.75, 109.5, image=self.image_image_1)

        # Create and place the "About Us" text  
        self.canvas.create_text(51.75, 219.0, anchor="nw", text="About Us", fill="#282828", font=("Roboto Black", 36 * -1))

        # Load and place the second image
        self.image_image_2 = PhotoImage(file=self.image_path / "image_2.png")
        self.image_2 = self.canvas.create_image(450.75, 323.5, image=self.image_image_2)

        # Create and place the "Our Team" text
        self.canvas.create_text(51.75, 417.0, anchor="nw", text="Our Team", fill="#282828", font=("Roboto Black", 36 * -1))

        # Load and place additional images
        self.image_image_3 = PhotoImage(file=self.image_path / "image_3.png")
        self.image_3 = self.canvas.create_image(238.5, 431.25, image=self.image_image_3)

        self.image_image_4 = PhotoImage(file=self.image_path / "image_4.png")
        self.image_4 = self.canvas.create_image(235.75, 578.5, image=self.image_image_4)

        self.image_image_5 = PhotoImage(file=self.image_path / "image_5.png")
        self.image_5 = self.canvas.create_image(661.0, 776.5, image=self.image_image_5)

        self.image_image_6 = PhotoImage(file=self.image_path / "image_6.png")
        self.image_6 = self.canvas.create_image(661.0, 578.5, image=self.image_image_6)

        self.image_image_7 = PhotoImage(file=self.image_path / "image_7.png")
        self.image_7 = self.canvas.create_image(661.0, 974.5, image=self.image_image_7)

        self.image_image_8 = PhotoImage(file=self.image_path / "image_8.png")
        self.image_8 = self.canvas.create_image(235.75, 776.5, image=self.image_image_8)

        self.image_image_9 = PhotoImage(file=self.image_path / "image_9.png")
        self.image_9 = self.canvas.create_image(661.0, 1172.5, image=self.image_image_9)

        self.image_image_10 = PhotoImage(file=self.image_path / "image_10.png")
        self.image_10 = self.canvas.create_image(235.75, 974.5, image=self.image_image_10)

        self.image_image_11 = PhotoImage(file=self.image_path / "image_11.png")
        self.image_11 = self.canvas.create_image(235.75, 1370.5, image=self.image_image_11)

        self.image_image_12 = PhotoImage(file=self.image_path / "image_12.png")
        self.image_12 = self.canvas.create_image(235.75, 1172.5, image=self.image_image_12)

        # Create and place the "Committed to Excellence" text
        self.canvas.create_text(51.75, 1535.25, anchor="nw", text="Committed to Excellence", fill="#282828", font=("Roboto Black", 36 * -1))

        # Load and place the final image
        self.image_image_13 = PhotoImage(file=self.image_path / "image_13.png")
        self.image_13 = self.canvas.create_image(431.75, 1639.5, image=self.image_image_13)
        
        #for i in range(90):
        #    tk.Label(self.canvas, text=f"Frame 1 - Item {i + 1}", bg="lightblue").pack(anchor="w", padx=10, pady=2)
       
        # Set this frame as the current frame in the parent
        self.parent.set_frame(self)
        
    
    def update(self):
        # Placeholder method for future updates to the view
        pass