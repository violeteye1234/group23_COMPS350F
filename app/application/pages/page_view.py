import tkinter as tk
from pathlib import Path
from typing import Any, Dict, Optional

class PageView(tk.Frame):
    def __init__(self, parent, *args: Any, **kwargs: Any):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.controller = None

        self.project_dir = Path(__file__).resolve().parent
        self.image_path = self.project_dir
    
    def set_controller(self, controller):
        self.controller = controller
    
    def render(self):
        pass
