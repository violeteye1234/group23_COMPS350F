from pages.page_controller import PageController
from .flight_detail_view import FlightDetailPageView

class FlightDetailPageController(PageController):
    def __init__(self, root):
        super().__init__(root)
        self.view = FlightDetailPageView(root)