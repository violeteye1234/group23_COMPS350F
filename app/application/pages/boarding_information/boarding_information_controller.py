from pages.page_controller import PageController
from .boarding_information_view import BoardingInformationPageView

class BoardingInformationPageController(PageController):
    def __init__(self, root):
        super().__init__(root)
        self.view = BoardingInformationPageView(root)