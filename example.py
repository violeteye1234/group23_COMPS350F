# ------------------------------------------------------- Library --------------------------------------------------------
from tkinter import Tk, Canvas, Entry, Text, Button, Checkbutton, IntVar, messagebox, Label, Listbox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from termcolor import colored, cprint
from screeninfo import get_monitors
from PIL.ImageTk import PhotoImage
from tkinter.ttk import Combobox
import matplotlib.pyplot as plt
from ctypes import wintypes
from pprint import pprint
from ctypes import windll
from faker import Faker
from tkinter import ttk
import tkinter as tk
import numpy as np
import pypyodbc
import datetime
import win32gui
import win32con
import datetime
import random
import ctypes
import shutil
import time
import json
import os

# -------------------------------------------------------- Config --------------------------------------------------------
now = datetime.datetime.now()
fake = Faker()
width_window = 1440
heigth_window = 1024
width_monitor = get_monitors()[0].width
height_monitor = get_monitors()[0].height
printing_adjust = 50

with open("./assets/json/data_preset.json", encoding="utf-8") as f:
    preset = json.load(f)
with open('./assets/json/table.json', encoding="utf-8") as f:
    table = json.load(f)
table_structure = table['table_structure']
table_default_data = table['table_default_data']
airports = table_default_data['Airport']
airports_revers = {ii[0]:i for i in airports.keys() for ii in airports[i]}
# --------------------------------------------------- Useful Function ----------------------------------------------------
def print_text(text, start="", flush=False, end="\n", state=""):
    elapsed_time = datetime.datetime.now() - now
    total_seconds = int(elapsed_time.total_seconds())
    milliseconds = elapsed_time.microseconds // 1000
    minutes, seconds = divmod(total_seconds, 60)
    time_now = f"{minutes:02d}:{seconds:02d}.{milliseconds:03d}"
    time_now = colored(time_now, 'red', attrs=['blink'])
    if state == "error":
        state = "Error"
    elif state == "sql":
        state = "Execute"
    elif state == "window":
        state = "Window"
    elif state == "sys":
        state = "System"
    elif state == "in":
        state = "Input"

    print(f"{start}[{time_now}]|[{state:-^8}]: {text}", flush=flush, end=end)

def print_process(title, process, flush = False, end = ""):
    if show_process:
        print_text(f"{title:<{printing_adjust}}{process}", start="\r", flush = flush, end=end)

# ------------------------------------------------------- Database -------------------------------------------------------

def create_conn_pool():
    pypyodbc.pooling = True

def get_conn(constr):
    return pypyodbc.connect(constr)

def close_conn(conn):
    conn.close()

def execute_sql(database, command, params=None):
    with database.cursor() as cur:
        try:
            if params:
                cur.execute(command, params)  # Prepared statement
            else:
                cur.execute(command)
            database.commit()
            return 1
        except Exception as e:
            database.rollback()
            if e.args[0] == "42S01":
                print(". Already exists.")
            elif e.args[0] == "42000":
                print(". Syntax error.")
                print(f"\n\t{e}")
            else:
                print(f"\n\t{e}")
            print(f"\t{command}\n")
            return 0

def get_database(database_path):
    constr = f"DRIVER={{Microsoft Access Driver (*.mdb, *.accdb)}};DBQ={database_path};"
    create_conn_pool()
    database = get_conn(constr)
    print_text(f"{f'Database connected':<{printing_adjust}}", state="sys")
    return database

# -------------------------------------------------------- Class ---------------------------------------------------------
class DraggableWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.iconbitmap('icon.ico')
        self.geometry(f'{width_window}x{heigth_window}+{int((width_monitor/2)-(width_window/2))}+{int((height_monitor/2)-(heigth_window/2))}')
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
        self.create_window_proc()
        
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
        with self.database.cursor() as cur:
            try:
                print_text(command, state="sql")
                cur.execute(command)
                if command.strip().upper().startswith("SELECT"):
                    results = cur.fetchall()
                else:
                    results = 1
                database.commit()
                return results
            except Exception as e:
                error_code = e.args[0]
                print_text(e, state="error")
                if error_code == '24000':
                    pass
                elif error_code == '23000':
                    pass
                else:
                    messagebox.showerror("Unexpected Error", e)
                print_text(f"({error_code}, {command}).", state="error")
                return -1      
    
    def disappear(self, speed):
        while(self.now_alpha > 0):
            self.attributes('-alpha', self.now_alpha-speed)
            self.now_alpha -= speed
            time.sleep(0.01)
            
    def appear(self, speed):
        while(self.now_alpha < 1):
            self.attributes('-alpha', self.now_alpha+speed)
            self.now_alpha += speed
            time.sleep(0.01)
            
    def is_pressed_top_bar(self, event):
        return self.winfo_x() + self.winfo_width()-60 >= event.x_root >= self.winfo_x() and self.winfo_y() + 30 >= event.y_root >= self.winfo_y()

    def start_move(self, event):
        if self.is_pressed_top_bar(event):
            self.dragging = True
            self._startx = event.x
            self._starty = event.y

    def stop_move(self, event):
        self.dragging = False

    def on_move(self, event):
        if self.dragging:
            x = self.winfo_x() + event.x - self._startx
            y = self.winfo_y() + event.y - self._starty
            self.geometry(f'+{x}+{y}')

    def on_key(self, event):
        if event.keysym == "Escape":
            self.on_destroy()

    def on_destroy(self):
        print_text("Closing the window...", state="window")
        self.disappear(0.025)
        self.quit()

    def on_minimize(self, hide=False):
        self.disappear(0.05)
        hwnd = windll.user32.GetParent(self.winfo_id())
        windll.user32.ShowWindow(hwnd, 0 if hide else 6)

    def on_restore(self):
        self.after(100, self.appear, 0.05)

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

    def set_database(self, database):
        self.database = database

    def add_frame(self, frame_name, frame_class):
        self.frames[frame_name] = frame_class(parent=self.container, controller=self)
        self.frames[frame_name].grid(row=0, column=0, sticky="nsew")
   
    def show_frame(self, page_name, note_frame = True):
        self.disappear(0.15)
        try:
            self.frames[page_name].page_update()
        except Exception as e:
            print_text(e, state="error")
        self.frames[page_name].tkraise()
        self.after(100, self.appear, 0.3)
        
        if note_frame:
            self.frame_history.append(self.current_frame_name)
        self.current_frame_name = page_name
        
        print_text(f"<{page_name}> now on the top.", state="window")

    def go_back(self):
        self.show_frame(self.frame_history[-1], note_frame = False)
        self.frame_history.pop()

    def login(self, username, password, is_admin):
        if username == "" or password == "":
            print_text("Username and Password are empty.", state="error")
            messagebox.showerror("You shell not pass.", "Username and Password should be filled.")
            return
        
        if is_admin:
            command = f"SELECT admin_id, password FROM Admin WHERE admin_id='{username}' AND password='{password}';"
        else:
            command = f"SELECT user_id, password FROM Customer WHERE user_id='{username}' AND password='{password}';"
        
        result = self.execute_sql(command)
        if result == "error":
            return

        if (username, password) in result:#1:#
            print_text("Login successfully.", state="sys")
            self.username = username
            if is_admin:
                self.show_frame("admin_main")
            else:
                print_text("Mark this record to login history table...", state="sys")
                self.execute_sql(f"INSERT INTO LoginHistory (login_date, ip_address, user_ID) VALUES (#{datetime.datetime.now().strftime('%m-%d-%Y')}#, '{fake.ipv4()}', '{username}');")
                self.show_frame("customer_main")
                
        else:
            print_text("Login Failed.", state="sys")
            print_text("Invalid username or password.", state="error")
            messagebox.showerror("You shell not pass.", "Invalid username or password.")
    
    def user_data_init(self):
        self.controller.flights_that_user_booked_before = None

    def update_flights_that_user_booked_before(self):
        self.flights_that_user_booked_before = []
        flight_ids = self.execute_sql(f"select flight_ID from Booking where user_ID = '{self.username}';")
        for flight_id in flight_ids:
            self.flights_that_user_booked_before.append(self.execute_sql(f"select * from Flight where flight_ID = {flight_id[0]};"))
        
    def create_window_proc(self):
        class WINDOWPOS(ctypes.Structure):
            _fields_ = [
                ('hwnd', wintypes.HWND), 
                ('hwndInsertAfter', wintypes.HWND), 
                ('x', ctypes.c_int), 
                ('y', ctypes.c_int), 
                ('cx', ctypes.c_int), 
                ('cy', ctypes.c_int), 
                ('flags', ctypes.c_uint), 
            ]

        def window_proc(hwnd, msg, wParam, lParam):
            if msg == win32con.WM_WINDOWPOSCHANGED:
                wp = ctypes.cast(lParam, ctypes.POINTER(WINDOWPOS)).contents
                if wp.flags & win32con.SWP_SHOWWINDOW:
                    self.on_restore()
            elif msg == win32con.WM_CLOSE:
                self.destroy()
            return win32gui.CallWindowProc(self.old_window_proc, hwnd, msg, wParam, lParam)

        self.old_window_proc = win32gui.SetWindowLong(self.winfo_id(), win32con.GWL_WNDPROC, window_proc)

class AdminTablePageWithInputs(tk.Frame):
    def __init__(self, parent, controller, img_path):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        self.canvas = tk.Canvas(self, height=heigth_window, width=width_window, bd=0, highlightthickness=0, relief="ridge", bg="#525252")
        self.canvas.pack()
        self.path_to_images = img_path
        self.image_image_1 = PhotoImage(file=self.path_to_images + "image_1.png")
        self.image_image_2 = PhotoImage(file=self.path_to_images + "image_2.png")
        self.image_image_3 = PhotoImage(file=self.path_to_images + "image_3.png")
        self.image_image_4 = PhotoImage(file=self.path_to_images + "image_4.png")
        image_1 = self.canvas.create_image(600, 500, image=self.image_image_1)
        image_2 = self.canvas.create_image(720.0, 15.0, image=self.image_image_2)
        image_3 = self.canvas.create_image(188.0, 15.0, image=self.image_image_3)
        image_4 = self.canvas.create_image(725.0, 635.0, image=self.image_image_4)
        self.canvas_outline_image = PhotoImage(file="./assets/img/common/outline.png")
        self.canvas.create_image(721, 512, image=self.canvas_outline_image)
        button_1 = CanvasButton(self.canvas, 1410.0,  3.0, self.path_to_images + "button_1.png", command = lambda: self.controller.on_destroy() )
        button_2 = CanvasButton(self.canvas, 1374.0,  3.0, self.path_to_images + "button_2.png", command = lambda: self.controller.on_minimize())
        button_3 = CanvasButton(self.canvas,   50.0, 38.0, self.path_to_images + "button_3.png", command = lambda: self.controller.show_frame("admin_main"))
        button_4 = CanvasButton(self.canvas, 1205.0, 78.0, self.path_to_images + "button_4.png", command = lambda: self.controller.go_back())
        button_5 = CanvasButton(self.canvas,  956.0, 78.0, self.path_to_images + "button_5.png", command = lambda: self.controller.show_frame("admin_database"))
        
        self.result_background_image = PhotoImage(file="./assets/img/common/admin_result_background.png")
        result_background = self.canvas.create_image(575+self.result_background_image.width()/2, 280+self.result_background_image.height()/2, image=self.result_background_image)
        self.result_canvas = tk.Canvas(self.canvas, height=700, width=900, bd=0, highlightthickness=0, relief="ridge", bg="#ffffff")
        self.result_canvas.place(x=475, y=280)
        self.result_listbox = Listbox(self.result_canvas, width = 800, height=700, font=("Courier", 10, "bold"))
        self.result_listbox.bind('<<ListboxSelect>>', self.on_select)
        self.result_listbox.place(x=0, y=0)
        self.selection = ""
        
        self.input_labels = []
        self.input_entries = []
        self.input_vars = []

        self.buttons = []
        
        self.input_x = 100
        self.input_y = 275
        
        self.table_name = ""
    
    def on_select(self,event):
        w = event.widget
        try:
            self.selection_index = int(w.curselection()[0])
            self.selection = [i.strip() for i in w.get(self.selection_index).split("|")]
        except Exception as e:
            print_text(e, state="error")
        print_text(f'Selected: {self.selection}', state="in")

    def search(self, command):
        self.result_listbox.delete(0, tk.END)
        result = self.controller.execute_sql(command)
        result_max_lengths = [max([len(str(i)) for i in col]) for col in zip(*result)]
        for data in result:
            self.result_listbox.insert(tk.END, "  "+" | ".join([f"{str(i if not isinstance(i, datetime.datetime) else i.strftime('%d/%m/%Y %H:%M:%S')):^{length}}" for i, length in zip(data, result_max_lengths)]))


    def add_input(self, label_text, x, y):
        label = tk.Label(self, text=label_text)
        label.place(x=x, y=y)
        self.input_labels.append(label)

        var = tk.StringVar()
        entry = tk.Entry(self, textvariable=var, width=10)
        entry.place(x=x + 200, y=y)
        self.input_entries.append(entry)
        self.input_vars.append(var)
        
    def add_inputs(self, label_texts):
        for label_text in label_texts:
            self.add_input(label_text, self.input_x, self.input_y)
            self.input_y += 40

    def add_buttons(self, button_texts, commands):
        for i, text in enumerate(button_texts):
            button = tk.Button(self, text=text, command=commands[i], bg="#aaaaaa")
            button.place(x=self.input_x, y=self.input_y)
            self.input_y+=50
            self.buttons.append(button)
    
    def get_inputs(self, add_name = False):
        input_info = [i.get() for i in self.input_vars]
        
        args = self.get_args_formatted(input_info, add_name = add_name)
                
        return input_info, args

    def get_args_formatted(self, data, add_name = False):
        args = []
        for data, its_type, name in zip(data, self.args_type, self.args_name):
            if data != "":
                data = f"""{name+" =" if add_name else ""} {"#" if its_type == "DATE" else ""}{"'" if its_type == "TEXT" else ""}{data}{"'" if its_type == "TEXT" else ""}{"#" if its_type == "DATE" else ""}"""
                args.append(data)
                
        return args
    
    def table_setup(self, table_name):
        self.table_name = table_name
        self.args_type = [i[1] for i in table_structure[self.table_name]]
        self.args_name = [i[0] for i in table_structure[self.table_name]]
    
    def search_data(self):
        input_info, args = self.get_inputs(add_name = True)
        command = f"select * from {self.table_name}" + ("" if sum([len(i) for i in input_info]) == 0 else " where ") + " and ".join(args) + ";"
        self.search(command)
    
    def insert_data(self):
        input_info, args = self.get_inputs()
        command = f"Insert into {self.table_name}(" + ", ".join([name for info,name in zip(input_info,self.args_name) if len(info) > 0]) + f") values ({', '.join(args)});"
        self.controller.execute_sql(command)

class CanvasButton:
    flash_delay = 100  # Milliseconds.

    def __init__(self, canvas, x, y, image_path, command, state=tk.NORMAL, tags=None):
        self.canvas = canvas
        self.btn_image = tk.PhotoImage(file=image_path)
        self.canvas_btn_img_obj = canvas.create_image(x, y, anchor='nw', state=state, 
                                                      image=self.btn_image, tags=tags)
        canvas.tag_bind(self.canvas_btn_img_obj, "<ButtonRelease-1>", 
                        lambda event: (self.flash(), command()))
        
    def flash(self):
        self.set_state(tk.HIDDEN)
        self.canvas.after(self.flash_delay, self.set_state, tk.NORMAL)

    def set_state(self, state):
        self.canvas.itemconfigure(self.canvas_btn_img_obj, state=state)
        
# ------------------------------------------------------ Login Page ------------------------------------------------------
class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        
        self.canvas = Canvas(self, bg="#FFFFFF", height=heigth_window, width=width_window, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack()
        self.image_image_1         = PhotoImage(file = "./assets/img/login/image_1.png")
        self.image_image_2         = PhotoImage(file = "./assets/img/login/image_2.png")
        self.image_image_3         = PhotoImage(file = "./assets/img/login/image_3.png")
        self.image_image_4         = PhotoImage(file = "./assets/img/login/image_4.png")
        self.image_image_5         = PhotoImage(file = "./assets/img/login/image_5.png")
        self.image_image_6         = PhotoImage(file = "./assets/img/login/image_6.png")
        self.image_image_8         = PhotoImage(file = "./assets/img/login/image_8.png")
        self.image_entry_username  = PhotoImage(file = "./assets/img/login/entry_1.png")
        self.image_entry_password  = PhotoImage(file = "./assets/img/login/entry_2.png")
        self.image_is_admin        = PhotoImage(file = "./assets/img/login/is_admin.png")
        self.image_is_not_admin    = PhotoImage(file = "./assets/img/login/is_not_admin.png")
        image_1 = self.canvas.create_image(656.5, 437, image = self.image_image_1)
        image_2 = self.canvas.create_image(540, 603, image = self.image_image_2)
        image_3 = self.canvas.create_image(544, 674, image = self.image_image_3)
        image_4 = self.canvas.create_image(735, 401, image = self.image_image_4)
        image_5 = self.canvas.create_image(507, 280, image = self.image_image_5)
        image_6 = self.canvas.create_image(720,  15, image = self.image_image_6)
        image_8 = self.canvas.create_image(108,  15, image = self.image_image_8)
        self.canvas_outline_image = PhotoImage(file = "./assets/img/common/outline.png")
        self.canvas.create_image(721,  512, image = self.canvas_outline_image)
        entry_username_bg = self.canvas.create_image(833, 607, image=self.image_entry_username)
        entry_password_bg = self.canvas.create_image(833, 680, image=self.image_entry_password)
        button_1 = CanvasButton(self.canvas, 1410,   3, "./assets/img/login/button_1.png", command = lambda: self.controller.on_destroy())
        button_2 = CanvasButton(self.canvas, 1374,   3, "./assets/img/login/button_2.png", command = lambda: self.controller.on_minimize())
        button_3 = CanvasButton(self.canvas,  658, 734, "./assets/img/login/button_3.png", command = lambda: self.controller.login(entry_username.get(), entry_password.get(), checkbutton_status.get()))
        entry_username = Entry(self.canvas, bd=0, bg="#c6c6c6", fg="#000716", highlightthickness=0, font=('Courier', '12', 'bold'))
        entry_password = Entry(self.canvas, bd=0, bg="#c6c6c6", fg="#000716", highlightthickness=0, show="*", font=('Courier', '12', 'bold'))
        
        entry_username.insert(0, "Aaron0x1a0b")
        entry_password.insert(0, "n1bxA0aaor0")
        
        

        checkbutton_status = IntVar()
        checkbutton = Checkbutton(self.canvas, image=self.image_is_not_admin, selectimage=self.image_is_admin, variable=checkbutton_status, 
                                indicatoron=False, borderwidth=0, highlightthickness=0, selectcolor="#2a2a2a", bg="#2a2a2a", activebackground="#2a2a2a")
        entry_username.place(x=645, y=583, width=376, height=34)
        entry_password.place(x=645, y=657, width=376, height=34)
        checkbutton.place(x=1060, y=550)

# ========================================================Customer========================================================
# -------------------------------------------------- Customer Main Page --------------------------------------------------
class CustomerMainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.page_not_inited = True
        
        self.canvas = Canvas(self, bg = "#9A9494", height = 1024, width = 1440, bd = 0, highlightthickness = 0, relief = "ridge")
        self.canvas.pack()
        self.path_to_customer_main = "./assets/img/customer_main/"
        self.image_image_1 = PhotoImage(file = self.path_to_customer_main + "image_1.png")
        self.image_image_2 = PhotoImage(file = self.path_to_customer_main + "image_2.png")
        self.image_image_3 = PhotoImage(file = self.path_to_customer_main + "image_3.png")
        self.image_image_4 = PhotoImage(file = self.path_to_customer_main + "image_4.png")
        self.image_image_5 = PhotoImage(file = self.path_to_customer_main + "image_5.png")
        self.image_image_6 = PhotoImage(file = self.path_to_customer_main + "image_6.png")
        image_1 = self.canvas.create_image( 753.0, 510.0, image = self.image_image_1)
        image_2 = self.canvas.create_image( 720.0,  15.0, image = self.image_image_2)
        image_3 = self.canvas.create_image( 149.0,  15.0, image = self.image_image_3)
        image_4 = self.canvas.create_image( 725.0, 625.0, image = self.image_image_4)
        image_5 = self.canvas.create_image( 409.0, 314.0, image = self.image_image_5)
        image_6 = self.canvas.create_image(1050.0, 316.0, image = self.image_image_6)
        self.canvas_outline_image = PhotoImage(file = "./assets/img/common/outline.png")
        self.canvas.create_image(721,  512, image = self.canvas_outline_image)
        button_1 = CanvasButton(self.canvas, 1410,  3, self.path_to_customer_main + "button_1.png", lambda: self.controller.on_destroy() ) # close
        button_2 = CanvasButton(self.canvas, 1374,  3, self.path_to_customer_main + "button_2.png", lambda: self.controller.on_minimize()) # minimize
        button_3 = CanvasButton(self.canvas,   50, 38, self.path_to_customer_main + "button_3.png", lambda: self.controller.show_frame("customer_main"))
        button_4 = CanvasButton(self.canvas,  707, 78, self.path_to_customer_main + "button_4.png", lambda: self.controller.show_frame("customer_booking"))
        button_5 = CanvasButton(self.canvas,  956, 78, self.path_to_customer_main + "button_5.png", lambda: self.controller.show_frame("customer_info"))
        button_6 = CanvasButton(self.canvas, 1205, 78, self.path_to_customer_main + "button_6.png", lambda: self.controller.show_frame("login"))

    def page_update(self):
        if self.page_not_inited:
            self.put_pie_chart()
            self.page_not_inited = False

    def generate_pie_chart(self, data, img_name):
        labels = [x[0] for x in data]
        values = [x[1] for x in data]
        
        threshold = sum(values)/50
        other_sum = sum(v for v in values if v < threshold)
        values = [v for v in values if v >= threshold]
        labels = [l for l, v in zip(labels, values) if v >= threshold]
        values.append(other_sum)
        labels.append('Other')
        
        fig, ax = plt.subplots(figsize=(7, 7))
        ax.pie(values,
               labels=labels, 
               autopct='%1.1f%%',
               textprops={'weight':'bold', 'size':12}
               )
        center_circle = plt.Circle((0, 0), 0.0, fc='white')
        fig.gca().add_artist(center_circle)
        ax.patch.set_alpha(0.0) 
        fig.savefig(self.path_to_customer_main + img_name, transparent=True, pad_inches=0.0, bbox_inches='tight')
    
    def put_pie_chart(self):
        command = """SELECT letter, SUM(count) AS total_count
                        FROM (
                            SELECT LEFT(LCase([first_name]), 1) AS letter, COUNT(*) AS count
                            FROM Customer
                            WHERE Len([first_name]) > 0
                            GROUP BY LEFT(LCase([first_name]), 1)
                            UNION ALL
                            SELECT LEFT(LCase([last_name]), 1) AS letter, COUNT(*) AS count
                            FROM Customer
                            WHERE Len([last_name]) > 0
                            GROUP BY LEFT(LCase([last_name]), 1)
                        ) AS subquery
                        GROUP BY letter
                        ORDER BY SUM(count) DESC;
                        """
        data = self.controller.execute_sql(command)
        self.generate_pie_chart(data, 'people_first_letter_chart.png')
        
        command = """SELECT Country.iso_alpha3 AS country, Count(Airplane.airplane_id) AS num_airplanes
                        FROM (Country
                        INNER JOIN Airline ON Country.country_ID = Airline.country_iso)
                        INNER JOIN Airplane ON Airline.airline_ID = Airplane.airline_ID
                        GROUP BY Country.iso_alpha3
                        ORDER BY Count(Airplane.airplane_id) DESC;
                        """
        data = self.controller.execute_sql(command)
        self.generate_pie_chart(data, 'country_airplane_count.png')
        
        self.people_first_letter_chart = PhotoImage(file = self.path_to_customer_main + 'people_first_letter_chart.png')
        self.canvas.create_image(125+self.people_first_letter_chart.width()/2, 374+self.people_first_letter_chart.height()/2, image = self.people_first_letter_chart)
        
        self.country_airplane_count = PhotoImage(file = self.path_to_customer_main + 'country_airplane_count.png')
        self.canvas.create_image(765+self.country_airplane_count.width()/2, 374+self.country_airplane_count.height()/2, image = self.country_airplane_count)

# ----------------------------------------------------- Booking Page -----------------------------------------------------
class CustomerBookingPage(tk.Frame): # make book_block_dark_if_unavailable
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.page_not_inited = True
        
        # -------------------------------------------------- Basic Element Area --------------------------------------------------
        self.canvas = Canvas(self, bg = "#9A9494", height = 1024, width = 1440, bd = 0, highlightthickness = 0, relief = "ridge")
        self.canvas.pack()
        self.path_to_customer_booking = "./assets/img/customer_booking/"
        self.image_image_1 = PhotoImage(file = self.path_to_customer_booking + "image_1.png")
        self.image_image_2 = PhotoImage(file = self.path_to_customer_booking + "image_2.png")
        self.image_image_3 = PhotoImage(file = self.path_to_customer_booking + "image_3.png")
        image_1 = self.canvas.create_image( 689.0,  355.0, image = self.image_image_1)
        image_2 = self.canvas.create_image( 720.0,   15.0, image = self.image_image_2)
        image_3 = self.canvas.create_image( 161.0,   15.0, image = self.image_image_3)
        self.canvas_outline_image = PhotoImage(file = "./assets/img/common/outline.png")
        self.canvas.create_image(721,  512, image = self.canvas_outline_image)
        button_1 = CanvasButton(self.canvas,   50,  38, self.path_to_customer_booking + "button_1.png", command = lambda: self.controller.show_frame("customer_main"))
        button_2 = CanvasButton(self.canvas, 1205,  78, self.path_to_customer_booking + "button_2.png", command = lambda: self.controller.go_back())
        button_3 = CanvasButton(self.canvas, 1410,   3, self.path_to_customer_booking + "button_3.png", command = lambda: self.controller.on_destroy() ) # close
        button_4 = CanvasButton(self.canvas, 1374,   3, self.path_to_customer_booking + "button_4.png", command = lambda: self.controller.on_minimize()) # minimize
        button_5 = CanvasButton(self.canvas,  956,  78, self.path_to_customer_booking + "button_5.png", command = lambda: self.controller.show_frame("customer_info"))
        
    def page_update(self):
        if self.page_not_inited:
            # --------------------------------------------------- Book Block Area ----------------------------------------------------
            self.book_block_canvas = Canvas(self.canvas, bg="#ffffff", width=1020, height=730, bd=0, highlightthickness=0, relief="ridge")
            self.book_block_canvas.bind("<MouseWheel>", self.on_mouse_wheel)
            self.book_block_canvas.place(x=50, y=250)
            self.scrollbar = tk.Scrollbar(self.canvas, width=20, highlightthickness=0, troughcolor='gray', orient=tk.VERTICAL)
            self.scrollbar.config(command=self.update_background_position)
            self.scrollbar.place(x=1080, y=250, height=730)
            self.book_block_canvas.config(yscrollcommand=self.scrollbar.set)
        
            self.book_block_canvas_background_image = PhotoImage(file = self.path_to_customer_booking + "image_5.png")
            self.book_block_canvas_background       = self.book_block_canvas.create_image( 0,  0, image = self.book_block_canvas_background_image, anchor=tk.NW)
            self.image_image_of_book_block          = PhotoImage(file = self.path_to_customer_booking + "image_4.png")
            
            # ----------------------------------------------------- Search Area ------------------------------------------------------
            self.image_image_inputs = PhotoImage(file = self.path_to_customer_booking + "image_6.png")
            self.image_inputs = self.canvas.create_image(1271.5, 603.5, image = self.image_image_inputs)
            
            self.flights = self.controller.execute_sql("Select * from Flight")
            
            departure_airport_list = list(set(i[1] for i in self.flights))
            arrival_airport_list   = list(set(i[2] for i in self.flights))
            
            self.airport_available = {i:[] for i in airports.keys()}
            departure_country_list = []
            arrival_country_list   = []
            
            for i, ii in zip(departure_airport_list, arrival_airport_list):
                if airports_revers[i] not in departure_country_list:
                    departure_country_list.append(airports_revers[i])
                if airports_revers[ii] not in arrival_country_list:
                    arrival_country_list.append(airports_revers[ii])
                for iii in [i,ii]:
                    if iii not in self.airport_available[airports_revers[iii]]:
                        self.airport_available[airports_revers[iii]].append(iii)
            
            self.combobox_departure_country = Combobox(self.canvas, state="readonly", values = sorted(departure_country_list), width=10)
            self.combobox_arrival_country   = Combobox(self.canvas, state="readonly", values = sorted(arrival_country_list  ), width=10)
            self.combobox_departure_airport = Combobox(self.canvas, state="readonly", values = [""], width=10)
            self.combobox_arrival_airport   = Combobox(self.canvas, state="readonly", values = [""], width=10)
            self.combobox_departure_year    = Combobox(self.canvas, state="readonly", values = [""], width=10)
            self.combobox_departure_month   = Combobox(self.canvas, state="readonly", values = [""], width=10)
            self.combobox_departure_day     = Combobox(self.canvas, state="readonly", values = [""], width=10)
            
            self.combobox_departure_country.bind('<<ComboboxSelected>>', self.update_comboboxes)
            self.combobox_arrival_country  .bind('<<ComboboxSelected>>', self.update_comboboxes)
            self.combobox_departure_airport.bind('<<ComboboxSelected>>', self.update_comboboxes)
            self.combobox_arrival_airport  .bind('<<ComboboxSelected>>', self.update_comboboxes)
            self.combobox_departure_year   .bind('<<ComboboxSelected>>', self.update_comboboxes)
            self.combobox_departure_month  .bind('<<ComboboxSelected>>', self.update_comboboxes)
            self.combobox_departure_day    .bind('<<ComboboxSelected>>', self.update_comboboxes)
            
            self.combobox_departure_country.place(x=1287,  y=377)
            self.combobox_arrival_country  .place(x=1287,  y=430)
            self.combobox_departure_airport.place(x=1287,  y=565)
            self.combobox_arrival_airport  .place(x=1287,  y=618)
            self.combobox_departure_year   .place(x=1287,  y=745)
            self.combobox_departure_month  .place(x=1287,  y=797)
            self.combobox_departure_day    .place(x=1287,  y=851)
            
            self.combobox_departure_airport.current(0)
            self.combobox_arrival_airport  .current(0)
            
            self.page_not_inited = False
        # --------------------------------------------------- Book Block Area ----------------------------------------------------
        self.remove_all_book_blocks()
        
        self.default_flight = random.choices(self.flights, k=60)
        self.pos_of_book_block = [(x, y) for y in range(30, 24300, 240) for x in range(30, 1020, 330)]
        for pos, flight_info in zip(self.pos_of_book_block, self.default_flight):
            self.make_book_block(x = pos[0], y = pos[1], flight_info = flight_info)
            
    def get_available_arrival_airports(self, departure_airport):
        available_arrival_airports = set()
        
        for flight in self.flights:
            if flight[1] == departure_airport:
                available_arrival_airports.add(flight[2])

        return list(available_arrival_airports)

    def filter_airports_by_country(self, selected_departure_country, selected_arrival_country):
        available_departure_airports = set()
        available_arrival_airports = set()

        for flight in self.flights:
            if airports_revers[flight[1]] == selected_departure_country:
                available_departure_airports.add(flight[1])
            if airports_revers[flight[2]] == selected_arrival_country:
                available_arrival_airports.add(flight[2])

        return available_departure_airports, available_arrival_airports
  
    def update_comboboxes(self, event):
        # ------------------------------------------------------- Airport --------------------------------------------------------
        selected_departure_country  = self.combobox_departure_country   .get()
        selected_arrival_country    = self.combobox_arrival_country     .get()
        selected_departure_airport  = self.combobox_departure_airport   .get()
        selected_arrival_airport    = self.combobox_arrival_airport     .get()
        
        if event.widget == self.combobox_departure_country or event.widget == self.combobox_arrival_country:
            self.combobox_departure_airport.set('')
            self.combobox_arrival_airport.set('')
            
        available_departure_airports, available_arrival_airports    = self.filter_airports_by_country(selected_departure_country, selected_arrival_country)
        available_departure_airports, _                             = self.filter_airports_by_country(selected_departure_country, selected_arrival_country)
        
        self.combobox_departure_airport.configure(values=[""] + sorted(list(available_departure_airports)))
        self.combobox_arrival_airport  .configure(values=[""] + sorted(list(available_arrival_airports)))
        self.combobox_departure_airport.configure(values=[""] + sorted(list(available_departure_airports)))

        if selected_departure_airport != "":
            available_arrival_airports = self.get_available_arrival_airports(selected_departure_airport)
            self.combobox_arrival_airport.configure(values=[""] + sorted(list(available_arrival_airports)))
        else:
            self.combobox_arrival_airport.configure(values=[""])

        if selected_departure_airport != "" and selected_arrival_airport != "":
            new_data = [flight for flight in self.flights if flight[1] == selected_departure_airport and flight[2] == selected_arrival_airport]
        elif selected_departure_airport != "":
            new_data = [flight for flight in self.flights if flight[1] == selected_departure_airport]
        else:
            new_data = []
            if selected_departure_country and selected_arrival_country:
                for departure_airport in self.airport_available[selected_departure_country]:
                    for arrival_airport in self.airport_available[selected_arrival_country]:
                        new_data.extend([flight for flight in self.flights if flight[1] == departure_airport and flight[2] == arrival_airport])


                        
        # --------------------------------------------------------- Date ---------------------------------------------------------
        dates = [i[3] for i in sorted(new_data, key=lambda x: x[3])]
        classified_dates = {year: {month: {d.day: d.strftime('%m/%d/%Y %H:%M:%S') for d in dates if d.year == year and d.month == month}
                                        for month in set(d.month for d in dates if d.year == year)}
                            for year in set(d.year for d in dates)
                            for d in dates}

        selected_year_str  = self.combobox_departure_year.get()
        selected_month_str = self.combobox_departure_month.get()
        selected_day_str   = self.combobox_departure_day.get()

        selected_year  = int(selected_year_str)  if selected_year_str   else None
        selected_month = int(selected_month_str) if selected_month_str  else None
        selected_day   = int(selected_day_str)   if selected_day_str    else None
        
        available_years  = list(classified_dates.keys())
        available_months = list(classified_dates[selected_year].keys()) if selected_year in classified_dates else [""]
        available_days   = list(classified_dates[selected_year][selected_month].keys()) if selected_year in classified_dates and selected_month in classified_dates[selected_year] else [""]

        self.combobox_departure_year .configure(values = available_years )
        self.combobox_departure_month.configure(values = available_months)
        self.combobox_departure_day  .configure(values = available_days  )
                
        # Create a datetime object from the selected date values
        if selected_year and selected_month and selected_day:
            selected_date = datetime.datetime(selected_year, selected_month, selected_day)
        else:
            selected_date = None

        # Filter flights in new_data based on the selected date
        if selected_date:
            new_data = [flight for flight in new_data if flight[3] > selected_date]

        # ------------------------------------------------------ Book Block ------------------------------------------------------

        
        
        self.remove_all_book_blocks()
        for pos, flight_info in zip(self.pos_of_book_block, sorted(new_data, key=lambda x: x[3])):
            self.make_book_block(x = pos[0], y = pos[1], flight_info = flight_info)
                    
    def make_book_block(self, x, y, flight_info):
        flight_block = self.book_block_canvas.create_image(x+self.image_image_of_book_block.width()/2,  y+self.image_image_of_book_block.height()/2, image = self.image_image_of_book_block, tags=("flight_block"))
        label_1 = Label(self.book_block_canvas, text=f"{flight_info[1]} to {flight_info[2]}" , font=("Courier", 15, "bold"))
        label_2 = Label(self.book_block_canvas, text=f"{flight_info[3].strftime('%Y-%m-%d')}", font=("Courier", 15, "bold"))
        label_3 = Label(self.book_block_canvas, text=f"{flight_info[3].strftime('%H:%M')}"   , font=("Courier", 15, "bold"))
        self.book_block_canvas.create_window(x+25, y+20   , width=250.0, height=40.0, window=label_1, anchor=tk.NW, tags=("flight_block"))
        self.book_block_canvas.create_window(x+25, y+20+40, width=250.0, height=40.0, window=label_2, anchor=tk.NW, tags=("flight_block"))
        self.book_block_canvas.create_window(x+25, y+20+80, width=250.0, height=40.0, window=label_3, anchor=tk.NW, tags=("flight_block"))
        button_book = CanvasButton(self.book_block_canvas,  x+75, y+145, self.path_to_customer_booking + "button_6.png", command = lambda: self.go_to_flight_info(flight_info), tags=("flight_block"))
        self.book_block_canvas.config(scrollregion=(0, 0, 1350, y+270))
    
    def remove_all_book_blocks(self):
        for tag in self.book_block_canvas.find_withtag("flight_block"):
            self.book_block_canvas.delete(tag)
    
    def search_for_booking_and_display_it_all(self):
        if 1:
            self.remove_all_book_blocks()
    
    def go_to_flight_info(self, flight_info):
        self.controller.frames["customer_flight_info"].information_update(flight_info)
        self.controller.show_frame("customer_flight_info")
    
    def on_mouse_wheel(self, event):
            delta = event.delta
            self.update_background_position("scroll", int(-1 * (delta / 120)), "units")
            
    def update_background_position(self, *args):
            self.book_block_canvas.yview(*args)
            current_y = self.book_block_canvas.canvasy(0)
            self.book_block_canvas.coords(self.book_block_canvas_background, 0, current_y)

# ----------------------------------------------- Flight Information Page ------------------------------------------------
class CustomerFlightInformationPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        self.canvas = Canvas(self, bg = "#9A9494", height = 1024, width = 1440, bd = 0, highlightthickness = 0, relief = "ridge")
        self.canvas.pack()
        self.path_to_customer_flight_info = "./assets/img/customer_flight_info/"

        self.image_image_1 = PhotoImage(file=self.path_to_customer_flight_info+"image_1.png")
        self.image_image_2 = PhotoImage(file=self.path_to_customer_flight_info+"image_2.png")
        self.image_image_3 = PhotoImage(file=self.path_to_customer_flight_info+"image_3.png")
        self.image_image_4 = PhotoImage(file=self.path_to_customer_flight_info+"image_4.png")
        self.image_image_5 = PhotoImage(file=self.path_to_customer_flight_info+"image_5.png")
        
        image_1 = self.canvas.create_image( 752.915,480.26,image=self.image_image_1)
        image_2 = self.canvas.create_image( 720.0,  15.0,image=self.image_image_2)
        image_3 = self.canvas.create_image( 215.0,  15.0,image=self.image_image_3)
        image_4 = self.canvas.create_image(1075.0, 524.0,image=self.image_image_4)
        image_5 = self.canvas.create_image( 375.0, 625.0,image=self.image_image_5)
        
        self.canvas_outline_image = PhotoImage(file = "./assets/img/common/outline.png")
        self.canvas.create_image(721,  512, image = self.canvas_outline_image)
        
        button_1 = CanvasButton(self.canvas, 1410.0,   3.0, self.path_to_customer_flight_info+"button_1.png", command=lambda: self.controller.on_destroy() )
        button_2 = CanvasButton(self.canvas, 1374.0,   3.0, self.path_to_customer_flight_info+"button_2.png", command=lambda: self.controller.on_minimize())
        button_3 = CanvasButton(self.canvas,   50.0,  38.0, self.path_to_customer_flight_info+"button_3.png", command=lambda: self.controller.show_frame("customer_main"))
        button_4 = CanvasButton(self.canvas, 1205.0,  78.0, self.path_to_customer_flight_info+"button_4.png", command=lambda: self.controller.go_back())
        button_6 = CanvasButton(self.canvas, 1158.0, 912.0, self.path_to_customer_flight_info+"button_6.png", command=lambda: self.controller.go_back())

    def information_update(self, flight_info):
        self.remove_old_data()
        font_default = ("Courier", "8", "bold")
        self.label_flight_id            = Label(self.canvas, anchor="e", text=f"{flight_info[0]}" , font=font_default)
        airplane_model                  = self.controller.execute_sql(f"select model_ID from Airplane where airplane_ID = '{flight_info[5]}'")[0][0]
        self.label_airplane_id          = Label(self.canvas, anchor="e", text=f"{flight_info[5]} ({airplane_model})" , font=font_default)
        departure_Airport_country_iso   = self.controller.execute_sql(f"select country_iso from Airport where airport_ID = '{flight_info[1]}'")[0][0]
        arrival_Airport_country_iso     = self.controller.execute_sql(f"select country_iso from Airport where airport_ID = '{flight_info[2]}'")[0][0]
        departure_airport_country       = self.controller.execute_sql(f"select full_name from Country where country_ID = '{departure_Airport_country_iso}'")[0][0]
        arrival_airport_country         = self.controller.execute_sql(f"select full_name from Country where country_ID = '{arrival_Airport_country_iso  }'")[0][0]
        self.label_departure_airport    = Label(self.canvas, anchor="e", text=f"{flight_info[1]} ({departure_airport_country})" , font=font_default)
        self.label_arrival_airport      = Label(self.canvas, anchor="e", text=f"{flight_info[2]} ({arrival_airport_country})" , font=font_default)
        self.label_arrival_date         = Label(self.canvas, anchor="e", text=f"{flight_info[3].strftime('%Y-%m-%d')}" , font=font_default)
        self.label_arrival_time         = Label(self.canvas, anchor="e", text=f"{flight_info[3].strftime('%H:%M')}->{(flight_info[3]+datetime.timedelta(hours=int(flight_info[4]))).strftime('%H:%M')}" , font=font_default)
        self.label_seat_selected        = Label(self.canvas, anchor="e", text=f"----" , font=font_default)
        self.canvas.create_window(1100, 360, window=self.label_flight_id         , anchor='nw', tags="item")
        self.canvas.create_window(1100, 410, window=self.label_airplane_id       , anchor='nw', tags="item")
        self.canvas.create_window(1100, 460, window=self.label_departure_airport , anchor='nw', tags="item")
        self.canvas.create_window(1100, 510, window=self.label_arrival_airport   , anchor='nw', tags="item")
        self.canvas.create_window(1100, 560, window=self.label_arrival_date      , anchor='nw', tags="item")
        self.canvas.create_window(1100, 610, window=self.label_arrival_time      , anchor='nw', tags="item")
        self.canvas.create_window(1100, 660, window=self.label_seat_selected     , anchor='nw', tags="item")

        payment_list = preset['payment']
        self.combobox_payment = Combobox(self.canvas, values = payment_list, state="readonly")
        self.combobox_payment.place(x=1100,  y=710)
        self.combobox_payment.current(0)
        
        self.entry_additional_service = Entry(self.canvas, font=font_default)
        self.entry_additional_service.place(x=1100,  y=760)
        self.entry_additional_service.insert(0, "Enter additional service...")
        self.entry_additional_service.bind("<FocusIn>", self.clear_placeholder)
        self.entry_additional_service.bind("<FocusOut>", self.restore_placeholder)
        
        seats_info = self.controller.execute_sql(f"select seat_ID, seat_position, class from Seat where airplane_ID = '{flight_info[5]}'")
        flight_booked_seat_info = [i[0] for i in self.controller.execute_sql(f"select seat_ID from Booking where flight_ID = {flight_info[0]}")]
        
        
        seats_index = 0
        business_seats = []
        premium_seats = []
        economy_seats = []

        for seat in seats_info:
            if seat[0] not in flight_booked_seat_info:
                command = (self.path_to_customer_flight_info + "green.png", lambda seat=seat: self.label_seat_selected.config(text=f"{seat[0]}:{seat[1]}:{seat[2]}"))
            else:
                command = (self.path_to_customer_flight_info + "red.png", lambda: print("red seat clicked."))

            if seat[2] == "business":
                business_seats.append(command)
            elif seat[2] == "premium":
                premium_seats.append(command)
            elif seat[2] == "economy":
                economy_seats.append(command)

        seat_categories = [business_seats, premium_seats, economy_seats]
        
        print_text(f"{airplane_model} {[len(business_seats),len(premium_seats),len(economy_seats)]}")
        
        for i, seat_list in enumerate(seat_categories):
            row = 25 if i == 0 else 26
            col = 4 if i == 0 else (8 if i == 1 else 17)
            seats_index = 0

            for y in range(col):
                for x in range(row):
                    if seats_index < len(seat_list):
                        command = seat_list[seats_index]
                        seats_index += 1
                    else:
                        command = [self.path_to_customer_flight_info + "gray.png", lambda: print("gray seat clicked.")]

                    CanvasButton(self.canvas, 85 + x * [23.5, 22.5, 22.5][i], [325, 435, 650][i] + y * [22, 22.5, 18][i], command[0], command=command[1], tags="item")
        
        
        button_5 = CanvasButton(self.canvas,  850.0, 912.0, self.path_to_customer_flight_info+"button_5.png", command=lambda: self.make_a_booking(flight_info))

    def remove_old_data(self):
        for item in self.canvas.find_withtag("item"):
            self.canvas.delete(item)

    def make_a_booking(self, flight_info):
        if self.label_seat_selected.cget("text").split(":")[0] == "----":
            messagebox.showerror("You shell not book.", "You should select a seat first.")
            return
        self.controller.update_flights_that_user_booked_before()
        for past_booking_list in self.controller.flights_that_user_booked_before:
            past_booking = past_booking_list[0]
            if past_booking[3]+datetime.timedelta(hours=int(past_booking[4])) >= flight_info[3] >= past_booking[3]:
                messagebox.showerror("You shell not book.", \
                    f"This flight's flying time is conflicted with the book that you booked before:\n{past_booking[1]} to {past_booking[2]}\n{past_booking[3].strftime('%Y-%m-%d')}\n{past_booking[3].strftime('%H:%M')} to {(past_booking[3]+datetime.timedelta(hours=int(past_booking[4]))).strftime('%H:%M')}")
                return
        response = messagebox.askyesnocancel("Really? Are you sure?", "This flight is no conflict with all the flight you booked before.\n Are you sure you want to book the flight?")
        if response is None:
            print_text("User clicked Cancel booking.", state="in")
        elif response:
            current_time = datetime.datetime.now()
            other_data = [self.label_seat_selected.cget("text").split(":")[0], self.combobox_payment.get(), self.entry_additional_service.get()]
            if other_data[2] == "Enter additional service...":
                other_data[2] = 'NULL'
            else:
                other_data[2] = f"'{other_data[2]}'"
            command = f"Insert into Booking values ({flight_info[0]}, {other_data[0]}, #{current_time.strftime('%m-%d-%Y %H:%M:%S')}#, '{other_data[1]}', {other_data[2]}, '{self.controller.username}');"
            try:
                result = self.controller.execute_sql(command)
                if result == 1:
                    messagebox.showinfo("Well", "Flight Booking successfully.\n You can leave this page now.")
                    self.information_update(flight_info)
            except Exception as e:
                print_text(e, state="error")
                messagebox.showinfo("You didn't booked", "Something goes wrong.")
        else:
            print_text("User clicked not booking.", state="in")
        
    def clear_placeholder(self,event):
        if self.entry_additional_service.get() == "Enter additional service...":
            self.entry_additional_service.delete(0, tk.END)

    def restore_placeholder(self,event):
        if self.entry_additional_service.get() == "":
            self.entry_additional_service.insert(0, "Enter additional service...")

# ---------------------------------------------------- Self Info Page ----------------------------------------------------
class CustomerInformationPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.page_not_inited = True
        # -------------------------------------------------------- basic ---------------------------------------------------------
        self.canvas = Canvas(self, bg = "#9A9494", height = 1024, width = 1440, bd = 0, highlightthickness = 0, relief = "ridge")
        self.canvas.pack()
        self.path_to_customer_info = "./assets/img/customer_info/"
        self.image_image_1 = PhotoImage(file=(self.path_to_customer_info + "image_1.png"))
        self.image_image_2 = PhotoImage(file=(self.path_to_customer_info + "image_2.png"))
        self.image_image_3 = PhotoImage(file=(self.path_to_customer_info + "image_3.png"))
        self.image_image_4 = PhotoImage(file=(self.path_to_customer_info + "image_4.png"))
        
        self.image_image_6 = PhotoImage(file=(self.path_to_customer_info + "image_6.png"))
        image_1 = self.canvas.create_image( 731.0, 486.0, image = self.image_image_1)
        image_2 = self.canvas.create_image( 720.0,  15.0, image = self.image_image_2)
        image_3 = self.canvas.create_image( 176.0,  15.0, image = self.image_image_3)
        image_4 = self.canvas.create_image(1075.0, 625.0, image = self.image_image_4)
        image_6 = self.canvas.create_image( 375.0, 625.0, image = self.image_image_6)
        self.canvas_outline_image = PhotoImage(file = "./assets/img/common/outline.png")
        self.canvas.create_image(721,  512, image = self.canvas_outline_image)
        button_1 = CanvasButton(self.canvas, 1410.0,   3.0, self.path_to_customer_info + "button_1.png", command=lambda: self.controller.on_destroy() )
        button_2 = CanvasButton(self.canvas, 1374.0,   3.0, self.path_to_customer_info + "button_2.png", command=lambda: self.controller.on_minimize())
        button_3 = CanvasButton(self.canvas,   50.0,  38.0, self.path_to_customer_info + "button_3.png", command=lambda: self.controller.show_frame("customer_main"))
        button_4 = CanvasButton(self.canvas, 1205.0,  78.0, self.path_to_customer_info + "button_4.png", command=lambda: self.controller.go_back())
        button_8 = CanvasButton(self.canvas,  956.0,  78.0, self.path_to_customer_info + "button_8.png", command=lambda: self.controller.show_frame("customer_booking"))
        
        # ------------------------------------------------------- bookings -------------------------------------------------------
        self.book_block_canvas = Canvas(self.canvas, bg="#ffffff", width=650, height=700, bd=0, highlightthickness=0, relief="ridge")
        self.book_block_canvas.bind("<MouseWheel>", self.on_mouse_wheel)
        self.book_block_canvas.place(x=742.5, y=300)
        self.scrollbar = tk.Scrollbar(self.canvas, width=20, highlightthickness=0, bg="#000000", troughcolor='gray', orient=tk.VERTICAL)
        self.scrollbar.config(command=self.update_background_position)
        self.scrollbar.place(x=1365, y=260, height=730)
        self.book_block_canvas.config(yscrollcommand=self.scrollbar.set)
    
        self.image_image_of_book_block  = PhotoImage(file=(self.path_to_customer_info + "image_5.png"))
        
        self.pos_of_book_block = [(50, y) for y in range(30, 2000, 75) ]
     
    def page_update(self):
        if self.page_not_inited:
            print_text("Page inited", state="window")
            # ------------------------------------------------------ self info -------------------------------------------------------
            font_default = ("Courier", "8", "bold")
            self.info = self.controller.execute_sql(f"select * from Customer where user_ID = '{self.controller.username}'")[0]
            
            self.entry_2  = Text(self.canvas, font=font_default, fg="black") # email
            self.entry_3  = Text(self.canvas, font=font_default, fg="black") # phone number
            self.entry_4  = Text(self.canvas, font=font_default, fg="black") # username
            self.entry_5  = Text(self.canvas, font=font_default, fg="black") # password
            self.entry_6  = Text(self.canvas, font=font_default, fg="black") # first name
            self.entry_7  = Text(self.canvas, font=font_default, fg="black") # last name
            self.entry_8  = Text(self.canvas, font=font_default, fg="black") # sex
            self.entry_9  = Text(self.canvas, font=font_default, fg="black") # married
            self.entry_10 = Text(self.canvas, font=font_default, fg="black") # birthday
            self.entry_11 = Text(self.canvas, font=font_default, fg="black") # address
            self.entry_12 = Text(self.canvas, font=font_default, fg="black") # address
            self.entry_2 .insert("1.0", self.info[11]                                       ) # email
            self.entry_3 .insert("1.0", self.info[12]                                       ) # phone number)
            self.entry_4 .insert("1.0", self.info[0]                                        ) # username
            self.entry_5 .insert("1.0", self.info[1]                                        ) # password
            self.entry_6 .insert("1.0", self.info[2]                                        ) # first name
            self.entry_7 .insert("1.0", self.info[3]                                        ) # last name
            self.entry_8 .insert("1.0", "Male" if self.info[4] == "M" else "Female"         ) # sex
            self.entry_9 .insert("1.0", "Married" if self.info[5] == "1" else "Not Married" ) # married
            self.entry_10.insert("1.0", self.info[6].strftime('%Y-%m-%d')                   ) # birthday
            self.entry_11.insert("1.0", ", \n".join(self.info[7:11])                        ) # address
            membership_name = self.controller.execute_sql(f"select type_description from Membership where type = '{self.info[13]}';")
            self.entry_12.insert("1.0", membership_name                                     ) # 

            self.entries = [self.entry_2 , self.entry_3 , self.entry_4 , self.entry_5 , self.entry_6 , self.entry_7 , self.entry_8 , self.entry_9 , self.entry_10, self.entry_12]
            for entry, y_pos in zip(self.entries, [330.0, 380.0, 430.0, 480.0, 530.0, 580.0, 630.0, 680.0, 730, 780]):
                entry.config(state="disabled")
                entry.place(x=450.0, y=y_pos, width=200.0, height=30)

            self.entry_11.config(state="disabled")
            self.entry_11.place(x=450.0, y=830, width=200.0, height=90)

            self.page_not_inited = False
        self.update_booking()
            
    def make_book_block(self, x, y, flight_info):
        flight_block_bg = self.book_block_canvas.create_image(x+self.image_image_of_book_block.width()/2,  y+self.image_image_of_book_block.height()/2, image = self.image_image_of_book_block, tags=("book_block"))

        label_1 = Label(self.book_block_canvas, text=f"{flight_info[3].strftime('%Y-%m-%d')} | {flight_info[1]} to {flight_info[2]}" , font=("Space Mono", 13, "bold"), bg = "#a5a4b1", anchor="w")
        self.book_block_canvas.create_window(x+20, y+12.5   , width=400.0, height=25.0, window=label_1, anchor=tk.NW, tags=("book_block"))
        button_book = CanvasButton(self.book_block_canvas,  x+500, y+20, self.path_to_customer_info + "button_5.png", command = lambda: self.delete_booking(flight_info), tags=("book_block"))
        self.book_block_canvas.config(scrollregion=(0, 0, 650, y+50))
    
    def update_info(self):
        pass 
    
    def edit_info(self):
        pass
    
    def save_edit_info(self):
        pass

    def update_booking(self):
        for tag in self.book_block_canvas.find_withtag("book_block"):
            self.book_block_canvas.delete(tag)
        flights_info = [ii for i in self.controller.execute_sql(f"select flight_ID from Booking where user_ID = '{self.controller.username}'") 
                        for ii in self.controller.execute_sql(f"select * from Flight where flight_ID = {i[0]}")]
        for pos, flight_info in zip(self.pos_of_book_block, flights_info):
            self.make_book_block(x = pos[0], y = pos[1], flight_info = flight_info)
            
    def delete_booking(self, flight_info):
        response = messagebox.askyesnocancel("Really? Are you sure?", "Delete that booking?")
        if response is None:
            print_text("User clicked cancel action.", state = "in")
        elif response:
            command = f"DELETE FROM Booking WHERE user_ID='{self.controller.username}' and flight_ID = {flight_info[0]};"
            result = self.controller.execute_sql(command)
            if result == 1:
                messagebox.showinfo("well", "Deleted successfully.")
                self.update_booking()
        else:
            print_text("User clicked not booking.", state = "in")

    def on_mouse_wheel(self, event):
        delta = event.delta
        self.update_background_position("scroll", int(-1 * (delta / 120)), "units")
            
    def update_background_position(self, *args):
        self.book_block_canvas.yview(*args)
        current_y = self.book_block_canvas.canvasy(0)

# =========================================================Admin==========================================================
# --------------------------------------------------- Admin Main Page ----------------------------------------------------
class AdminMainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        self.canvas = tk.Canvas(self, height=heigth_window, width=width_window, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack()
        self.path_to_admin_main = "./assets/img/admin_main/"
        self.image_image_1   = PhotoImage(file = self.path_to_admin_main + "image_1.png"  )
        self.image_image_2   = PhotoImage(file = self.path_to_admin_main + "image_2.png"  )
        self.image_image_3   = PhotoImage(file = self.path_to_admin_main + "image_3.png"  )
        self.image_image_4   = PhotoImage(file = self.path_to_admin_main + "image_4.png"  )
        self.image_1 = self.canvas.create_image( 657.0, 300.0, image = self.image_image_1)
        self.image_2 = self.canvas.create_image( 725.0, 622.0, image = self.image_image_2)
        self.image_3 = self.canvas.create_image( 720.0,  15.0, image = self.image_image_3)
        self.image_4 = self.canvas.create_image( 130.0,  15.0, image = self.image_image_4)
        self.canvas_outline_image = PhotoImage(file = "./assets/img/common/outline.png")
        self.canvas.create_image(721,  512, image = self.canvas_outline_image)
        self.button_1  = CanvasButton(self.canvas, 1410,   3, self.path_to_admin_main + "button_1.png" , command = lambda: self.controller.on_destroy()) # close
        self.button_2  = CanvasButton(self.canvas, 1374,   3, self.path_to_admin_main + "button_2.png" , command = lambda: self.controller.on_minimize()) # minimize
        self.button_3  = CanvasButton(self.canvas,   50,  38, self.path_to_admin_main + "button_3.png" , command = lambda: print_text("button_0 clicked"))
        self.button_4  = CanvasButton(self.canvas, 1205,  78, self.path_to_admin_main + "button_4.png" , command = lambda: self.controller.show_frame("login"))
        self.button_5  = CanvasButton(self.canvas,  101, 609, self.path_to_admin_main + "button_5.png" , command = lambda: self.controller.show_frame("admin_admin"))
        self.button_6  = CanvasButton(self.canvas,  100, 301, self.path_to_admin_main + "button_6.png" , command = lambda: self.controller.show_frame("admin_flight"))
        self.button_7  = CanvasButton(self.canvas,  432, 301, self.path_to_admin_main + "button_7.png" , command = lambda: self.controller.show_frame("admin_booking"))
        self.button_8  = CanvasButton(self.canvas,  764, 301, self.path_to_admin_main + "button_8.png" , command = lambda: self.controller.show_frame("admin_baggage"))
        self.button_9  = CanvasButton(self.canvas,  432, 455, self.path_to_admin_main + "button_9.png" , command = lambda: self.controller.show_frame("admin_login_history"))
        self.button_11 = CanvasButton(self.canvas,  100, 455, self.path_to_admin_main + "button_11.png", command = lambda: self.controller.show_frame("admin_customer"))
        self.button_12 = CanvasButton(self.canvas,  956,  78, self.path_to_admin_main + "button_12.png", command = lambda: print_text("button_about clicked"))#self.controller.show_frame("admin_database"))

# -------------------------------------------------- Flight Table Page ---------------------------------------------------
class AdminFlightTablePage(AdminTablePageWithInputs):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, "./assets/img/admin_flight/")
        self.table_setup("Flight")
        self.setup_inputs()
        
    def setup_inputs(self):
        self.add_inputs(["Flight ID", "Departure Airport", "Arrival Airport", "Departure Time", "Duration", "Airplane ID"])
        self.add_buttons(["Search","Insert"], [self.search_data, self.insert_data])

# -------------------------------------------------- Booking Table Page --------------------------------------------------
class AdminBookingTablePage(AdminTablePageWithInputs):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, "./assets/img/admin_booking/")
        self.table_setup("Booking")        
        self.setup_inputs()


    def setup_inputs(self):
        self.add_inputs(["Flight ID", "Seat ID", "Booking Date", "Payment Information", "Additional Service", "User ID"])
        self.add_buttons(["Search","Insert"], [self.search_data, self.insert_data])

# -------------------------------------------------- Baggage Table Page --------------------------------------------------
class AdminBaggageTablePage(AdminTablePageWithInputs):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, "./assets/img/admin_baggage/")
        self.table_setup("Baggage")        
        self.setup_inputs()

    def setup_inputs(self):
        self.add_inputs(["Baggage ID", "User ID", "Flight ID", "Baggage Count", "Baggage Type", "Weight(kg)", "Dimension"])
        self.add_buttons(["Search","Insert"], [self.search_data, self.insert_data])
        
# ----------------------------------------------- Login History Table Page -----------------------------------------------
class AdminLoginHistoryTablePage(AdminTablePageWithInputs):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, "./assets/img/admin_login_history/")
        self.table_setup("LoginHistory")        
        self.setup_inputs()

    def setup_inputs(self):
        self.add_inputs(["Login ID", "Login ID", "IP Address", "User ID"])
        self.add_buttons(["Search","Insert"], [self.search_data, self.insert_data])

# --------------------------------------------------- Admin Table Page ---------------------------------------------------
class AdminAdminTablePage(AdminTablePageWithInputs):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, "./assets/img/admin_admin/")
        self.table_setup("Admin")        
        self.setup_inputs()

    def setup_inputs(self):
        self.add_inputs(["Admin ID", "Password", "First name", "Last name", "Email", "Phone Number", "Country ISO"])
        self.add_buttons(["Search","Insert"], [self.search_data, self.insert_data])
    
# ------------------------------------------------- Customer Table Page --------------------------------------------------
class AdminCustomerTablePage(AdminTablePageWithInputs):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, "./assets/img/admin_customer/")
        self.table_setup("Customer")        
        self.setup_inputs()

    def setup_inputs(self):
        self.add_inputs(["User ID", "Password", "First name", "Last name", "Gender", "Married", "Birthday", "Country ISO", "Region", "Address 1", "Address 2", "Email", "Phone Number", "Membership"])
        self.add_buttons(["Search","Insert"], [self.search_data, self.insert_data])

# ---------------------------------------------------- Admin Database ----------------------------------------------------
class AdminDatabase(AdminTablePageWithInputs):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, "./assets/img/admin_customer/")
        
# ----------------------------------------------------- Main Running -----------------------------------------------------
if __name__ == '__main__':
    print_text(f"{'Program Begin':=^{printing_adjust}}", state="sys")
    print_text(f"{'Database Init':-^{printing_adjust}}", state="sys")
    database = get_database(os.getcwd() + r"\gui.accdb")
    window = DraggableWindow()
    window.set_database(database)
    
    pages = [
        [               "login", LoginPage                      ],
        [       "customer_main", CustomerMainPage               ], 
        [    "customer_booking", CustomerBookingPage            ], 
        [       "customer_info", CustomerInformationPage        ], 
        ["customer_flight_info", CustomerFlightInformationPage  ],
        [          "admin_main", AdminMainPage                  ], 
        [        "admin_flight", AdminFlightTablePage           ], 
        [       "admin_booking", AdminBookingTablePage          ], 
        [       "admin_baggage", AdminBaggageTablePage          ],
        [ "admin_login_history", AdminLoginHistoryTablePage     ],
        [         "admin_admin", AdminAdminTablePage            ],
        [      "admin_customer", AdminCustomerTablePage         ],
        [      "admin_database", AdminDatabase                  ]
        ]
    for page in pages:
        window.add_frame(page[0], page[1])
    
    # Start the main event loop
    window.show_frame("login")
    window.mainloop()

    close_conn(database)
    print_text(f"{'Program Done':=^{printing_adjust}}", state="sys")