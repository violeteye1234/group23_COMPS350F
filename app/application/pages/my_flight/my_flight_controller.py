from utils.page_controller import PageController
from .my_flight_view import MyFlightPageView

class MyFlightPageController(PageController):
    def __init__(self, root, parent_container):
        super().__init__(root, parent_container)
        self.view = MyFlightPageView(parent_container)