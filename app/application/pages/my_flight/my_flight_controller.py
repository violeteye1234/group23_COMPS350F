from pages.page_controller import PageController
from .my_flight_view import MyFlightPageView

class MyFlightPageController(PageController):
    def __init__(self, root):
        super().__init__(root)
        self.view = MyFlightPageView(root)