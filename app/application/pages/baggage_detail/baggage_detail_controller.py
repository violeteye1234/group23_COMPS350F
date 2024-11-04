from pages.page_controller import PageController
from .baggage_detail_view import BaggageDetailPageView

class BaggageDetailPageController(PageController):
    def __init__(self, root, parent_container):
        super().__init__(root, parent_container)
        self.view = BaggageDetailPageView(parent_container)