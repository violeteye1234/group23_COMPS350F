from utils.page_controller import PageController
from .register_view import RegisterPageView

class RegisterPageController(PageController):
    def __init__(self, root, parent_container):
        super().__init__(root, parent_container)
        self.view = RegisterPageView(parent_container)
        self.view_set_controller()