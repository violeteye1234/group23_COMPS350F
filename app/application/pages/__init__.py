# pages/__init__.py

from .about.about_controller import AboutPageController
from .baggage_detail.baggage_detail_controller import BaggageDetailPageController
from .boarding_information.boarding_information_controller import BoardingInformationPageController
from .dashboard.dashboard_controller import DashboardPageController
from .flight_detail.flight_detail_controller import FlightDetailPageController
from .help.help_controller import HelpPageController
from .login.login_controller import LoginPageController
from .main_page.main_page_controller import MainPageController
from .map.map_controller import MapPageController
from .my_baggage.my_baggage_controller import MyBaggagePageController
from .my_flight.my_flight_controller import MyFlightPageController
from .notification_center.notification_center_controller import NotificationCenterPageController
from .notification_setting.notification_setting_controller import NotificationSettingPageController
from .personal_information.personal_information_controller import PersonalInformationPageController
from .profile.profile_controller import ProfilePageController
from .register.register_controller import RegisterPageController
from .side_bar.sidebar_controller import SideBarController
from .topbar.topbar_controller import TopbarController

from .about.about_view import AboutPageView
from .baggage_detail.baggage_detail_view import BaggageDetailPageView
from .boarding_information.boarding_information_view import BoardingInformationPageView
from .dashboard.dashboard_view import DashboardPageView
from .flight_detail.flight_detail_view import FlightDetailPageView
from .help.help_view import HelpPageView
from .login.login_view import LoginPageView
from .main_page.main_page_view import MainPageView
from .map.map_view import MapPageView
from .my_baggage.my_baggage_view import MyBaggagePageView
from .my_flight.my_flight_view import MyFlightPageView
from .notification_center.notification_center_view import NotificationCenterPageView
from .notification_setting.notification_setting_view import NotificationSettingPageView
from .personal_information.personal_information_view import PersonalInformationPageView
from .profile.profile_view import ProfilePageView
from .register.register_view import RegisterPageView
from .side_bar.sidebar_view import SideBarView
from .topbar.topbar_view import TopbarView

__all__ = [
    'AboutPageController',
    'BaggageDetailPageController',
    'BoardingInformationPageController',
    'DashboardPageController',
    'FlightDetailPageController',
    'HelpPageController',
    'LoginPageController',
    'MainPageController',
    'MapPageController',
    'MyBaggagePageController',
    'MyFlightPageController',
    'NotificationCenterPageController',
    'NotificationSettingPageController',
    'PersonalInformationPageController',
    'ProfilePageController',
    'RegisterPageController',
    'SideBarController',
    'TopbarController',
    'BasePage',
    'AboutPageView',
    'BaggageDetailPageView',
    'BoardingInformationPageView',
    'DashboardPageView',
    'FlightDetailPageView',
    'HelpPageView',
    'LoginPageView',
    'MainPageView',
    'MapPageView',
    'MyBaggagePageView',
    'MyFlightPageView',
    'NotificationCenterPageView',
    'NotificationSettingPageView',
    'PersonalInformationPageView',
    'ProfilePageView',
    'RegisterPageView',
    'SideBarView',
    'TopbarView'
]
