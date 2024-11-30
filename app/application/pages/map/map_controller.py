from utils.page_controller import PageController  # Import base class for page controllers
from .map_view import MapPageView  # Import the view class for the map page

# Define the MapPageController class, inheriting from PageController
class MapPageController(PageController):
    def __init__(self, root, parent_container):
        # Initialize the parent class with the root and parent container
        super().__init__(root, parent_container)
        self.view = MapPageView(parent_container)  # Create the map page view
        self.view.set_controller()  # Set this controller as the controller for the view