import configparser
import glob
import os

import emoji

def get_ini_file():
    # GET PATH TO THE INI DIRECTORY
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ini_path = os.path.join(root_dir, 'ini', '*.ini')
    
    # GET INI FILES
    ini_files = glob.glob(ini_path)

    # CHECK IF THERE IS ONLY ONE INI FILE
    if len(ini_files) != 1: 
        print(emoji.emojize("[-] :cross_mark: THERE SHOULD BE ONLY ONE INI FILE IN THE DIRECTORY!"))
        return
    
    # GET INI FILENAME
    ini_filename = ini_files[0]

    # READ INI FILE
    try:
        config = configparser.ConfigParser()
        config.read(ini_filename)
    except configparser.ParsingError:
        print(emoji.emojize("[-] :cross_mark: INI FILE HAS INVALID FORMAT!"))
        return

    # GET VALUES
    name = config.get('TEST', 'NAME', fallback=None)
    base_url = config.get('TEST', 'URL', fallback=None)
    ecgain = config.get('TEST', 'ECGAIN', fallback=None)
    parent_element = config.get('TEST', 'PARENT_ELEMENT_XPATH', fallback=None)
    child_element = config.get('TEST', 'CHILD_ELEMENT_NAME', fallback=None)
    bidno_xpath = config.get('TEST', 'BIDNO_XPATH', fallback=None)
    title_xpath = config.get('TEST', 'TITLE_XPATH', fallback=None)
    duedate_xpath = config.get('TEST', 'DUEDATE_XPATH', fallback=None)

    # CHECK IF FIELDS ARE EMPTY
    if any(variable is None for variable in [name, base_url, ecgain, parent_element, child_element, bidno_xpath, title_xpath, duedate_xpath]):
        print(emoji.emojize("[-] :cross_mark: ONE OR MORE FIELDS ARE EMPTY!"))
        return
    
    return name, base_url, ecgain, parent_element, child_element, bidno_xpath, title_xpath, duedate_xpath
