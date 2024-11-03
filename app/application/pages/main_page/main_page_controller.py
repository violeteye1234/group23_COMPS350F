# main_page_controller.py
from pages.page_controller import PageController
from .main_page_view import MainPageView

class MainPageController(PageController):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.view = MainPageView(root)  # MainPageView 實例
        self.current_content_controller = None
        self.view_set_controller()  # 設置 View 的 Controller 引用
        self.view.render()

    def switch_page(self, page_name):
        # 1. 清理當前頁面
        if self.current_content_controller:
            self.current_content_controller.cleanup()
            self.view.clear_content()

        # 2. 實例化新頁面的 Controller
        # if page_name == "Home":
        #     self.current_content_controller = HomePageController(self.view.content_frame, self.model)
        # elif page_name == "Settings":
        #     self.current_content_controller = SettingsPageController(self.view.content_frame, self.model)
        # else:
        #     print(f"Unknown page: {page_name}")
        #     return

        # 3. 渲染新頁面
        self.current_content_controller.render()

    def clean_content(self):
        if self.current_content_controller:
            self.current_content_controller.cleanup()
            self.current_content_controller = None
            self.view.clear_content()