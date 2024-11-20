# dashboard model
from pages.login1.login1_controller import Login1PageController


class DashboardModel:
    def __init__(self):
        self.pagedata = {
            'flights': [],
            'baggages': []
        }

    def set_user_data(self, user_data):
        self.pagedata['user'] = user_data
    
    def set_flights(self, flights):
        self.pagedata['flights'] = flights

    def set_baggages(self, baggages):
        self.pagedata['baggages'] = baggages


    def get_data(self):
        return self.pagedata

    def get_flight_by_id(self, flight_id):
        for flight in self.pagedata['flights']:
            if flight['flightid'] == flight_id:
                return flight
        return None