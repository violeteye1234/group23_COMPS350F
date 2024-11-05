from utils.page_controller import PageController
from .login_view import LoginPageView

class LoginPageController(PageController):
    def __init__(self, root, parent_container):
        super().__init__(root, parent_container)
        self.view = LoginPageView(parent_container)
        self.view_set_controller()
        
    def login(self, username: str, password: str):
        self.root.logger.info(f"Attempting login with username: {username}, password: {password}")
        self.root.show_page('Main')
    
    def go_to_register(self):
        self.root.show_page('Register')
    
    def cleanup(self):
        self.view.destroy()
        self.view = None
