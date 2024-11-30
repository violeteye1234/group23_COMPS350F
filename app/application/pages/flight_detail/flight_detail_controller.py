from utils.page_controller import PageController  # Import the base class for page controllers
from .flight_detail_view import FlightDetailPageView  # Import the view class for the flight detail page

# Define the FlightDetailPageController class, inheriting from PageController
class FlightDetailPageController(PageController):
    def __init__(self, root, parent_container):
        # Initialize the parent class with the root and parent container
        super().__init__(root, parent_container)
        
        # Create an instance of the FlightDetailPageView, passing the parent container
        self.view = FlightDetailPageView(parent_container)
        
        # Set this controller as the controller for the view
        self.view.set_controller(self)