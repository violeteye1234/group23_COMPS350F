from pages.page_controller import PageController
from .my_baggage_view import MyBaggagePageView

class MyBaggagePageController(PageController):
    def __init__(self, root, parent_container):
        super().__init__(root, parent_container)
        self.view = MyBaggagePageView(parent_container)