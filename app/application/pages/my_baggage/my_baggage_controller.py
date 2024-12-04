from utils.page_controller import PageController
from .my_baggage_view import MyBaggagePageView

class MyBaggagePageController(PageController):
    def __init__(self, root, parent_container):
        # Initialize the MyBaggagePageController by calling the parent constructor
        super().__init__(root, parent_container)
        
        # Store a reference to the root object
        self.root = root

        # Create an instance of MyBaggagePageView, passing the parent container
        self.view = MyBaggagePageView(parent_container)

        # Set this controller as the controller for the MyBaggagePageView
        self.view_set_controller()