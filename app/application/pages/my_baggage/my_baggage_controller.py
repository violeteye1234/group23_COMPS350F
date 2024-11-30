from utils.page_controller import PageController  # Import base class for page controllers
from .my_baggage_view import MyBaggagePageView  # Import the view class for the My Baggage page

# Define the MyBaggagePageController class, inheriting from PageController
class MyBaggagePageController(PageController):
    def __init__(self, root, parent_container):
        # Initialize the parent class with the root and parent container
        super().__init__(root, parent_container)
        self.root = root  # Store the root reference
        self.view = MyBaggagePageView(parent_container)  # Create the My Baggage page view
        self.view.set_controller()  # Set this controller as the controller for the view