from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def switch_to_iframe(driver, parent_container_xpath):
    try:
        iframe_element = driver.find_element(By.TAG_NAME, "iframe")
        driver.switch_to.frame(iframe_element)
        driver.find_element(By.XPATH, parent_container_xpath)
        return driver
    except NoSuchElementException:
        driver.switch_to.default_content()
        return False