# MVC Architecture Sequence Diagrams

## Model - class diagram

```plantuml
@startuml
skinparam classAttributeIconSize 0

' 定义类

class User {
    - username: str
    - userID: str
    - email: str
    - userInfo: dict[str, any]
    - current_location: str
    --
    + get_flights(): list[Flight]
    + get_baggages(): list[Baggage]
}

class Database {
    - database
    --
    + check_login_valid(userID: str): bool
    + get_user_info(userID: str): dict[str, any]
    + get_flights(userID: str): list[Flight]
    + get_baggages(userID: str): list[Baggage]
    + registration(user_info: dict[str, any])
    + update_data(table: str, data: dict[str, any], condition: str)
    + set_database(filepath: str)
    + execute_sql(sql: str)
    + create_connection()
    + close_connection()
}

class Flight {
    - flight_number: str
    - departure_airport: Airport
    - arrival_airport: Airport
    - boarding_gate: BoardingGate
    - departure_time: datetime
    - arrival_time: datetime
    - status: str
    - last_update_time: datetime
    - airline: Airline
    - terminal: str
    - baggage_claim: str
    - aircraft_type: str
    - seat_map: Image
    - my_seat_number: str
    - my_seat_type: str
    - checkin_counter: str
    - checkin_counter_operating_hour: str
    --
    + get_my_seat_type(): str
    + get_flight_duration(): timedelta
    + update_status()
    + get_tracking_history(): list[dict[str, any]]
}

class Baggage {
    - baggage_id: str
    - flight_number: str
    - weight: float
    - status: str
    - last_update_time: datetime
    - pickup_time: datetime
    - last_scanned_location: str
    - destination_airport: Airport
    - departure_airport: Airport
    --
    + update_status()
}

class Airport {
    - short_code: str
    - full_name: str
    - city_name: str
}

class Airline {
    - name: str
    - logo: Image
}

class BoardingGate {
    - status: str
    - lineup_count: int
    - streaming_link: str
    - boarding_type: str
    --
    + update_status()
}

' 定义关系
User "1" --> "*" Flight : get_flights()
User "1" --> "*" Baggage : get_baggages()
Flight "1" --> "1" Airline
Flight "1" --> "1" BoardingGate
Flight "1" --> "1" Airport : departure_airport
Flight "1" --> "1" Airport : arrival_airport
Baggage "1" --> "1" Flight
Baggage "1" --> "1" Airport : departure_airport
Baggage "1" --> "1" Airport : destination_airport

@enduml
```

---

## 1. 登录页面（Login Page）

```plantuml
@startuml
title 登录页面（Login Page）

actor User
participant "LoginPageView" as View
participant "LoginPageController" as Controller
participant "Database" as DB
participant "User Model" as UserModel

User -> View: 输入邮箱和密码
View -> Controller: handle_login(email, password)
Controller -> DB: check_login_valid(email, password)
DB --> Controller: valid = true/false
alt valid
    Controller -> DB: get_user_info(email)
    DB --> Controller: user_info
    Controller -> UserModel: 初始化User对象
    Controller -> View: 导航到Dashboard Page
else
    Controller -> View: 显示错误信息
end
@enduml
```

---

## 2. 注册页面（Register Page）

```plantuml
@startuml
title 注册页面（Register Page）

actor User
participant "RegisterPageView" as View
participant "RegisterPageController" as Controller
participant "Database" as DB

User -> View: 输入注册信息
View -> Controller: handle_registration(user_info)
Controller -> View: 验证输入数据
Controller -> DB: check_user_exists(email)
DB --> Controller: exists = true/false
alt not exists
    Controller -> DB: registration(user_info)
    Controller -> View: 显示注册成功，导航到Login Page
else
    Controller -> View: 显示用户已存在错误
end
@enduml
```

---

## 3. 仪表板页面（Dashboard Page）

```plantuml
@startuml
title 仪表板页面（Dashboard Page）

actor User
participant "DashboardPageView" as View
participant "DashboardPageController" as Controller
participant "User Model" as UserModel
participant "Flight Model" as FlightModel
participant "Baggage Model" as BaggageModel

User -> View: 打开Dashboard Page
View -> Controller: load_dashboard()
Controller -> UserModel: get_flights()
UserModel -> FlightModel: 获取用户的航班列表
FlightModel --> UserModel: flights_list
Controller -> UserModel: get_baggages()
UserModel -> BaggageModel: 获取用户的行李列表
BaggageModel --> UserModel: baggages_list
Controller -> View: 显示航班和行李信息
@enduml
```

---

## 4. 关于我们页面（About Page）

```plantuml
@startuml
title 关于我们页面（About Page）

actor User
participant "AboutPageView" as View
participant "AboutPageController" as Controller

User -> View: 打开About Page
View -> Controller: load_about_page()
Controller -> View: 显示公司信息和团队成员
@enduml
```

---

## 5. 帮助页面（Help Page）

```plantuml
@startuml
title 帮助页面（Help Page）

actor User
participant "HelpPageView" as View
participant "HelpPageController" as Controller

User -> View: 打开Help Page
View -> Controller: load_help_page()
Controller -> View: 显示常见问题列表
User -> View: 输入搜索查询
View -> Controller: handle_search(query)
Controller -> View: 显示搜索结果
@enduml
```

---

## 6. 个人资料页面（Profile Page）

```plantuml
@startuml
title 个人资料页面（Profile Page）

actor User
participant "ProfilePageView" as View
participant "ProfilePageController" as Controller

User -> View: 打开Profile Page
View -> Controller: load_profile_page()
Controller -> View: 显示个人信息和设置选项
User -> View: 选择"个人信息"或"通知设置"
View -> Controller: navigate_to_selected_option(option)
Controller -> View: 导航到相应页面
@enduml
```

---

## 7. 个人信息页面（Personal Information Page）

```plantuml
@startuml
title 个人信息页面（Personal Information Page）

actor User
participant "PersonalInformationPageView" as View
participant "PersonalInformationPageController" as Controller
participant "User Model" as UserModel
participant "Database" as DB

User -> View: 打开Personal Information Page
View -> Controller: load_personal_information()
Controller -> UserModel: 获取用户信息
UserModel --> Controller: user_info
Controller -> View: 显示用户信息
User -> View: 点击"编辑"按钮
View -> Controller: handle_edit_personal_information()
Controller -> View: 启用编辑模式
User -> View: 修改信息并点击"保存"
View -> Controller: handle_save_personal_information(updated_info)
Controller -> UserModel: 更新用户信息
UserModel -> DB: update_data("users", updated_info)
Controller -> View: 显示保存成功消息
@enduml
```

---

## 8. 通知设置页面（Notification Setting Page）

```plantuml
@startuml
title 通知设置页面（Notification Setting Page）

actor User
participant "NotificationSettingPageView" as View
participant "NotificationSettingPageController" as Controller
participant "User Model" as UserModel
participant "Database" as DB

User -> View: 打开Notification Setting Page
View -> Controller: load_notification_settings()
Controller -> UserModel: 获取通知设置
UserModel --> Controller: settings
Controller -> View: 显示当前设置
User -> View: 切换某个通知设置
View -> Controller: handle_toggle_notification(setting_name, value)
Controller -> UserModel: 更新通知设置
UserModel -> DB: update_data("notification_settings", {setting_name: value})
Controller -> View: 更新显示状态
@enduml
```

---

## 9. 通知中心页面（Notification Center Page）

```plantuml
@startuml
title 通知中心页面（Notification Center Page）

actor User
participant "NotificationCenterPageView" as View
participant "NotificationCenterPageController" as Controller
participant "User Model" as UserModel

User -> View: 打开Notification Center Page
View -> Controller: load_notifications()
Controller -> UserModel: 获取用户通知
UserModel --> Controller: notifications_list
Controller -> View: 显示通知列表
User -> View: 点击某个通知
View -> Controller: handle_notification_click(notification_id)
Controller -> UserModel: 标记通知为已读
Controller -> View: 导航到相关内容或显示详情
@enduml
```

---

## 10. 登机信息页面（Boarding Information Page）

```plantuml
@startuml
title 登机信息页面（Boarding Information Page）

actor User
participant "BoardingInformationPageView" as View
participant "BoardingInformationPageController" as Controller
participant "User Model" as UserModel
participant "Flight Model" as FlightModel

User -> View: 打开Boarding Information Page
View -> Controller: load_boarding_information()
Controller -> UserModel: get_flights()
UserModel -> FlightModel: 获取航班信息
FlightModel --> UserModel: flights_list
Controller -> View: 显示航班登机信息
User -> View: 点击"查看地图"按钮
View -> Controller: handle_view_map(flight_number)
Controller -> View: 导航到Map Page
@enduml
```

---

## 11. 我的航班页面（My Flight Page）

```plantuml
@startuml
title 我的航班页面（My Flight Page）

actor User
participant "MyFlightPageView" as View
participant "MyFlightPageController" as Controller
participant "User Model" as UserModel
participant "Flight Model" as FlightModel

User -> View: 打开My Flight Page
View -> Controller: load_my_flights()
Controller -> UserModel: get_flights()
UserModel -> FlightModel: 获取航班列表
FlightModel --> UserModel: flights_list
Controller -> View: 显示航班列表
User -> View: 点击某个航班的"go_detail_button"
View -> Controller: handle_go_detail(flight_number)
Controller -> View: 导航到Flight Detail Page
@enduml
```

---

## 12. 我的行李页面（My Baggage Page）

```plantuml
@startuml
title 我的行李页面（My Baggage Page）

actor User
participant "MyBaggagePageView" as View
participant "MyBaggagePageController" as Controller
participant "User Model" as UserModel
participant "Baggage Model" as BaggageModel

User -> View: 打开My Baggage Page
View -> Controller: load_my_baggages()
Controller -> UserModel: get_baggages()
UserModel -> BaggageModel: 获取行李列表
BaggageModel --> UserModel: baggages_list
Controller -> View: 显示行李列表
User -> View: 输入搜索查询
View -> Controller: handle_search_baggage(query)
Controller -> View: 显示过滤后的行李列表
User -> View: 点击某个行李的"to_baggage_detail_page_button"
View -> Controller: handle_baggage_selection(baggage_id)
Controller -> View: 导航到Baggage Detail Page
@enduml
```

---

## 13. 航班详情页面（Flight Detail Page）

```plantuml
@startuml
title 航班详情页面（Flight Detail Page）

actor User
participant "FlightDetailPageView" as View
participant "FlightDetailPageController" as Controller
participant "Flight Model" as FlightModel

User -> View: 打开Flight Detail Page
View -> Controller: load_flight_detail(flight_number)
Controller -> FlightModel: 获取航班详情
FlightModel --> Controller: flight_details
Controller -> View: 显示航班详情和座位图
User -> View: 点击"Track My Baggage"按钮
View -> Controller: handle_track_my_baggage()
Controller -> View: 导航到My Baggage Page
@enduml
```

---

## 14. 行李详情页面（Baggage Detail Page）

```plantuml
@startuml
title 行李详情页面（Baggage Detail Page）

actor User
participant "BaggageDetailPageView" as View
participant "BaggageDetailPageController" as Controller
participant "Baggage Model" as BaggageModel

User -> View: 打开Baggage Detail Page
View -> Controller: load_baggage_detail(baggage_id)
Controller -> BaggageModel: 获取行李详情
BaggageModel --> Controller: baggage_details
Controller -> View: 显示行李信息、当前位置和活动历史
@enduml
```

---

## 15. 地图页面（Map Page）

```plantuml
@startuml
title 地图页面（Map Page）

actor User
participant "MapPageView" as View
participant "MapPageController" as Controller
participant "User Model" as UserModel
participant "Flight Model" as FlightModel

User -> View: 打开Map Page
View -> Controller: load_map(target_location)
Controller -> UserModel: 获取current_location
UserModel --> Controller: current_location
Controller -> FlightModel: 获取target_location（如boarding_gate位置）
FlightModel --> Controller: target_location_info
Controller -> View: 显示从current_location到target_location的导航地图
@enduml
```

---