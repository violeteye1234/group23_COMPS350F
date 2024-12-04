from utils.page_controller import PageController
from .login_view import LoginPageView

class LoginPageController(PageController):
    def __init__(self, root, parent_container):
        # Initialize the LoginPageController by calling the parent constructor
        super().__init__(root, parent_container)

        # Create an instance of LoginPageView, passing the parent container
        self.view = LoginPageView(parent_container)

        # Set this controller as the controller for the LoginPageView
        self.view_set_controller()
        
    def login(self, username: str, password: str):
        # Log the login attempt with username and password
        self.root.logger.info(f"Attempting login with username: {username}, password: {password}")
        # Navigate to the main page after a successful login
        self.root.show_page('Main')

    def login_default(self):
        # Navigate to the default login page
        self.root.show_page('Login1')
    
    def go_to_register(self):
        # Navigate to the registration page
        self.root.show_page('Register')

    def jump_to_main(self):
        # Navigate directly to the main page
        self.root.show_page('Main')
    
    def cleanup(self):
        # Clean up the view by destroying it and setting it to None
        self.view.destroy()
        self.view = None
