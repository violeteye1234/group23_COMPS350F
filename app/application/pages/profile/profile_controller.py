from utils.page_controller import PageController
from .profile_view import ProfilePageView

class ProfilePageController(PageController):
    def __init__(self, root, parent_container):
        super().__init__(root, parent_container)
        self.view = ProfilePageView(parent_container)
        self.view_set_controller()