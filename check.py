from selenium import webdriver
import time
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait


def get_clear_browsing_button(driver):
    """Find the "CLEAR BROWSING BUTTON" on the Chrome settings page."""
    return driver.find_element_by_css_selector('* /deep/ #clearBrowsingDataConfirm')


def clear_cache(driver, timeout=60):
    """Clear the cookies and cache for the ChromeDriver instance."""
    # navigate to the settings page
    driver.get('chrome://settings/clearBrowserData')

    # wait for the button to appear
    wait = WebDriverWait(driver, timeout)
    wait.until(get_clear_browsing_button)

    # click the button to clear the cache
    get_clear_browsing_button(driver).click()

    # wait for the button to be gone before returning
    wait.until_not(get_clear_browsing_button)


for i in range(0, 100):
    # Driver
    driver = webdriver.Chrome(ChromeDriverManager().install())

    time.sleep(2)

    # Get the website
    driver.get(
        "https://thegreatpageantcommunity.com/2021/09/18/episode-1-indias-miss-tgpc-season-10-meet-the-contestants/")

    time.sleep(1)

    # Click Amanda
    radiobtn = driver.find_element_by_xpath("//*[@id='poll-answer-2183']")
    radiobtn.click()

    time.sleep(1)

    # Click Vote
    votebtn = driver.find_element_by_xpath(
        "//*[@id='polls-48-ans']/p[1]/input")
    votebtn.click()

    time.sleep(2)
    clear_cache(driver)
    driver.close()
