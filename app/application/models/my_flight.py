from datetime import datetime
from models.flight import Flight

class MyFlight(Flight):
    def __init__(self, flight: Flight, owner:"User", owner_seat_number:str, owner_seat_type:str): # type: ignore
        super().__init__(flight.flight_number, flight.departure_time, flight.arrival_time, flight.departure_airport, flight.arrival_airport, flight.gate, flight.status)
        self.owner = owner
        self.owner_seat_number = owner_seat_number
