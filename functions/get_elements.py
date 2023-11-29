import emoji
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from .elements_filter import filter_elements

def extract_elements(driver, parent_element_xpath, child_element_name):
    try:
        parent_element = driver.find_element(By.XPATH, parent_element_xpath)
        child_elements = parent_element.find_elements(By.TAG_NAME, child_element_name)
    except NoSuchElementException:
        print(emoji.emojize("[-] :cross_mark: ELEMENT NOT FOUND! CHECK PARENT ELEMENT XPATH OR CHILD ELEMENT NAME!"))

    # FILTER ELEMENTS WITHOUT AN ANCHOR TAG
    return filter_elements(child_elements)
