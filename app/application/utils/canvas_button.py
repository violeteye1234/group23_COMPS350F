import tkinter as tk

class CanvasButton:
    flash_delay = 100  # Milliseconds.

    def __init__(self, canvas, x, y, image_path_normal, command, image_path_hover=None, state=tk.NORMAL, tags=None, text="", font_size=12,text_width=800):
        # Initialize the button on the specified canvas at (x, y)
        self.canvas = canvas
        # Load the normal state image for the button
        self.btn_image_normal = tk.PhotoImage(file=image_path_normal)
        # Load the hover state image if provided
        self.btn_image_hover = tk.PhotoImage(file=image_path_hover) if image_path_hover else None
        # Create the image on the canvas
        self.canvas_btn_img_obj = canvas.create_image(x, y, anchor='center', state=state, 
                                                      image=self.btn_image_normal, tags=tags)
        canvas.tag_bind(self.canvas_btn_img_obj, "<ButtonRelease-1>", lambda event: (self.flash(), command()))
        # Bind mouse enter and leave events for hover effects
        self.canvas.tag_bind(self.canvas_btn_img_obj, "<Enter>", self.on_enter)
        self.canvas.tag_bind(self.canvas_btn_img_obj, "<Leave>", self.on_leave)
        

        # Add text label to the button with custom font size
        self.text_obj = canvas.create_text(x, y, text=text, font=("Arial", font_size), fill="black", state=state, tags=tags,width=text_width)

    def flash(self):
        # Temporarily hide the button and then show it again after a delay
        self.set_state(tk.HIDDEN)
        self.canvas.after(self.flash_delay, self.set_state, tk.NORMAL)

    def set_state(self, state):
        # Change the visibility state of the button image
        self.canvas.itemconfigure(self.canvas_btn_img_obj, state=state)

    def on_enter(self, event):
        # Change the button image to hover state when mouse enters
        if self.btn_image_hover:
            self.canvas.itemconfig(self.canvas_btn_img_obj, image=self.btn_image_hover)

    def on_leave(self, event):
        # Revert the button image to normal state when mouse leaves
        self.canvas.itemconfig(self.canvas_btn_img_obj, image=self.btn_image_normal)