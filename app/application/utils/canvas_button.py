import tkinter as tk

class CanvasButton:
    flash_delay = 100  # Milliseconds.

    def __init__(self, canvas, x, y, image_path_normal, command,image_path_hover=None, state=tk.NORMAL, tags=None):
        self.canvas = canvas
        self.btn_image_normal = tk.PhotoImage(file=image_path_normal)
        self.btn_image_hover = tk.PhotoImage(file=image_path_hover) if image_path_hover else None
        self.canvas_btn_img_obj = canvas.create_image(x, y, anchor='center', state=state, 
                                                      image=self.btn_image_normal, tags=tags)
        canvas.tag_bind(self.canvas_btn_img_obj, "<ButtonRelease-1>", lambda event: (self.flash(), command()))
        self.canvas.tag_bind(self.canvas_btn_img_obj, "<Enter>", self.on_enter)
        self.canvas.tag_bind(self.canvas_btn_img_obj, "<Leave>", self.on_leave)


    def flash(self):
        self.set_state(tk.HIDDEN)
        self.canvas.after(self.flash_delay, self.set_state, tk.NORMAL)

    def set_state(self, state):
        self.canvas.itemconfigure(self.canvas_btn_img_obj, state=state)

    def on_enter(self, event):
        self.is_hovering = True
        if self.btn_image_hover:
            self.canvas.itemconfig(self.canvas_btn_img_obj, image=self.btn_image_hover)

    def on_leave(self, event):
        self.is_hovering = False
        self.canvas.itemconfig(self.canvas_btn_img_obj, image=self.btn_image_normal)
