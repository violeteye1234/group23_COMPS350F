from pages.page_controller import PageController
from .baggage_detail_view import BaggageDetailPageView

class BaggageDetailPageController(PageController):
    def __init__(self, root):
        super().__init__(root)
        self.view = BaggageDetailPageView(root)