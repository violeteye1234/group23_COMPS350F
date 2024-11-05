import os

# 定義目錄和文件結構
structure = {
    'application': {
        'models': [
            '__init__.py',
            'user.py',
            'flight.py',
            'baggage.py',
            'notification.py',
            'database.py'
        ],
        'pages': {
            '__init__.py': '',
            'login': {
                'login_view.py': '',
                'login_controller.py': '',
                'images': []
            },
            'register': {
                'register_view.py': '',
                'register_controller.py': '',
                'images': []
            },
            'dashboard': {
                'dashboard_view.py': '',
                'dashboard_controller.py': '',
                'images': []
            },
            'about': {
                'about_view.py': '',
                'about_controller.py': '',
                'images': []
            },
            'help': {
                'help_view.py': '',
                'help_controller.py': '',
                'images': []
            },
            'profile': {
                'profile_view.py': '',
                'profile_controller.py': '',
                'images': []
            },
            'personal_information': {
                'personal_information_view.py': '',
                'personal_information_controller.py': '',
                'images': []
            },
            'notification_setting': {
                'notification_setting_view.py': '',
                'notification_setting_controller.py': '',
                'images': []
            },
            'notification_center': {
                'notification_center_view.py': '',
                'notification_center_controller.py': '',
                'images': []
            },
            'boarding_information': {
                'boarding_information_view.py': '',
                'boarding_information_controller.py': '',
                'images': []
            },
            'my_flight': {
                'my_flight_view.py': '',
                'my_flight_controller.py': '',
                'images': []
            },
            'my_baggage': {
                'my_baggage_view.py': '',
                'my_baggage_controller.py': '',
                'images': []
            },
            'flight_detail': {
                'flight_detail_view.py': '',
                'flight_detail_controller.py': '',
                'images': []
            },
            'baggage_detail': {
                'baggage_detail_view.py': '',
                'baggage_detail_controller.py': '',
                'images': []
            },
            'map': {
                'map_view.py': '',
                'map_controller.py': '',
                'images': []
            }
        }
    },
    'app.py': '',
    'config.py': '',
    'requirements.txt': '',
    'README.md': ''
}


def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            # 如果是字典，則為目錄
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        elif isinstance(content, list):
            # 如果是列表，則為目錄，列表內為文件
            os.makedirs(path, exist_ok=True)
            for file_name in content:
                file_path = os.path.join(path, file_name)
                with open(file_path, 'w', encoding='utf-8') as f:
                    pass  # 創建空文件
        else:
            # 否則為文件
            with open(path, 'w', encoding='utf-8') as f:
                pass  # 創建空文件

if __name__ == '__main__':
    base_directory = r'./coding_part'  # 可以更改為您想要的基礎目錄
    create_structure(base_directory, structure)
    print("文件夾和文件已成功創建。")
