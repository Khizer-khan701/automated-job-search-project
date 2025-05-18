import os
from datetime import datetime
import logging
from exception import CustomException
import sys

LOG_FILE = f"[{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}].log"
file_path=os.path.join(os.getcwd(),"Log")
os.makedirs(file_path,exist_ok=True)
LOG_FILE_PATH=os.path.join(file_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(filename)s %(lineno)d - %(levelname)s - %(message)s",
    level=logging.INFO
)

if __name__=="__main__":
    try:
        logging.info("execution started")
        a=1/0
    except Exception as e:
        raise CustomException(e,sys)
