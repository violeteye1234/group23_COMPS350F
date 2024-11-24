from utils.page_controller import PageController
from .baggage_detail_view import BaggageDetailPageView

class BaggageDetailPageController(PageController):
    def __init__(self, root, parent_container):
        # Initialize the BaggageDetailPageController with root and parent container

        # Call the parent class constructor 
        super().__init__(root, parent_container)
        # Create an instance of BaggageDetailPageView
        self.view = BaggageDetailPageView(parent_container)
        # Set this controller as the controller for the view
        self.view_set_controller()

