# dashboard controller
from utils.page_controller import PageController
from .dashboard_view import DashboardPageView
from models.user_model import UserModel
# from models.dashboard import DashboardModel
import tkinter as tk
from pages.login1.login1_controller import Login1PageController
from models.sharedata import SharedData
from datetime import datetime, timedelta
import datetime

class DashboardPageController(PageController):
    def __init__(self, root, parent_container):
        # Initialize the DashboardPageController by calling the parent constructor
        super().__init__(root, parent_container)

        # Store the parent container for future reference
        self.parent_container = parent_container

        # Create an instance of DashboardPageView, passing the parent container

        self.view = DashboardPageView(parent_container)

        # Set this controller as the controller for the DashboardPageView
        self.view.set_controller(self)
        # self.view.insert_data()
        #self.model = DashboardModel()
        #self.user_data = SharedData.user_data
        #self.load_data()
        

    '''
    def load_data(self):
        #login_controller = Login1PageController(self.root, self.parent_container)
        #user_data = login_controller.user_data

        if self.user_data is None:
            print("Error: user_data is None")
            return

        flights = self.user_data.get('flights', [])
        baggages = self.user_data.get('baggages', [])
        print(flights)

        # update pagedata
        self.model.set_user_data(self.user_data)
        self.model.set_flights(flights)
        self.model.set_baggages(baggages)

        # get element by id
        # 获取第一个航班的信息
        flight_data = self.get_flight_data('flights', 0, 'departuretime')  
            # departure_time = flight_data.get('departuretime', 'N/A')
            #flight_data = datetime.now()
            #flight_data = datetime.timedelta(hours=flight_data.hour, minutes=flight_data.minute)
        data = flight_data
        print(data)
        self.view.set_flight_data(data)
        #print(flight_data)

    def get_flight_data(self, table_name, index, field_name):
        return self.model.get_flight_data(table_name, index, field_name)
    '''