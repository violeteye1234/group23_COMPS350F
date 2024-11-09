# models/baggage.py


class Baggage:
    def __init__(self, baggage_id, user_id, flight_number, status, current_location, activity_history):
        self.baggage_id = baggage_id
        self.user_id = user_id
        self.flight_number = flight_number
        self.status = status
        self.current_location = current_location
        self.activity_history = activity_history  # 假設 activity_history 是一個列表，記錄行李的活動

    def update_location(self, new_location):
        self.current_location = new_location
        self.activity_history.append({'location': new_location, 'timestamp': self.get_current_time()})

    def update_status(self, new_status):
        self.status = new_status
        self.activity_history.append({'status': new_status, 'timestamp': self.get_current_time()})

    def get_current_time(self):
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return f"Baggage({self.baggage_id}, Flight: {self.flight_number}, Status: {self.status})"
