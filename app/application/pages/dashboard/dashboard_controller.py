# dashboard controller

# Import necessary modules and classes
from utils.page_controller import PageController  # Base class for page controllers
from .dashboard_view import DashboardPageView      # View class for the dashboard page
from models.user_model import UserModel            # Model class for user data
import tkinter as tk                               # Import tkinter for GUI
from pages.login1.login1_controller import Login1PageController  # Controller for login page
from models.sharedata import SharedData            # Shared data model for inter-page data sharing
from datetime import datetime, timedelta           # Import datetime for handling dates
import datetime                                     # Additional import for datetime module

# Define the DashboardPageController class, inheriting from PageController
class DashboardPageController(PageController):
    def __init__(self, root, parent_container):
        # Initialize the parent class (PageController)
        super().__init__(root, parent_container)
        
        # Store the parent container for layout management
        self.parent_container = parent_container
        
        # Create an instance of the DashboardPageView
        self.view = DashboardPageView(parent_container)
        
        # Set the controller for the view to enable interaction
        self.view.set_controller(self)