from utils.page_controller import PageController
from .boarding_information_view import BoardingInformationPageView

class BoardingInformationPageController(PageController):
    def __init__(self, root, parent_container):
        super().__init__(root, parent_container)
        self.view = BoardingInformationPageView(parent_container)
        self.view_set_controller()