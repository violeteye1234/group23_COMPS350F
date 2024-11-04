# models/user.py
from models.my_flight import MyFlight
from models.my_baggage import MyBaggage

class User:
    def __init__(self, user_id, username, email):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.current_location = None
        
        self.flights = []
        self.baggages = []
        
    def get_location(self):
        # self.current_location = 
        pass

    def update_info(self):
        pass
    
    def getFlight(self) -> list[MyFlight]:
        return []
    
    def getBaggage(self) -> list[MyBaggage]:
        return []

    def __str__(self):
        return f"User({self.user_id}, {self.first_name} {self.last_name}, {self.email})"
