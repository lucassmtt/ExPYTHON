from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chromium.service import ChromiumService

ROOT = Path(__file__).parent.parent.parent.parent
CHROME_DRIVER_PATH = 'chromedriver'

def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromiumEdge


    #chrome_options.add_argument('--headless')
    if options is not None:
        for option in options:
            chrome_options.add_argument(option)

    chrome_service = Service(
        executable_path=CHROME_DRIVER_PATH,
    )

    browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options
    )

    return browser

if __name__ == '__main__':
    options = ('--disable-gpu', '--no-sandbox',)
    browser = make_chrome_browser(*options)
    browser.get('https://www.google.com')
    browser.quit()

