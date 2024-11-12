# models/notification.py

# so you have to had a notification table in the database

class Notification:
    def __init__(self, notification_id, user_id, title, message, datetime, is_read=False):
        self.notification_id = notification_id
        self.user_id = user_id
        self.title = title
        self.message = message
        self.datetime = datetime
        self.is_read = is_read
        
    def get_notifications(self) -> list: # type: ignore
        pass
        
    def check_flight(self) -> None:
        pass
    
    def check_baggage(self) -> None:
        pass

    def __str__(self):
        status = "Read" if self.is_read else "Unread"
        return f"Notification({self.notification_id}, {self.title}, {status})"
