from pages.page_controller import PageController
from .login_view import LoginPageView

class LoginPageController(PageController):
    def __init__(self, root):
        super().__init__(root)
        self.view = LoginPageView(root)