from utils.page_controller import PageController
from .boarding_information_view import BoardingInformationPageView

class BoardingInformationPageController(PageController):
    def __init__(self, root, parent_container):
        # Initialize the BoardingInformationPageController by calling the parent constructor
        super().__init__(root, parent_container)
        # Create an instance of BoardingInformationPageView, passing the parent container
        self.view = BoardingInformationPageView(parent_container)
        # Set this controller as the controller for the BoardingInformationPageView
        self.view_set_controller()