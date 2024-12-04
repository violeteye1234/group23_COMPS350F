from utils.page_controller import PageController
from .map_view import MapPageView

class MapPageController(PageController):
    def __init__(self, root, parent_container):
        # Initialize the MapPageController by calling the parent constructor
        super().__init__(root, parent_container)

        # Create an instance of MapPageView, passing the parent container
        self.view = MapPageView(parent_container)
        
        # Set this controller as the controller for the MapPageView
        self.view_set_controller()