from utils.page_controller import PageController  # Import base class for page controllers
from .notification_center_view import NotificationCenterPageView  # Import the view class for the Notification Center
from pages.my_baggage.my_baggage_controller import MyBaggagePageController  # Import baggage page controller
from datetime import datetime, timedelta  # Import datetime and timedelta for time calculations
from models.sharedata import SharedData  # Import SharedData model for accessing shared user data
import datetime  # Import datetime module (duplicate import, could be removed)

# Define the NotificationCenterPageController class, inheriting from PageController
class NotificationCenterPageController(PageController):
    def __init__(self, root, parent_container):
        # Initialize the parent class with the root and parent container
        super().__init__(root, parent_container)
        self.root = root  # Store the root reference
        self.view = NotificationCenterPageView(parent_container)  # Create the Notification Center page view
        self.view.set_controller()  # Set this controller as the controller for the view

        # Retrieve shared user data
        self.user_data = SharedData.user_data
        
        # Get takeoff and landing times for the first flight
        takeoff_time0 = self.user_data['flights'][0]['departuretime']
        takeoff_time = timedelta(hours=takeoff_time0.hour, minutes=takeoff_time0.minute)
        landing_time0 = self.user_data['flights'][0]['arrivaltime']
        landing_time = timedelta(hours=landing_time0.hour, minutes=landing_time0.minute)

        # Get the current time
        current_time0 = datetime.now()
        current_time = timedelta(hours=current_time0.hour, minutes=current_time0.minute)

        # Calculate important time milestones relative to the flight
        one_hour_ago = takeoff_time - timedelta(minutes=60)  # One hour before takeoff
        half_hour_ago = takeoff_time - timedelta(minutes=30)  # Half an hour before takeoff
        a_quarter_later = landing_time + timedelta(minutes=15)  # 15 minutes after landing

        # Calculate time until takeoff and time since landing
        current_time_obj = current_time
        time_until_takeoff = (takeoff_time - current_time_obj).total_seconds() / 60  # Time until takeoff in minutes
        time_later_landing = (current_time_obj - landing_time).total_seconds() / 60  # Time since landing in minutes

        # Store calculated times in the controller for later use
        self.current_time = current_time
        self.half_hour_ago = half_hour_ago
        self.a_quarter_later = a_quarter_later
        self.one_hour_ago = one_hour_ago
        self.takeoff_time = takeoff_time
        self.landing_time = landing_time
        self.time_until_takeoff = time_until_takeoff
        self.time_later_landing = time_later_landing