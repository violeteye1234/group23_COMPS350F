import tkinter as tk

class CanvasButton:
    flash_delay = 100  # Milliseconds.

    def __init__(self, canvas, x, y, image_path, command, state=tk.NORMAL, tags=None):
        self.canvas = canvas
        self.btn_image = tk.PhotoImage(file=image_path)
        self.canvas_btn_img_obj = canvas.create_image(x, y, anchor='nw', state=state, 
                                                      image=self.btn_image, tags=tags)
        canvas.tag_bind(self.canvas_btn_img_obj, "<ButtonRelease-1>", 
                        lambda event: (self.flash(), command()))
        
    def flash(self):
        self.set_state(tk.HIDDEN)
        self.canvas.after(self.flash_delay, self.set_state, tk.NORMAL)

    def set_state(self, state):
        self.canvas.itemconfigure(self.canvas_btn_img_obj, state=state)
      