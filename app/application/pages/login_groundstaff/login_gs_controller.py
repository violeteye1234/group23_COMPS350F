#login_gs_controller.py
from utils.page_controller import PageController
from .login_gs_view import LoginPageViewGS
from models.GS_user import gs_user

class LoginGS_PageController(PageController):
    def __init__(self, root, parent_container):
        super().__init__(root, parent_container)
        self.view = LoginPageViewGS(parent_container, self.onclick1, self.onclick2)
        self.view.render()

    def onclick1(self):
        print("login clicked!")
        user_name = self.view.entry_user_name.get()     #这里有问题   .entry_user_name.get()
        password = self.view.entry_password.get()

        GS_user = gs_user(user_name, password)
        print(f"Created: Username:{GS_user.user_name}, Password:{GS_user.password}")

        #加入验证部分...

    def onclick2(self):
        print("forgot clicked!")