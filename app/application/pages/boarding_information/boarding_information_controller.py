from utils.page_controller import PageController
from .boarding_information_view import BoardingInformationPageView

class BoardingInformationPageController(PageController):
    def __init__(self, root, parent_container):
        # Initialize the BoardingInformationPageController with root and parent container
        super().__init__(root, parent_container)
        # Call the parent class constructor
        self.view = BoardingInformationPageView(parent_container)
        # Create an instance of BoardingInformationPageView
        self.view_set_controller() # Set this controller as the controller for the view