from application.models.logger import get_logger
from application.main_window import MainWindow

logger = get_logger()
logger.info("Application started.")

window = MainWindow(logger)

window.mainloop()
logger.info("Application closed.")
