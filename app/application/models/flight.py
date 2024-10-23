from datetime import datetime

class Flight:
    def __init__(self, flight_number: str, departure_time:datetime, arrival_time:datetime, departure_airport:str, arrival_airport: str, gate:str, status:str):
        self.flight_number = flight_number
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.departure_airport = departure_airport
        self.arrival_airport = arrival_airport
        self.gate = gate
        self.status = status

    def update_status(self, new_status):
        self.status = new_status

    def __str__(self):
        return f"Flight({self.flight_number}: {self.departure} -> {self.destination}, {self.status})"
    
    
if __name__ == "__main__":
    # 創建一個 Flight 實例
    flight = Flight(
        flight_number="CX123",
        departure_time=datetime(2024, 10, 23, 10, 30),
        arrival_time=datetime(2024, 10, 23, 14, 45),
        departure_airport="London",
        arrival_airport="Hong Kong",
        gate="A12",
        status="On Time"
    )

    # 打印 Flight 信息
    print(flight)

    # 測試更新航班狀態的方法
    flight.update_status("Delayed")
    print(f"Updated Status: {flight.status}")

    # 測試 __str__ 方法
    print(f"Flight Info: {flight}")