from utils.page_controller import PageController
from .help_view import HelpPageView

class HelpPageController(PageController):
    def __init__(self, root, parent_container):
        # Initialize the HelpPageController by calling the parent constructor
        super().__init__(root, parent_container)
        # Create an instance of HelpPageView, passing the parent container
        self.view = HelpPageView(parent_container)
        # Set this controller as the controller for the HelpPageView
        self.view_set_controller()