from application.models.logger import get_logger
from application.main_window import MainWindow

# Initialize the logger to record application events
logger = get_logger()
logger.info("Application started.")

# Create an instance of the main application window, passing the logger for logging purposes
window = MainWindow(logger)

# Start the main event loop of the application
window.mainloop()

# Log the event when the application is closed
logger.info("Application closed.")
