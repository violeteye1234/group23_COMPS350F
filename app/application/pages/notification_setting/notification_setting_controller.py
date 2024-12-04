from utils.page_controller import PageController
from .notification_setting_view import NotificationSettingPageView

class NotificationSettingPageController(PageController):
    def __init__(self, root, parent_container):
        super().__init__(root, parent_container)

        # Create an instance of NotificationSettingPageView, passing the parent container
        self.view = NotificationSettingPageView(parent_container)

        # Set this controller as the controller for the NotificationSettingPageView
        self.view_set_controller()