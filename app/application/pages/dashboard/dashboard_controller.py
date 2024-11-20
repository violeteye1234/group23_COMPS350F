# dashboaed controller
from utils.page_controller import PageController
from .dashboard_view import DashboardPageView
from models.user_model import UserModel
from models.dashboard import DashboardModel
import tkinter as tk
from pages.login1.login1_controller import Login1PageController
from models.sharedata import SharedData

class DashboardPageController(PageController):
    def __init__(self, root, parent_container):
        super().__init__(root, parent_container)
        self.parent_container = parent_container
        self.view = DashboardPageView(parent_container)
        self.view.set_controller(self)
        # self.load_data()
        self.model = DashboardModel()
        # self.view.insert_data()
        self.user_data = SharedData.user_data
        print(self.user_data)
    '''
    def load_data(self):
        login_controller = Login1PageController(self.root, self.parent_container)
        user_data = login_controller.user_data
        flights = user_data.get('flights', [])
        baggages = user_data.get('baggages', [])

        # update pagedata
        self.model.set_user_data(user_data)
        self.model.set_flights(flights)
        self.model.set_baggages(baggages)

        # get element by id
        flight_id = 101
        flight_data = self.model.get_flight_by_id(flight_id)
        if flight_data:
            self.view.insert_data({'flight': flight_data})
    '''