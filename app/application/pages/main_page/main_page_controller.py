# main_page_controller.py
from utils.page_controller import PageController
from .main_page_view import MainPageView
from pages.about.about_controller import AboutPageController
from pages.baggage_detail.baggage_detail_controller import BaggageDetailPageController
from pages.boarding_information.boarding_information_controller import BoardingInformationPageController
from pages.dashboard.dashboard_controller import DashboardPageController
from pages.flight_detail.flight_detail_controller import FlightDetailPageController
from pages.help.help_controller import HelpPageController
from pages.login.login_controller import LoginPageController
from pages.map.map_controller import MapPageController
from pages.my_baggage.my_baggage_controller import MyBaggagePageController
from pages.my_flight.my_flight_controller import MyFlightPageController
from pages.notification_center.notification_center_controller import NotificationCenterPageController
from pages.notification_setting.notification_setting_controller import NotificationSettingPageController
from pages.personal_information.personal_information_controller import PersonalInformationPageController
from pages.profile.profile_controller import ProfilePageController
from pages.register.register_controller import RegisterPageController
import time

class MainPageController(PageController):
    def __init__(self, root, parent_container = None):
        super().__init__(root, parent_container)
        self.root = root
        self.view = MainPageView(root.container)
        self.current_content_controller = None
        self.view_set_controller()
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
        if self.current_content_controller:
            self.current_content_controller.cleanup()
        
        self.current_content_controller = self.pages[page_name](self.root, self.view.content_frame)
        
        self.current_content_controller.render()
        self.root.logger.info(f"Showing page {page_name}")


    def clean_content(self):
        if self.current_content_controller:
            self.current_content_controller.cleanup()
            self.current_content_controller = None
            self.view.clear_content()
        
    def logout(self) -> None:
        self.root.show_page('Login')
        
    def update_clock(self) -> None:
        current_time = time.strftime("%H:%M")
        self.view.canvas.itemconfig(self.view.clock, text=current_time) # type: ignore
        self.view.canvas.after(1000, self.update_clock) # type: ignore

    def render(self):
        super().render()
        self.update_clock()
        self.switch_page("dashboard")
