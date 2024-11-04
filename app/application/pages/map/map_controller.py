from pages.page_controller import PageController
from .map_view import MapPageView

class MapPageController(PageController):
    def __init__(self, root, parent_container):
        super().__init__(root, parent_container)
        self.view = MapPageView(parent_container)