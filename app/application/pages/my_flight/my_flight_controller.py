from utils.page_controller import PageController
from .my_flight_view import MyFlightPageView

class MyFlightPageController(PageController):
    def __init__(self, root, parent_container):
        # Initialize the MyFlightPageController by calling the parent constructor
        super().__init__(root, parent_container)

        # Create an instance of MyFlightPageView, passing the parent container
        self.view = MyFlightPageView(parent_container)

        # Set this controller as the controller for the MyFlightPageView
        self.view_set_controller()