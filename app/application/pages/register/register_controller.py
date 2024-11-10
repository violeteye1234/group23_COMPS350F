from utils.page_controller import PageController
from .register_view import RegisterPageView
import tkinter as tk

class RegisterPageController(PageController):
    def __init__(self, root, parent_container):
        super().__init__(root, parent_container)
        self.view = RegisterPageView(parent_container)
        self.view.set_controller(self)
        self.view.render()
        
    def register(self, full_name: str, phone: str, email: str, password: str, confirm_password: str):
        self.root.logger.info(f"Attempting to register with full name: {full_name}, phone: {phone}, email: {email}, password: {password}, confirm password: {confirm_password}")
        
        if password != confirm_password:
            self.root.logger.error("Passwords do not match!")
            return
        
        # 这里你可以添加注册逻辑，例如将用户信息保存到数据库
        self.root.logger.info("Registration successful!")
        self.root.show_page('Login')
    
    def go_to_login(self):
        self.root.show_page('Login')
    
    def cleanup(self):
        self.view.destroy()
        self.view = None

class CanvasButton:
    flash_delay = 100  # Milliseconds.

    def __init__(self, canvas, x, y, image_path, command, state=tk.NORMAL, tags=None):
        self.canvas = canvas
        self.btn_image = tk.PhotoImage(file=image_path)
        self.canvas_btn_img_obj = canvas.create_image(x, y, anchor='center', state=state, 
                                                      image=self.btn_image, tags=tags)
        canvas.tag_bind(self.canvas_btn_img_obj, "<ButtonRelease-1>", 
                        lambda event: (self.flash(), command()))
        
    def flash(self):
        self.set_state(tk.HIDDEN)
        self.canvas.after(self.flash_delay, self.set_state, tk.NORMAL)

    def set_state(self, state):
        self.canvas.itemconfigure(self.canvas_btn_img_obj, state=state)