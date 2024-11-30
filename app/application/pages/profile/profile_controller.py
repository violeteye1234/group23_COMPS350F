from utils.page_controller import PageController  # Import base class for page controllers
from .profile_view import ProfilePageView  # Import the view class for the profile page

# Define the ProfilePageController class, inheriting from PageController
class ProfilePageController(PageController):
    def __init__(self, root, parent_container):
        # Initialize the parent class with the root and parent container
        super().__init__(root, parent_container)
        
        # Create the Profile page view
        self.view = ProfilePageView(parent_container)
        
        # Set this controller as the controller for the view
        self.view.set_controller()