from utils.page_controller import PageController  # Import base class for page controllers
from .personal_information_view import PersonalInformationPageView  # Import the view class for personal information

# Define the PersonalInformationPageController class, inheriting from PageController
class PersonalInformationPageController(PageController):
    def __init__(self, root, parent_container):
        # Initialize the parent class with the root and parent container
        super().__init__(root, parent_container)
        
        # Create the Personal Information page view
        self.view = PersonalInformationPageView(parent_container)
        
        # Set this controller as the controller for the view
        self.view.set_controller()