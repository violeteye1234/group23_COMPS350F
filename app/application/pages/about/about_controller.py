from utils.page_controller import PageController
from .about_view import AboutPageView

class AboutPageController(PageController):
    def __init__(self, root, parent_container):
        # Initialize the AboutPageController with root and parent container

        # Call the parent class constructor
        super().__init__(root, parent_container)
        # Create an instance of AboutPageView
        self.view = AboutPageView(parent_container)
        # Set this controller as the controller for the view
        self.view_set_controller()