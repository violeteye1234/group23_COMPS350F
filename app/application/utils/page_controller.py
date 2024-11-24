from utils.page_view import PageView

class PageController:
    def __init__(self, root, parent_container):
        # Initialize the PageController with root and parent container
        self.root = root
        self.view:PageView = None
        
    def view_set_controller(self):
        # Set the controller for the associated view
        self.view.set_controller(self)
    
    def render(self):
        # Call the render method on the view to display its contents
        self.view.render()
        
    def log(self, text:str) -> None:
        # Log a message using the logger associated with the root
        self.root.logger.info(text)
        
    def cleanup(self) -> None:
        # Cleanup method to destroy the current view and reset the view reference
        self.view.destroy()
        self.view = None # type: ignore
        
    def scale_all_widgets(self, scale_factor):
        # Scale all widgets in the view's canvas by the given scale factor
        self.view.canvas.scale("all", 0, 0, scale_factor, scale_factor)  # Apply scaling transformation
        self.view.canvas.config(scrollregion=self.view.canvas.bbox("all"))  # Update the canvas scroll region based on the new size