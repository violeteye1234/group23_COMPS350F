from utils.page_controller import PageController  # Import base class for page controllers
from .my_flight_view import MyFlightPageView  # Import the view class for the My Flight page

# Define the MyFlightPageController class, inheriting from PageController
class MyFlightPageController(PageController):
    def __init__(self, root, parent_container):
        # Initialize the parent class with the root and parent container
        super().__init__(root, parent_container)
        self.view = MyFlightPageView(parent_container)  # Create the My Flight page view
        self.view.set_controller()  # Set this controller as the controller for the view