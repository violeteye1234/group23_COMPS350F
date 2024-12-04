from utils.page_controller import PageController
from .flight_detail_view import FlightDetailPageView

class FlightDetailPageController(PageController):
    def __init__(self, root, parent_container):
        # Initialize the FlightDetailPageController by calling the parent constructor
        super().__init__(root, parent_container)
        # Create an instance of FlightDetailPageView, passing the parent container
        self.view = FlightDetailPageView(parent_container)
        # Set this controller as the controller for the FlightDetailPageView
        self.view_set_controller()