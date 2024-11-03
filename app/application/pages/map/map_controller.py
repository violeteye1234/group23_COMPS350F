from pages.page_controller import PageController
from .map_view import MapPageView

class MapPageController(PageController):
    def __init__(self, root):
        super().__init__(root)
        self.view = MapPageView(root)