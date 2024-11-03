from pages.page_controller import PageController
from .my_baggage_view import MyBaggagePageView

class MyBaggagePageController(PageController):
    def __init__(self, root):
        super().__init__(root)
        self.view = MyBaggagePageView(root)