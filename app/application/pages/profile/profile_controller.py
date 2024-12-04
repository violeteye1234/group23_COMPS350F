from utils.page_controller import PageController
from .profile_view import ProfilePageView

class ProfilePageController(PageController):
    def __init__(self, root, parent_container):
        super().__init__(root, parent_container)

        # Create an instance of ProfilePageView, passing the parent container
        self.view = ProfilePageView(parent_container)

        # Set this controller as the controller for the ProfilePageView
        self.view_set_controller()