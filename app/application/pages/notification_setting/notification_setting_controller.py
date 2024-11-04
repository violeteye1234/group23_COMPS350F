from utils.page_controller import PageController
from .notification_setting_view import NotificationSettingPageView

class NotificationSettingPageController(PageController):
    def __init__(self, root, parent_container):
        super().__init__(root, parent_container)
        self.view = NotificationSettingPageView(parent_container)