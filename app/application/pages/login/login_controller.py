from utils.page_controller import PageController  # Import base class for page controllers
from .login_view import LoginPageView  # Import the view class for the login page

# Define the LoginPageController class, inheriting from PageController
class LoginPageController(PageController):
    def __init__(self, root, parent_container):
        # Initialize the parent class with the root and parent container
        super().__init__(root, parent_container)
        
        # Create an instance of the LoginPageView, passing the parent container
        self.view = LoginPageView(parent_container)
        
        # Set this controller as the controller for the view
        self.view.set_controller(self)
        
    def login(self, username: str, password: str):
        # Log the attempt to log in with the provided username and password
        self.root.logger.info(f"Attempting login with username: {username}, password: {password}")
        
        # Show the main page upon successful login
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
        # Clean up resources when done
        self.view.destroy()  # Destroy the view
        self.view = None  # Clear the view reference