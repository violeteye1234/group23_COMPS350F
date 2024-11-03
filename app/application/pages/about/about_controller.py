from pages.page_controller import PageController
from .about_view import AboutPageView

class AboutPageController(PageController):
    def __init__(self, root):
        super().__init__(root)
        self.view = AboutPageView(root)