import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" 
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE) 
os.makedirs(logs_path,exist_ok=True) 
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE) 
logging.basicConfig( 
                    filename=LOG_FILE_PATH, 
                    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s", 
                    level=logging.INFO) 

# if __name__ == "__main__": 
#     logging.info("Logging initiated")


# # 1. Create a unique log file name with timestamp
# LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# # 2. Define logs folder path (just the folder, not the file)
# logs_dir = os.path.join(os.getcwd(), "logs")
# os.makedirs(logs_dir, exist_ok=True)  # create "logs" folder if not exists

# # 3. Create full log file path inside logs folder
# LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# # 4. Configure logging
# logging.basicConfig(
#     filename=LOG_FILE_PATH,
#     format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
#     level=logging.INFO,
# )

# # 5. Write first log entry
# if __name__ == "__main__":
#     logging.info("Logging has started")
    

"""
datetime.now().strftime('%m_%d_%Y_%H_%M_%S') → generates a timestamp like:
09_27_2025_15_30_45
The .log is added to the end.
So LOG_FILE = "09_27_2025_15_30_45.log"

os.getcwd() → gets your current working directory, e.g.,
"C:/Users/Obey/Projects"
"logs" → a folder name.
LOG_FILE → the unique file name.
So logs_path =
"C:/Users/Obey/Projects/logs/09_27_2025_15_30_45.log"

os.makedirs(logs_path, exist_ok=True)
Making sure the logs folder exists

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)
Preparing the full log file path
"C:/Users/Obey/Projects/logs/09_27_2025_15_30_45.log/09_27_2025_15_30_45.log"

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
filename=LOG_FILE_PATH → Where logs will be written.
format=... → Structure of each log message.
[2025-09-27 15:35:00] 12 root - INFO - Logging has started
level=logging.INFO → Only logs INFO, WARNING, ERROR, CRITICAL (not DEBUG).

if __name__ == "__main__":
    logging.info("Logging has started")
Writing the first log message
When you run this script directly, it will log:
[2025-09-27 15:35:00] 33 root - INFO - Logging has started
"""