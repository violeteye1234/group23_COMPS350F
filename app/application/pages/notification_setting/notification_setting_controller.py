from utils.page_controller import PageController  # Import base class for page controllers
from .notification_setting_view import NotificationSettingPageView  # Import the view class for notification settings

# Define the NotificationSettingPageController class, inheriting from PageController
class NotificationSettingPageController(PageController):
    def __init__(self, root, parent_container):
        # Initialize the parent class with the root and parent container
        super().__init__(root, parent_container)
        
        # Create the Notification Setting page view
        self.view = NotificationSettingPageView(parent_container)
        
        # Set this controller as the controller for the view
        self.view.set_controller()