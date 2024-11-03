from pages.page_controller import PageController
from .notification_setting_view import NotificationSettingPageView

class NotificationSettingPageController(PageController):
    def __init__(self, root):
        super().__init__(root)
        self.view = NotificationSettingPageView(root)