# models/user.py
from models.my_flight import MyFlight
from models.my_baggage import MyBaggage

class User:
    def __init__(self, user_id, first_name, last_name, gender, birthday, passport, phone_number, email, password):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.birthday = birthday
        self.passport = passport
        self.phone_number = phone_number
        self.email = email
        
        self.flights = []
        self.baggages = []

    def update_info(self):
        pass
    
    def getFlight(self) -> list[MyFlight]:
        return []
    
    def getBaggage(self) -> list[MyBaggage]:
        return []

    def __str__(self):
        return f"User({self.user_id}, {self.first_name} {self.last_name}, {self.email})"
