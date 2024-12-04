import tkinter as tk
from pathlib import Path
from typing import Any, Dict, Optional

class PageView(tk.Frame):
    def __init__(self, parent, *args: Any, **kwargs: Any):
        # Initialize the parent Frame and store the parent reference
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.controller = None # Initialize the controller to None

        # Set the project directory to the parent of the current file's directory

        self.project_dir = Path(__file__).resolve().parent.parent
        
        # Construct the path to the "pages" directory within the project
        self.image_path = self.project_dir / "pages"
    
    def set_controller(self, controller):
        # Set the controller for this PageView, allowing interaction with other components
        self.controller = controller
    
    def render(self):
        # Method to render the page view; currently a placeholder
        pass
