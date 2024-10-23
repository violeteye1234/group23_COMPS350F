# models/my_baggage.py
from models.baggage import Baggage

class MyBaggage(Baggage):
    def __init__(self, baggage, owner:User): # type: ignore
        super().__init__(baggage.baggage_id, baggage.user_id, baggage.flight_number, baggage.status, baggage.current_location, baggage.activity_history)
        self.owner = owner