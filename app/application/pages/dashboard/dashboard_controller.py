from pages.page_controller import PageController
from .dashboard_view import DashboardPageView

class DashboardPageController(PageController):
    def __init__(self, root):
        super().__init__(root)
        self.view = DashboardPageView(root)