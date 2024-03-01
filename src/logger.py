import logging
import os

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)  # Create a log file in the logs folder with current date and time as name
os.makedirs(logs_path,exist_ok =True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)
logging.basicConfig(

    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s -%(levelname)s - %(message)s",
    level=logging.INFO,

    )
