from utils.page_controller import PageController
from .help_view import HelpPageView

class HelpPageController(PageController):
    def __init__(self, root, parent_container):
        super().__init__(root, parent_container)
        self.view = HelpPageView(parent_container)