import time

import emoji
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from functions import initalize_webdriver
from config import Values


def get_procurement_bids(url: str):
    login_url = "https://procurement.opengov.com/login"

    # INITIALIZE THE WEBDRIVER & GET THE LOGIN PAGE
    driver = initalize_webdriver()
    driver.get(login_url)
    time.sleep(5)

    # LOGIN
    login(driver)
    time.sleep(5)

    # GO TO THE ORIGINAL URL
    driver.get(url)
    time.sleep(5)

    '''
    ECGAIN
    BASEURL
    BIDNO
    TITLE
    DUEDATE
    FILENAME
    FILEURL
    FILESIZE
    HASH
    '''

    # GET NUMBER OF DIVS CONTAINING BIDS
    html = driver.page_source
    number_of_bids = get_number_of_bids(html)

    # ACCESS & FILTER ELEMENTS
    bids = {}
    bid_elements = driver.find_elements(By.CLASS_NAME, "rt-tr-group")[:number_of_bids]
    for index, bid_element in enumerate(bid_elements):
        bid_no = bid_element.find_element(By.XPATH, ".//div/div[2]").text
        title = bid_element.find_element(By.XPATH, ".//div/div[1]").text
        due_date = bid_element.find_element(By.XPATH, ".//div/div[5]").text
        
        bids[index] = {
            "ecgain": Values.ECGAIN.value,
            "base_url": Values.BASEURL.value,
            "bid_no": bid_no,
            "title": title,
            "due_date": due_date
        }

    # CLOSE THE DRIVER
    driver.quit()


def login(driver):
    try:
        # ENTER EMAIL AND PRESS ENTER
        driver.find_element(By.XPATH, '//*[@id="form-group-email"]').send_keys("primevendor124@gmail.com")
        driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/div[2]/div/form/button').click()

        time.sleep(5)

        # ENTER PASSWORD AND PRESS ENTER TO LOGIN
        driver.find_element(By.XPATH, '//*[@id="form-group-password"]').send_keys("Bidding*1234")
        driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div/div/div[2]/div/form/button').click()
    except NoSuchElementException:
        print(emoji.emojize("[-] :cross_mark: LOGIN FAILED! CHECK XPATH!"))


def get_number_of_bids(html):
    soup = BeautifulSoup(html, 'html.parser')

    bids_with_even_classname = soup.find_all("div", {"class": "rt-tr _19vFWHGT79hXeijNVm7GpF -even"})
    bids_with_odd_classname = soup.find_all("div", {"class": "rt-tr _19vFWHGT79hXeijNVm7GpF -odd"})

    total_number_of_bids = len(bids_with_even_classname) + len(bids_with_odd_classname)
    return total_number_of_bids
