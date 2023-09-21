import logging
# logging is done to keep track/log of execution , errors,exception in some files.
import os  # to store logs in file
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)

# making file in directory even though if it is already present.--> exist_ok=True
os.makedirs(logs_path,exist_ok=True)

# Log File Path
LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE);

# if I want to extend functionalities of logging ,I have to do it in logging.basicConfig 

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)