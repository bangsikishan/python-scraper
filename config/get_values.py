from enum import Enum
import os

from dotenv import load_dotenv

from functions import get_ini_file

class Values(Enum):
    load_dotenv()
    ini_values = get_ini_file()

    DB_HOST = os.environ.get('DB_HOST')
    DB_PORT = os.environ.get('DB_PORT')
    DB_NAME = os.environ.get('DB_NAME')
    
    DB_USER = os.environ.get('DB_USER')
    DB_PASS = os.environ.get('DB_PASS')

    NAME = ini_values[0]
    URL = ini_values[1]
    ECGAIN = ini_values[2]
    PARENT_XPATH = ini_values[3]
    CHILD_XPATH = ini_values[4]
    BIDNO_XPATH = ini_values[5]
    TITLE_XPATH = ini_values[6]
    DUEDATE_XPATH = ini_values[7]
    