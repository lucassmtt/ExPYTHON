from pathlib import Path

from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

ROOT = Path(__file__).parent
CHROME_EXEC = Path(__file__).parent / 'drivers' / 'chromedriver'

chrome_options = webdriver.ChromeOptions()
chrome_services = Service(executable_path=str(CHROME_EXEC))
chrome_browser = webdriver.Chrome(
    service=chrome_services,
    options=chrome_options,
)

sleep(2)
chrome_browser.