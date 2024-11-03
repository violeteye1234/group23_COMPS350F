from pages.page_controller import PageController
from .register_view import RegisterPageView

class RegisterPageController(PageController):
    def __init__(self, root):
        super().__init__(root)
        self.view = RegisterPageView(root)