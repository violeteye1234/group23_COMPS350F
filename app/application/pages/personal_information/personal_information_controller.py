from utils.page_controller import PageController
from .personal_information_view import PersonalInformationPageView

class PersonalInformationPageController(PageController):
    def __init__(self, root, parent_container):
        super().__init__(root, parent_container)

        # Create an instance of PersonalInformationPageView, passing the parent container
        self.view = PersonalInformationPageView(parent_container)

        # Set this controller as the controller for the PersonalInformationPageView
        self.view_set_controller()