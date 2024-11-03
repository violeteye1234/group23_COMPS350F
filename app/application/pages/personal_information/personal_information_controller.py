from pages.page_controller import PageController
from .personal_information_view import PersonalInformationPageView

class PersonalInformationPageController(PageController):
    def __init__(self, root):
        super().__init__(root)
        self.view = PersonalInformationPageView(root)