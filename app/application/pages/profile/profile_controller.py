from pages.page_controller import PageController
from .profile_view import ProfilePageView

class ProfilePageController(PageController):
    def __init__(self, root):
        super().__init__(root)
        self.view = ProfilePageView(root)