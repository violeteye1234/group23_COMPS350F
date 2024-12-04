from utils.page_controller import PageController
from .about_view import AboutPageView

class AboutPageController(PageController):
    def __init__(self, root, parent_container):
        # Initialize the AboutPageController by calling the parent constructor
        super().__init__(root, parent_container)
        # Create an instance of AboutPageView, passing the parent container
        self.view = AboutPageView(parent_container)
        # Set this controller as the controller for the AboutPageView
        self.view_set_controller()