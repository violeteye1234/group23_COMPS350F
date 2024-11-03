from pages.page_controller import PageController
from .sidebar_view import SideBarView

class SideBarController(PageController):
    def __init__(self, root):
        super().__init__(root)
        self.view = SideBarView(root)