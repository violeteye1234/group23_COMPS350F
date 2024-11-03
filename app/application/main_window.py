# main_window.py

import tkinter as tk
from typing import Any, Dict, Optional
from models.logger import get_logger
from pages.page_controller import PageController
from pages import LoginPageController, RegisterPageController, MainPageController

class MainWindow(tk.Tk):
    def __init__(self, logger = get_logger(), *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.logger = logger
        self.logger.info("Initializing MainWindow")

        # Set window properties
        self.geometry("800x600")
        self.overrideredirect(True)
        self.resizable(False, False)
        self.wm_attributes('-transparentcolor', '#123456')

        # Initialize variables
        self.hasstyle: bool = False
        self.dragging: bool = False
        self.now_alpha: float = 1.0
        self.database: Optional[Any] = None
        self.pages: Dict[str, PageController] = {}
        self.page_history: list[str] = []
        self.current_page_name: Optional[str] = None
        self._startx: int = 0
        self._starty: int = 0

        # Set up container
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # Initialize pages
        self.init_pages()

        # Set application window style
        self.set_appwindow()

        # Bind events
        self.bind('<ButtonPress-1>', self.start_move)
        self.bind('<ButtonRelease-1>', self.stop_move)
        self.bind('<B1-Motion>', self.on_move)
        self.bind('<Escape>', self.on_key)

    def init_pages(self):
        # Initialize the pages (controllers)
        pages = {
            'Login': LoginPageController,
            'Register': RegisterPageController,
            'Main': MainPageController
        }
        for name, ControllerClass in pages.items():
            controller = ControllerClass(self)
            self.pages[name] = controller
            self.logger.info(f"Page '{name}' initialized.")

    def show_page(self, page_name: str, note_page: bool = True) -> None:
        self.logger.info(f"Showing page '{page_name}'.")
        # Hide current page
        if self.current_page_name and self.current_page_name in self.pages:
            self.pages[self.current_page_name].view.pack_forget()

        # Show new page
        page_controller = self.pages[page_name]
        page_controller.render()
        self.current_page_name = page_name

        if note_page and self.current_page_name:
            self.page_history.append(self.current_page_name)
            self.logger.debug(f"Added '{self.current_page_name}' to page history.")

    def go_back(self) -> None:
        if self.page_history:
            previous_page = self.page_history.pop()
            self.show_page(previous_page, note_page=False)
            self.logger.info(f"Navigated back to page '{previous_page}'.")
        else:
            self.logger.warning("No page to go back to.")

    # Draggable window methods
    def start_move(self, event: tk.Event) -> None:
        self.dragging = True
        self._startx = event.x
        self._starty = event.y
        self.logger.info("Started dragging the window.")

    def stop_move(self, event: tk.Event) -> None:
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
            # Windows-specific code to set the window style
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
    app.show_page('Login')  # Start with the Login page
    app.mainloop()
