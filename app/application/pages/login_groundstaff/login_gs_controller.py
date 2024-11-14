#login_gs_controller.py
from utils.page_controller import PageController
from .login_gs_view import LoginPageViewGS
from models.GS_user import gs_user
import tkinter.messagebox as alertbox

class LoginGS_PageController(PageController):
    def __init__(self, root, parent_container):
        super().__init__(root, parent_container)
        self.view = LoginPageViewGS(parent_container)
        self.view.set_controller(self)
        self.default_user_name = "123"
        self.default_password = "123"
        self.view.render()

    def login(self, entry_user_name: str, entry_password: str):
        print("login clicked!")
        #user_name = self.view.entry_user_name.get()     #这里有问题   .entry_user_name.get()
        #password = self.view.entry_password.get()

        GS_user = gs_user(entry_user_name, entry_password)
        print(f"Input: Username:{GS_user.user_name}, Password:{GS_user.password}")

        #logic
        if entry_user_name != self.default_user_name:
            print("Username not found")
            alertbox.showwarning("Login Error", "User account not found!")
            
        elif entry_password != self.default_password:
            print("Password not match")
            alertbox.showwarning("Login Error", "Incorrect password!")

        else:
            print("Correct match!")
            self.root.show_page('Main')

    def forgotpassword(self):
        print("forgot clicked!")