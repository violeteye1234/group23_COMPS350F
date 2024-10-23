# logger.py
import logging
import os

# 創建一個 logs 目錄來存放日誌文件
LOG_DIR = r"app/logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# 配置日誌記錄器
logger = logging.getLogger("AppLogger")
logger.setLevel(logging.DEBUG)

# 創建日誌處理器，寫入文件
file_handler = logging.FileHandler(os.path.join(LOG_DIR, "app.log"))
file_handler.setLevel(logging.DEBUG)

# 創建日誌處理器，輸出到控制台
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# 定義日誌格式
formatter = logging.Formatter(
    fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# 添加處理器到記錄器
logger.addHandler(file_handler)
logger.addHandler(console_handler)

def get_logger():
    return logger