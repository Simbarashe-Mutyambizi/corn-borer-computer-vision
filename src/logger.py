# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 11:42:34 2024

@author: SWRM
"""

import logging
import os
from datetime import datetime

#this file logs the activities and functions executed on our app, from errors to anything else
#grabs the date of the operation and time details
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

#here any log created will be added to the log file which will be located in the current directory which is src
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
    
    )