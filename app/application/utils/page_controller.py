from utils.page_view import PageView

class PageController:
    def __init__(self, root, parent_container):
        # Initialize the controller with the root window and parent container
        self.root = root
        self.view:PageView = None # Placeholder for the PageView instance
        
    def view_set_controller(self):
        # Set the controller for the PageView, enabling interaction
        self.view.set_controller(self)
    
    def render(self):
        # Call the render method of the PageView to display it
        self.view.render()
        
    def log(self, text:str) -> None:
        # Log a message using the logger associated with the root
        self.root.logger.info(text)
        
    def cleanup(self) -> None:
        # Clean up the view by destroying it and setting it to None
        self.view.destroy()
        self.view = None # type: ignore
        
    def scale_all_widgets(self, scale_factor):
        # Scale all widgets on the canvas by the given scale factor
        self.view.canvas.scale("all", 0, 0, scale_factor, scale_factor)  # Scale the canvas items
        self.view.canvas.config(scrollregion=self.view.canvas.bbox("all"))  # Update the canvas bounds