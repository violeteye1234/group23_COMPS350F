# main_page_controller.py
from pages.home_page_controller import HomePageController
from pages.settings_page_controller import SettingsPageController
import tkinter as tk

class MainPageController:
    def __init__(self, view, model):
        self.view = view  # MainPageView 實例
        self.model = model  # MainPageModel 實例
        self.current_content_controller = None
        self.view.controller = self  # 設置 View 的 Controller 引用
        self.view.render()

    def switch_page(self, page_name):
        # 1. 清理當前頁面
        if self.current_content_controller:
            self.current_content_controller.cleanup()
            self.view.clear_content()

        # 2. 實例化新頁面的 Controller
        if page_name == "Home":
            self.current_content_controller = HomePageController(self.view.content_frame, self.model)
        elif page_name == "Settings":
            self.current_content_controller = SettingsPageController(self.view.content_frame, self.model)
        else:
            print(f"Unknown page: {page_name}")
            return

        # 3. 渲染新頁面
        self.current_content_controller.render()

    def clean_content(self):
        if self.current_content_controller:
            self.current_content_controller.cleanup()
            self.current_content_controller = None
            self.view.clear_content()