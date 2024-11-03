from pages.page_controller import PageController
from .topbar_view import TopbarView

class TopbarController(PageController):
    def __init__(self, root):
        super().__init__(root)
        self.view = TopbarView(root)