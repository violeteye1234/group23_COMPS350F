# main_window.py

import tkinter as tk
from typing import Any, Dict, Optional
from models.logger import get_logger
from utils.page_controller import PageController
from pages import LoginPageController, RegisterPageController, MainPageController, LoginGS_PageController

#testing
import unittest

class MainWindow(tk.Tk):
    def __init__(self, logger=get_logger(), *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs) 
        self.logger = logger
        self.logger.info("Initializing MainWindow")

        # 設置視窗屬性
        self.geometry("1080x768")
        self.overrideredirect(True)
        self.resizable(True, True)
        self.wm_attributes('-transparentcolor', '#123456')

        # 初始化變數
        self.hasstyle: bool = False
        self.dragging: bool = False
        self.now_alpha: float = 1.0
        self.database: Optional[Any] = None
        self.pages: Dict[str, PageController] = {}
        self.page_history: list[str] = []
        self.current_page_name: Optional[str] = None
        self._startx: int = 0
        self._starty: int = 0
        
        # Common Model
        # TODO: build a database model instance
        # TODO: build a user model instance

        # 設置容器
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)

        # 初始化頁面
        self.init_pages()

        # 設置應用程式視窗樣式
        self.set_appwindow()

        # 綁定事件
        self.bind('<ButtonPress-1>', self.start_move)
        self.bind('<ButtonRelease-1>', self.stop_move)
        self.bind('<B1-Motion>', self.on_move)
        self.bind('<Escape>', self.on_key)

    def init_pages(self):
        pages = {
            'Login': LoginPageController,
            'Register': RegisterPageController,
            'Main': MainPageController,
            'GS_login' : LoginGS_PageController
        }
        for name, ControllerClass in pages.items():
            controller = ControllerClass(self, self.container)
            self.pages[name] = controller
            self.logger.info(f"Page '{name}' initialized.")

    def show_page(self, page_name: str, note_page: bool = True) -> None:
        self.logger.info(f"Showing page '{page_name}'.")
        if self.current_page_name and self.current_page_name in self.pages:
            self.pages[self.current_page_name].view.pack_forget()

        page_controller = self.pages[page_name]
        page_controller.render()
        page_controller.view.pack(fill="both", expand=True)

        self.current_page_name = page_name

        if note_page and self.current_page_name:
            self.page_history.append(self.current_page_name)
            self.logger.debug(f"Added '{self.current_page_name}' to page history.")

    def login(self, id: str, password: str) -> None:
        self.logger.info(f"Login as {id}.")
        self.show_page("Main")

    def go_to_gs(self):
        self.show_page("GS_login")
        

    def is_pressed_top(self, event):
        return self.winfo_x() + self.winfo_width()-60 >= event.x_root >= self.winfo_x() and self.winfo_y() + 30 >= event.y_root >= self.winfo_y()

    def start_move(self, event: tk.Event) -> None:
        if self.is_pressed_top(event):
            self.dragging = True
            self._startx = event.x
            self._starty = event.y
            self.logger.info("Started dragging the window.")

    def stop_move(self, event: tk.Event) -> None:
        if self.dragging:
            self.dragging = False
            self.logger.info("Stopped dragging the window.")

    def on_move(self, event: tk.Event) -> None:
        if self.dragging:
            x = self.winfo_x() + event.x - self._startx
            y = self.winfo_y() + event.y - self._starty
            self.geometry(f'+{x}+{y}')
            self.logger.debug(f"Window moved to ({x}, {y}).")

    def on_key(self, event: tk.Event) -> None:
        if event.keysym == "Escape":
            self.logger.info("Escape key pressed. Closing the window.")
            self.on_destroy()

    def on_destroy(self) -> None:
        self.logger.info("Closing the window...")
        self.quit()

    def set_appwindow(self) -> None:
        try:
            import ctypes
            GWL_EXSTYLE = -20
            WS_EX_APPWINDOW = 0x00040000
            WS_EX_TOOLWINDOW = 0x00000080
            hwnd = ctypes.windll.user32.GetParent(self.winfo_id())
            style = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
            style = style & ~WS_EX_TOOLWINDOW
            style = style | WS_EX_APPWINDOW
            ctypes.windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, style)
            self.withdraw()
            self.after(10, self.wm_deiconify)
            self.logger.debug("Set application window style.")
        except Exception as e:
            self.logger.error(f"Failed to set app window style: {e}")

if __name__ == "__main__":
    app = MainWindow()
    app.show_page('Login')
    app.mainloop()