from utils.page_controller import PageController  # Import base class for page controllers
from .help_view import HelpPageView  # Import the view class for the help page

# Define the HelpPageController class, inheriting from PageController
class HelpPageController(PageController):
    def __init__(self, root, parent_container):
        # Initialize the parent class with the root and parent container
        super().__init__(root, parent_container)
        
        # Create an instance of the HelpPageView, passing the parent container
        self.view = HelpPageView(parent_container)
        
        # Set this controller as the controller for the view
        self.view.set_controller(self)