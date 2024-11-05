from utils.page_controller import PageController
from .flight_detail_view import FlightDetailPageView

class FlightDetailPageController(PageController):
    def __init__(self, root, parent_container):
        super().__init__(root, parent_container)
        self.view = FlightDetailPageView(parent_container)
        self.view_set_controller()