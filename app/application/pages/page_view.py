import tkinter as tk

class PageView(tk.Frame):
    def __init__(self):
        self.controller = None
    
    def set_controller(self, controller):
        self.controller = controller
    
    def render(self):
        pass
