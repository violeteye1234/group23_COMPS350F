# models/__init__.py

from models.user import User
from models.my_flight import MyFlight
from models.my_baggage import MyBaggage
from models.notification import Notification
from models.database import Database

__all__ = ['User', 'Flight', 'Baggage', 'Notification', 'Database']