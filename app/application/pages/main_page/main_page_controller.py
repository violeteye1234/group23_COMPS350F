# main_page_controller.py

from utils.page_controller import PageController  # Import base class for page controllers
from .main_page_view import MainPageView  # Import the view class for the main page
from pages.about.about_controller import AboutPageController  # Import About page controller
from pages.baggage_detail.baggage_detail_controller import BaggageDetailPageController  # Import Baggage Detail page controller
from pages.boarding_information.boarding_information_controller import BoardingInformationPageController  # Import Boarding Information page controller
from pages.dashboard.dashboard_controller import DashboardPageController  # Import Dashboard page controller
from pages.flight_detail.flight_detail_controller import FlightDetailPageController  # Import Flight Detail page controller
from pages.help.help_controller import HelpPageController  # Import Help page controller
from pages.login.login_controller import LoginPageController  # Import Login page controller
from pages.map.map_controller import MapPageController  # Import Map page controller
from pages.my_baggage.my_baggage_controller import MyBaggagePageController  # Import My Baggage page controller
from pages.my_flight.my_flight_controller import MyFlightPageController  # Import My Flight page controller
from pages.notification_center.notification_center_controller import NotificationCenterPageController  # Import Notification Center page controller
from pages.notification_setting.notification_setting_controller import NotificationSettingPageController  # Import Notification Setting page controller
from pages.personal_information.personal_information_controller import PersonalInformationPageController  # Import Personal Information page controller
from pages.profile.profile_controller import ProfilePageController  # Import Profile page controller
from pages.register.register_controller import RegisterPageController  # Import Register page controller
import time  # Import time module for handling time-related functions

# Define the MainPageController class, inheriting from PageController
class MainPageController(PageController):
    def __init__(self, root, parent_container = None):
        # Initialize the parent class with the root and optional parent container
        super().__init__(root, parent_container)
        self.root = root  # Store the root reference
        self.view = MainPageView(root.container)  # Create the main page view
        self.current_content_controller = None  # Initialize current content controller to None
        self.view.set_controller()  # Set the view's controller

        # Dictionary to map page names to their respective controllers
        self.pages = {
            "about"                  : AboutPageController                 ,
            "baggage_detail"         : BaggageDetailPageController         ,
            "boarding_information"   : BoardingInformationPageController   ,
            "dashboard"              : DashboardPageController             ,
            "flight_detail"          : FlightDetailPageController          ,
            "help"                   : HelpPageController                  ,
            "login"                  : LoginPageController                 ,
            "map"                    : MapPageController                   ,
            "my_baggage"             : MyBaggagePageController             ,
            "my_flight"              : MyFlightPageController              ,
            "notification_center"    : NotificationCenterPageController    ,
            "notification_setting"   : NotificationSettingPageController   ,
            "personal_information"   : PersonalInformationPageController   ,
            "profile"                : ProfilePageController               ,
            "register"               : RegisterPageController              
        }
        
    def switch_page(self, page_name):
        # Clean up the current content controller if it exists
        if self.current_content_controller:
            self.current_content_controller.cleanup()
        
        # Instantiate the new content controller for the given page name
        self.current_content_controller = self.pages[page_name](self.root, self.view.content_frame)
        
        # Render the new content controller
        self.current_content_controller.render()
        self.root.logger.info(f"Showing page {page_name}")  # Log the current page shown

    def clean_content(self):
        # Clean up the current content controller and clear the view
        if self.current_content_controller:
            self.current_content_controller.cleanup()
            self.current_content_controller = None
            self.view.clear_content()  # Clear the content of the view
        
    def logout(self) -> None:
        # Navigate to the login page
        self.root.show_page('Login')
        
    def update_clock(self) -> None:
        # Update the clock display on the main page
        current_time = time.strftime("%H:%M")  # Get the current time in HH:MM format
        self.view.canvas.itemconfig(self.view.clock, text=current_time)  # Update the clock display on the canvas
        self.view.canvas.after(1000, self.update_clock)  # Schedule the next update in 1000 milliseconds (1 second)

    def render(self):
        # Render the main page and start the clock update
        super().render()  # Call the parent render method
        self.update_clock()  # Start the clock update
        self.switch_page("dashboard")  # Switch to the dashboard page initially