from tkinter import ttk, messagebox
import tkinter as tk
from ctypes import windll
import time
from models.logger import get_logger

width_window = 800
height_window = 600
width_monitor = windll.user32.GetSystemMetrics(0)
height_monitor = windll.user32.GetSystemMetrics(1)

class DraggableWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = get_logger()
        self.logger.info("Initializing DraggableWindow")

        try:
            self.iconbitmap('icon.ico')
            self.logger.info("Icon set successfully.")
        except Exception as e:
            self.logger.error(f"Icon file not found: {e}")
        
        self.geometry(f'{width_window}x{height_window}+{int((width_monitor/2)-(width_window/2))}+{int((height_monitor/2)-(height_window/2))}')
        self.overrideredirect(True)
        self.resizable(False, False)
        self.wm_attributes('-transparentcolor', '#123456') 
        
        self.bind('<ButtonPress-1>', self.start_move)
        self.bind('<ButtonRelease-1>', self.stop_move)
        self.bind('<B1-Motion>', self.on_move)
        self.bind('<Escape>', self.on_key)
                    
        self.hasstyle = False
        self.dragging = False
        self.now_alpha = 1
        self.database = None
        
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        
        self.set_appwindow()
        # 如果 create_window_proc 是自定義方法，請確保其已定義或移除
        # self.create_window_proc()
        
        self.frame_history = []
        self.current_frame_name = None
        
        self.username = ""
        self.flights_that_user_booked_before = []

        self.style = ttk.Style()
        self.style.theme_create('custom_style', parent='alt', settings={
            'TCombobox': {
                'configure': {
                    'borderwidth': 0,
                    'padding': 0,
                    'highlightthickness': 0,
                    'selectbackground': 'white',
                    'selectforeground': 'black',
                },
            },
            'TCombobox::droparrow': {
                'configure': {
                    'padding': 0,
                    'width':0,
                    'height':0
                },
            },
        })
        self.style.theme_use('custom_style')

    def execute_sql(self, command):
        if self.database is None:
            self.logger.error("Database is not set.")
            return -1
        with self.database.cursor() as cur:
            try:
                self.logger.debug(f"Executing SQL command: {command}")
                cur.execute(command)
                if command.strip().upper().startswith("SELECT"):
                    results = cur.fetchall()
                else:
                    results = 1
                self.database.commit()
                self.logger.info("SQL command executed successfully.")
                return results
            except Exception as e:
                error_code = e.args[0] if len(e.args) > 0 else 'Unknown'
                self.logger.error(f"SQL execution error: {e}")
                if error_code == '24000':
                    self.logger.warning("Integrity constraint violation.")
                elif error_code == '23000':
                    self.logger.warning("Integrity constraint violation.")
                else:
                    messagebox.showerror("Unexpected Error", str(e))
                self.logger.error(f"({error_code}, {command}).")
                return -1      

    def disappear(self, speed):
        def fade_out():
            if self.now_alpha > 0:
                self.now_alpha = max(self.now_alpha - speed, 0)
                self.attributes('-alpha', self.now_alpha)
                self.after(10, fade_out)
        self.logger.debug("Starting fade out.")
        fade_out()
                
    def appear(self, speed):
        def fade_in():
            if self.now_alpha < 1:
                self.now_alpha = min(self.now_alpha + speed, 1)
                self.attributes('-alpha', self.now_alpha)
                self.after(10, fade_in)
        self.logger.debug("Starting fade in.")
        fade_in()
                
    def is_pressed_top_bar(self, event):
        # 修正鼠標位置判斷邏輯
        x_root = self.winfo_rootx()
        y_root = self.winfo_rooty()
        width = self.winfo_width()
        height = 30  # 假設頂部 30 像素為拖動區域
        pressed = y_root <= event.y_root <= y_root + height and x_root <= event.x_root <= x_root + width
        self.logger.debug(f"is_pressed_top_bar: {pressed}")
        return pressed
    
    def start_move(self, event):
        if self.is_pressed_top_bar(event):
            self.dragging = True
            self._startx = event.x
            self._starty = event.y
            self.logger.info("Started dragging the window.")
    
    def stop_move(self, event):
        if self.dragging:
            self.dragging = False
            self.logger.info("Stopped dragging the window.")
    
    def on_move(self, event):
        if self.dragging:
            x = self.winfo_x() + event.x - self._startx
            y = self.winfo_y() + event.y - self._starty
            self.geometry(f'+{x}+{y}')
            self.logger.debug(f"Window moved to ({x}, {y}).")
    
    def on_key(self, event):
        if event.keysym == "Escape":
            self.logger.info("Escape key pressed. Closing the window.")
            self.on_destroy()
    
    def on_destroy(self):
        self.logger.info("Closing the window...")
        self.disappear(0.025)
        # 延遲關閉以完成淡出效果
        self.after(250, self.quit)
    
    def on_minimize(self, hide=False):
        self.logger.info("Minimizing the window.")
        self.disappear(0.05)
        hwnd = windll.user32.GetParent(self.winfo_id())
        windll.user32.ShowWindow(hwnd, 0 if hide else 6)
    
    def on_restore(self):
        self.logger.info("Restoring the window.")
        self.after(100, lambda: self.appear(0.05))
    
    def set_appwindow(self):
        GWL_EXSTYLE = -20
        WS_EX_APPWINDOW = 0x00040000
        WS_EX_TOOLWINDOW = 0x00000080
        if not self.hasstyle:
            hwnd = windll.user32.GetParent(self.winfo_id())
            style = windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
            style = style & ~WS_EX_TOOLWINDOW
            style = style | WS_EX_APPWINDOW
            res = windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, style)
            self.withdraw()
            self.after(10, lambda: self.wm_deiconify())
            self.hasstyle = True
            self.logger.debug("Set application window style.")
    
    def set_database(self, database):
        self.database = database
        self.logger.info("Database connection set.")
    
    def add_frame(self, frame_name, frame_class):
        self.frames[frame_name] = frame_class(parent=self.container, controller=self)
        self.frames[frame_name].grid(row=0, column=0, sticky="nsew")
        self.logger.info(f"Frame '{frame_name}' added.")
   
    def show_frame(self, page_name, note_frame=True):
        self.logger.info(f"Showing frame '{page_name}'.")
        self.disappear(0.15)
        try:
            if hasattr(self.frames[page_name], 'page_update'):
                self.frames[page_name].page_update()
                self.logger.debug(f"Page '{page_name}' updated.")
        except Exception as e:
            self.logger.error(f"Error updating page '{page_name}': {e}")
        self.frames[page_name].tkraise()
        self.after(100, lambda: self.appear(0.3))
        
        if note_frame and self.current_frame_name:
            self.frame_history.append(self.current_frame_name)
            self.logger.debug(f"Added '{self.current_frame_name}' to frame history.")
        self.current_frame_name = page_name
        
        self.logger.info(f"<{page_name}> is now on top.")
    
    def go_back(self):
        if self.frame_history:
            previous_frame = self.frame_history.pop()
            self.show_frame(previous_frame, note_frame=False)
            self.logger.info(f"Navigated back to frame '{previous_frame}'.")
        else:
            self.logger.warning("No frame to go back to.")
