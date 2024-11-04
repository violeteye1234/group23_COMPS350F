from pages.page_controller import PageController
from .dashboard_view import DashboardPageView

class DashboardPageController(PageController):
    def __init__(self, root, parent_container):
        super().__init__(root, parent_container)
        self.view = DashboardPageView(parent_container)