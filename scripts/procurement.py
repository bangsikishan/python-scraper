import os
import time
import zipfile

import emoji
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
    for index in range(number_of_bids):
        bid_element = driver.find_element(By.XPATH, f"/html/body/div/div/div/div/main/div/div[2]/div/div/div[3]/div[1]/div[2]/div[{index+1}]")
        bid_no = bid_element.find_element(By.XPATH, ".//div/div[2]").text
        title = bid_element.find_element(By.XPATH, ".//div/div[1]").text
        due_date = bid_element.find_element(By.XPATH, ".//div/div[5]").text
        
        bid_element.click()
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div/main/div[5]/div/ul/li[3]/a"))
        ).click()
        time.sleep(2)

        driver.find_element(By.XPATH, "/html/body/div/div/div/div/main/div[5]/div/ul/li[3]/a").click()
        time.sleep(1)

        driver.find_element(By.XPATH, "/html/body/div/div/div/div/main/div[5]/div/div/div/div/div[2]/div[1]/button").click()
        time.sleep(1)

        driver.find_element(By.CLASS_NAME, "fa-download").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div/div[2]/div/button[1]").click()
        time.sleep(1)

        download_link = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div/div/div[2]/div/a"))
        ).get_attribute("href")

        # DOWNLOAD FILE
        download_info = download_file(download_link)
        
        bids[index] = {
            "ecgain": Values.ECGAIN.value,
            "base_url": Values.URL.value,
            "bid_no": bid_no,
            "title": title,
            "due_date": due_date,
            "fileurl": download_info["fileurl"],
            "filename": download_info["filename"],
            "filesize": download_info["content_length"],
        }
        
        driver.get(url)
        time.sleep(5)

    with open("test.json", "w", encoding="utf-8") as f:
        f.write(str(bids))

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


def download_file(url):
    print(emoji.emojize("[+] :check_mark:  DOWNLOADING FILE..."))

    # GET THE FILE
    response = requests.get(url)

    # GET THE HEADERS
    parsed_headers = dict(response.headers)

    # GET THE FILENAME AND THE CONTENT LENGTH
    filename = parsed_headers.get('Content-Disposition', '').split('filename="')[-1].split('"')[0]
    content_length_bytes  = parsed_headers.get('Content-Length')
    content_length_mb = str(int(content_length_bytes) / (1024 * 1024)) + " MB"

    # WRITE THE CONTENT
    with open("downloads/" + filename, 'wb') as f:
        f.write(response.content)
    
    # EXTRACT DOWNLOADED ZIP FILE
    extracted_files = extract_zip_file("downloads/" + filename)
    
    return {
        "fileurl": url,
        "filename": extracted_files,
        "content_length": content_length_mb
    }


def extract_zip_file(zip_file_path):
    print(emoji.emojize("[+] :check_mark:  EXTRACTING ZIP FILE..."))

    extracted_files = []

    # CREATE A DIRECTORY TO EXTRACT THE FILES
    extraction_directory = os.path.splitext(zip_file_path)[0]
    os.makedirs(extraction_directory, exist_ok=True)

    # EXTRACT THE ZIP FILE
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extraction_directory)
        extracted_files = zip_ref.namelist()
    
    return extracted_files
