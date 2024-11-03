from pages.page_controller import PageController
from .help_view import HelpPageView

class HelpPageController(PageController):
    def __init__(self, root):
        super().__init__(root)
        self.view = HelpPageView(root)