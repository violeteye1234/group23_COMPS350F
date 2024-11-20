from utils.page_controller import PageController
from .notification_center_view import NotificationCenterPageView
from pages.my_baggage.my_baggage_controller import MyBaggagePageController
from datetime import datetime, timedelta

class NotificationCenterPageController(PageController):
    def __init__(self, root, parent_container):
        super().__init__(root, parent_container)
        self.root = root
        self.view = NotificationCenterPageView(parent_container)
        self.view_set_controller()

        # 假设飞机起飞时间和降落时间
        takeoff_time = datetime.strptime("23:00", "%H:%M")
        landing_time = datetime.strptime("23:59", "%H:%M")
        
        current_time = datetime.now()
        current_time = current_time.strftime("%H:%M")

        one_hour_ago = takeoff_time - timedelta(minutes=60)  # 行李检查 飞机起飞前一小时
        half_hour_ago = takeoff_time - timedelta(minutes=30)  # 登机 飞机起飞前半小时
        a_quarter_later = landing_time + timedelta(minutes=15)  # 行李到达 飞机降落后15分钟

        current_time_obj = datetime.strptime(current_time, "%H:%M")
        time_until_takeoff = (takeoff_time - current_time_obj).total_seconds() / 60
        time_later_landing = (current_time_obj - landing_time).total_seconds() / 60

        takeoff_time = takeoff_time.strftime("%H:%M")
        landing_time = landing_time.strftime("%H:%M")
        one_hour_ago = one_hour_ago.strftime("%H:%M")
        half_hour_ago = half_hour_ago.strftime("%H:%M")
        a_quarter_later= a_quarter_later.strftime("%H:%M")

        # 将时间显示在控制器中
        self.current_time = current_time
        self.half_hour_ago = half_hour_ago
        self.a_quarter_later = a_quarter_later
        self.one_hour_ago = one_hour_ago
        self.takeoff_time = takeoff_time
        self.landing_time = landing_time
        self.time_until_takeoff = time_until_takeoff
        self.time_later_landing = time_later_landing