from pages.page_controller import PageController
from .personal_information_view import PersonalInformationPageView

class PersonalInformationPageController(PageController):
    def __init__(self, root, parent_container):
        super().__init__(root, parent_container)
        self.view = PersonalInformationPageView(parent_container)