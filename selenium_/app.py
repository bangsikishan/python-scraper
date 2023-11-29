import time

import emoji
from selenium.webdriver.common.by import By

# from config import Values
from config.file_values import results
from functions import identify_website, get_ini_file, initalize_webdriver, switch_to_iframe, extract_elements


def run():
    # base_url = Values.URL.value
    
    # IDENTIFY WEBSITE TYPE
    identify_website(results[1])

    # INITIALIZE THE WEBDRIVER & GET THE WEBSITE
    # driver = initalize_webdriver()
    # driver.get(base_url)
    # time.sleep(5)

    '''
    # SWITCH TO IFRAME IF NEEDED
    is_inside_iframe = switch_to_iframe(driver, parent_element)
    print(emoji.emojize("[+] :check_mark:  INSIDE IFRAME!")) if is_inside_iframe else print(emoji.emojize("[+] :check_mark:  NOT INSIDE IFRAME!"))

    # EXTRACT CHILD ELEMENTS
    child_elements = extract_elements(driver, parent_element, child_element)
    if not child_elements:
        print(emoji.emojize("[-] :cross_mark: NO CHILD ELEMENTS FOUND!"))
        driver.quit()

    for child_element in child_elements:
        title = child_element.find_element(By.XPATH, title_xpath).text
        bidno = child_element.find_element(By.XPATH, bidno_xpath).text
        duedate = child_element.find_element(By.XPATH, duedate_xpath).text
        print("Title: ", title)
        print("Bid No: ", bidno)
        print("Due Date: ", duedate)

    '''
    # CLOSE THE DRIVER
    # driver.quit()
