from pages.page_controller import PageController
from .notification_center_view import NotificationCenterPageView

class NotificationCenterPageController(PageController):
    def __init__(self, root):
        super().__init__(root)
        self.view = NotificationCenterPageView(root)