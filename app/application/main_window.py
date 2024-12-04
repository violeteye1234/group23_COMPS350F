import tkinter as tk
from typing import Any, Dict, Optional
from models.logger import get_logger
from utils.page_controller import PageController
from pages import LoginPageController, RegisterPageController, MainPageController, Login1PageController, ForgotPasswordPageController

class MainWindow(tk.Tk):
    def __init__(self, logger=get_logger(), *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs) 
        self.logger = logger
        self.logger.info("Initializing MainWindow")

        # Set Windows Properties
        self.geometry("1080x768")
        self.overrideredirect(True)
        self.resizable(True, True)
        self.wm_attributes('-transparentcolor', '#123456')

        # Initialize Variables
        self.hasstyle: bool = False
        self.dragging: bool = False
        self.now_alpha: float = 1.0
        self.database: Optional[Any] = None
        self.pages: Dict[str, PageController] = {}
        self.page_history: list[str] = []
        self.current_page_name: Optional[str] = None
        self._startx: int = 0
        self._starty: int = 0
        

        # Set up Container
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)

        # Initialize Pages
        self.init_pages()

        # Set up Application Window Style
        self.set_appwindow()

        # Binding Events
        self.bind('<ButtonPress-1>', self.start_move)
        self.bind('<ButtonRelease-1>', self.stop_move)
        self.bind('<B1-Motion>', self.on_move)
        self.bind('<Escape>', self.on_key)
    #Initialize different page controllers in a dictionary
    def init_pages(self):
        pages = {
            'Login': LoginPageController,
            'Register': RegisterPageController,
            'Main': MainPageController,
            'Login1': Login1PageController,
            'ForgotPassword': ForgotPasswordPageController
        }

        #loop through each page to create an instance of its controller
        for name, ControllerClass in pages.items():
            controller = ControllerClass(self, self.container)
            self.pages[name] = controller
            self.logger.info(f"Page '{name}' initialized.")

    def show_page(self, page_name: str, note_page: bool = True) -> None:
        #logs the action of showing a specific page
        self.logger.info(f"Showing page '{page_name}'.")
        if self.current_page_name and self.current_page_name in self.pages:
            self.pages[self.current_page_name].view.pack_forget()

        #set controller and render the new page
        self.page_controller = self.pages[page_name]
        self.page_controller.render()
        self.page_controller.view.pack(fill="both", expand=True)

        #update the current page name
        self.current_page_name = page_name

        if note_page and self.current_page_name:
            self.page_history.append(self.current_page_name)
            self.logger.debug(f"Added '{self.current_page_name}' to page history.")

    def login(self, id: str, password: str) -> None:
        #login attempt with the given ID
        self.logger.info(f"Login as {id}.")
        #Show main page after successful login
        self.show_page("Main")
        

    def is_pressed_top(self, event):
        #check to see if the mouse event occurred in the top area of the window for dragging
        return self.winfo_x() + self.winfo_width()-60 >= event.x_root >= self.winfo_x() and self.winfo_y() + 30 >= event.y_root >= self.winfo_y()

    def start_move(self, event: tk.Event) -> None:
        #Initiates the dragging of the window if the top area is pressed
        if self.is_pressed_top(event):
            self.dragging = True
            self._startx = event.x
            self._starty = event.y
            self.logger.info("Started dragging the window.")

    def stop_move(self, event: tk.Event) -> None:
        #stops the dragging of the window when the mouse is released
        if self.dragging:
            self.dragging = False
            self.logger.info("Stopped dragging the window.")

    def on_move(self, event: tk.Event) -> None:
        #updates the window postion while dragging
        if self.dragging:
            x = self.winfo_x() + event.x - self._startx
            y = self.winfo_y() + event.y - self._starty
            self.geometry(f'+{x}+{y}')
            self.logger.debug(f"Window moved to ({x}, {y}).")

    def on_key(self, event: tk.Event) -> None:
        #handling key pressed events, also closing the window when Escape key is pressed
        if event.keysym == "Escape":
            self.logger.info("Escape key pressed. Closing the window.")
            self.on_destroy()

    def on_destroy(self) -> None:
        #Logging the action of closing the window and quitting the application
        self.logger.info("Closing the window...")
        self.quit()

    def set_appwindow(self) -> None:
        #setting window style to be an application window
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
    #Initialising main window and showing the login page
    app = MainWindow()
    app.show_page('Login')
    app.mainloop()