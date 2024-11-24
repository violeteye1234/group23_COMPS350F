import tkinter as tk

class CanvasButton:
    # Milliseconds for flash duration
    flash_delay = 100 

    def __init__(self, canvas, x, y, image_path_normal, command, image_path_hover=None, state=tk.NORMAL, tags=None, text="", font_size=12,text_width=800):
         # Initialize the button with parameters including position, images, command, and text
        self.canvas = canvas
        self.btn_image_normal = tk.PhotoImage(file=image_path_normal) # Load normal state image
        self.btn_image_hover = tk.PhotoImage(file=image_path_hover) if image_path_hover else None # Load hover state image if provided
        self.canvas_btn_img_obj = canvas.create_image(x, y, anchor='center', state=state, 
                                                      image=self.btn_image_normal, tags=tags) # Create image on canvas
        # Bind mouse click event to flash effect and command execution
        canvas.tag_bind(self.canvas_btn_img_obj, "<ButtonRelease-1>", lambda event: (self.flash(), command()))
        self.canvas.tag_bind(self.canvas_btn_img_obj, "<Enter>", self.on_enter) # Bind hover enter event
        self.canvas.tag_bind(self.canvas_btn_img_obj, "<Leave>", self.on_leave)# Bind hover leave event
        

        # Add text label to the button with custom font size
        self.text_obj = canvas.create_text(x, y, text=text, font=("Arial", font_size), fill="black", state=state, tags=tags,width=text_width)

    def flash(self):
        # Flash the button by hiding it briefly     
        self.set_state(tk.HIDDEN)
        self.canvas.after(self.flash_delay, self.set_state, tk.NORMAL)

    def set_state(self, state):
         # Set the state of the button (visible/hidden)
        self.canvas.itemconfigure(self.canvas_btn_img_obj, state=state)

    def on_enter(self, event):
        # Change image to hover image on mouse enter
        if self.btn_image_hover:
            self.canvas.itemconfig(self.canvas_btn_img_obj, image=self.btn_image_hover)

    def on_leave(self, event):
         # Change image back to normal on mouse leave
        self.canvas.itemconfig(self.canvas_btn_img_obj, image=self.btn_image_normal)

        