from utils.page_controller import PageController
from .notification_center_view import NotificationCenterPageView

class NotificationCenterPageController(PageController):
    def __init__(self, root, parent_container):
        super().__init__(root, parent_container)
        self.view = NotificationCenterPageView(parent_container)
        self.view_set_controller()
