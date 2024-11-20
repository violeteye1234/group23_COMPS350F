# dashboard model
'''
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

    def get_flight_data(self, table_name, index, field_name):
        flight_data = self.pagedata[table_name][index][field_name]
        # departure_time = flight_data.get('departuretime', 'N/A')
        #flight_data = datetime.now()
        #flight_data = datetime.timedelta(hours=flight_data.hour, minutes=flight_data.minute)
        time = flight_data
        return time

  
        #flight_data = datetime.timedelta(hours=flight_data.hour, minutes=flight_data.minute)

'''
