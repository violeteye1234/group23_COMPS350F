# MVC Architecture Sequence Diagrams

## Model - class diagram

```plantuml
@startuml
skinparam classAttributeIconSize 0

' Defining Classes

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

' Defining relationships
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

User -> View: Enter your email address and password
View -> Controller: handle_login(email, password)
Controller -> DB: check_login_valid(email, password)
DB --> Controller: valid = true/false
alt valid
    Controller -> DB: get_user_info(email)
    DB --> Controller: user_info
    Controller -> UserModel: Initialize the User object
    Controller -> View: Navigate to the Dashboard Page
else
    Controller -> View: Display error message
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

User -> View: Enter registration information
View -> Controller: handle_registration(user_info)
Controller -> View: Validating input data
Controller -> DB: check_user_exists(email)
DB --> Controller: exists = true/false
alt not exists
    Controller -> DB: registration(user_info)
    Controller -> View: Display registration successful, navigate to the Login Page
else
    Controller -> View: Show user already exists error
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

User -> View: Open the Dashboard Page
View -> Controller: load_dashboard()
Controller -> UserModel: get_flights()
UserModel -> FlightModel: Get the user's flight list
FlightModel --> UserModel: flights_list
Controller -> UserModel: get_baggages()
UserModel -> BaggageModel: Get the user's luggage list
BaggageModel --> UserModel: baggages_list
Controller -> View: Display flight and baggage information
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
Controller -> View: Display company information and team members
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

User -> View: Open Help Page
View -> Controller: load_help_page()
Controller -> View: Show FAQ list
User -> View: Enter your search query
View -> Controller: handle_search(query)
Controller -> View: Show search results
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

User -> View: Open Profile Page
View -> Controller: load_profile_page()
Controller -> View: Display personal information and settings options
User -> View: Select "Personal Information" or "Notification Settings"
View -> Controller: navigate_to_selected_option(option)
Controller -> View: Navigate to the corresponding page
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

User -> View: Open Personal Information Page
View -> Controller: load_personal_information()
Controller -> UserModel: Get user information
UserModel --> Controller: user_info
Controller -> View: Display user information
User -> View: Click the "Edit" button
View -> Controller: handle_edit_personal_information()
Controller -> View: Enable Edit Mode
User -> View: Modify the information and click "Save"
View -> Controller: handle_save_personal_information(updated_info)
Controller -> UserModel: Update User Information
UserModel -> DB: update_data("users", updated_info)
Controller -> View: Display save success message
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

User -> View: Open Notification Setting Page
View -> Controller: load_notification_settings()
Controller -> UserModel: Get notification settings
UserModel --> Controller: settings
Controller -> View: Display current settings
User -> View: Toggle a notification setting
View -> Controller: handle_toggle_notification(setting_name, value)
Controller -> UserModel: Update notification settings
UserModel -> DB: update_data("notification_settings", {setting_name: value})
Controller -> View: Update display status
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

User -> View: Open Notification Center Page
View -> Controller: load_notifications()
Controller -> UserModel: Get user notifications
UserModel --> Controller: notifications_list
Controller -> View: Show Notification List
User -> View: Click on a notification
View -> Controller: handle_notification_click(notification_id)
Controller -> UserModel: Click on a notification
Controller -> View: Navigate to related content or display details
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

User -> View: Open Boarding Information Page
View -> Controller: load_boarding_information()
Controller -> UserModel: get_flights()
UserModel -> FlightModel: Get flight information
FlightModel --> UserModel: flights_list
Controller -> View: Display flight boarding information
User -> View: Click the "View Map" button
View -> Controller: handle_view_map(flight_number)
Controller -> View: Navigate to the Map Page
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

User -> View: Open My Flight Page
View -> Controller: load_my_flights()
Controller -> UserModel: get_flights()
UserModel -> FlightModel: Get flight list
FlightModel --> UserModel: flights_list
Controller -> View: Show flight list
User -> View: Click on the "go_detail_button" for a flight
View -> Controller: handle_go_detail(flight_number)
Controller -> View: Navigate to the Flight Detail Page
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

User -> View: Open My Baggage Page
View -> Controller: load_my_baggages()
Controller -> UserModel: get_baggages()
UserModel -> BaggageModel: Get baggage list
BaggageModel --> UserModel: baggages_list
Controller -> View: Show baggage list
User -> View: Enter your search query
View -> Controller: handle_search_baggage(query)
Controller -> View: Display the filtered baggage list
User -> View: Click on a bag "to_baggage_detail_page_button"
View -> Controller: handle_baggage_selection(baggage_id)
Controller -> View: Navigate to the Baggage Detail Page
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

User -> View: Open Flight Detail Page
View -> Controller: load_flight_detail(flight_number)
Controller -> FlightModel: Get flight details
FlightModel --> Controller: flight_details
Controller -> View: Display flight details and seat map
User -> View: Click the "Track My Baggage" button
View -> Controller: handle_track_my_baggage()
Controller -> View: Navigate to My Baggage Page
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

User -> View: Open Baggage Detail Page
View -> Controller: load_baggage_detail(baggage_id)
Controller -> BaggageModel: Get baggage details
BaggageModel --> Controller: baggage_details
Controller -> View: Display baggage information, current location and activity history
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

User -> View: Open Map Page
View -> Controller: load_map(target_location)
Controller -> UserModel: Get current_location
UserModel --> Controller: current_location
Controller -> FlightModel: Get target_location (such as boarding_gate location)
FlightModel --> Controller: target_location_info
Controller -> View: Displays a navigation map from current_location to target_location
@enduml
```

---