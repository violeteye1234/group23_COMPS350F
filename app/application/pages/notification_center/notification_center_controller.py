from utils.page_controller import PageController
from .notification_center_view import NotificationCenterPageView
from pages.my_baggage.my_baggage_controller import MyBaggagePageController
from datetime import datetime, timedelta
from models.sharedata import SharedData
import datetime

class NotificationCenterPageController(PageController):
    def __init__(self, root, parent_container):
        super().__init__(root, parent_container)
        self.root = root

        # Create an instance of NotificationCenterPageView, passing the parent container
        self.view = NotificationCenterPageView(parent_container)

        # Set this controller as the controller for the NotificationCenterPageView
        self.view_set_controller()

        # Retrieve user data from shared data model
        self.user_data = SharedData.user_data

        # Extract takeoff and landing times for the first flight
        takeoff_time0 = self.user_data['flights'][0]['departuretime']
        takeoff_time = datetime.timedelta(hours=takeoff_time0.hour, minutes=takeoff_time0.minute)
        landing_time0 = self.user_data['flights'][0]['arrivaltime']
        landing_time = datetime.timedelta(hours=landing_time0.hour, minutes=landing_time0.minute)

        # Get the current time
        current_time0 = datetime.datetime.now()
        current_time = datetime.timedelta(hours=current_time0.hour, minutes=current_time0.minute)

        # Define important time thresholds
        one_hour_ago = takeoff_time - timedelta(minutes=60)  # Time for baggage check, one hour before takeoff
        half_hour_ago = takeoff_time - timedelta(minutes=30)  # Boarding time, thirty minutes before takeoff
        a_quarter_later = landing_time + timedelta(minutes=15)  # Baggage arrival, fifteen minutes after landing

        # Calculate time differences
        current_time_obj = current_time
        time_until_takeoff = (takeoff_time - current_time_obj).total_seconds() / 60
        time_later_landing = (current_time_obj - landing_time).total_seconds() / 60

    

        # Store calculated time values in the controller
        self.current_time = current_time
        self.half_hour_ago = half_hour_ago
        self.a_quarter_later = a_quarter_later
        self.one_hour_ago = one_hour_ago
        self.takeoff_time = takeoff_time
        self.landing_time = landing_time
        self.time_until_takeoff = time_until_takeoff
        self.time_later_landing = time_later_landing