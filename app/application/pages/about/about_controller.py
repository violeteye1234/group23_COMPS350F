from pages.page_controller import PageController
from .about_view import AboutPageView

class AboutPageController(PageController):
    def __init__(self, root, parent_container):
        super().__init__(root, parent_container)
        self.view = AboutPageView(parent_container)