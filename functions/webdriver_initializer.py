from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

def initalize_webdriver() -> webdriver.Chrome:
    options = Options()
    # options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-software-rasterizer")
    options.add_argument("--log-level=3")

    service = Service(executable_path="chromedriver-win64\\chromedriver.exe")

    return webdriver.Chrome(service=service, options=options)