from utils.page_controller import PageController
from .notification_center_view import NotificationCenterPageView
from pages.my_baggage.my_baggage_controller import MyBaggagePageController
#from utils.scrollable_frame import ScrollableFrame
#import tkinter as tk


class NotificationCenterPageController(PageController):
    def __init__(self, root, parent_container):
        super().__init__(root, parent_container)
        self.root = root
        self.view = NotificationCenterPageView(parent_container)
        self.view_set_controller()