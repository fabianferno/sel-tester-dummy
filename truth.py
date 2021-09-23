from selenium import webdriver
import os
import subprocess
import time
from selenium.webdriver.support.ui import WebDriverWait

# To use Tor's SOCKS proxy server with chrome, include the socks protocol in the scheme with the --proxy-server option
# PROXY = "socks5://127.0.0.1:9150" # IP:PORT or HOST:PORT


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


try:

    for i in range(0, 100):
        torexe = subprocess.Popen(
            r'D:\Softwares\TOR\Tor Browser\Browser\TorBrowser\Tor\tor.exe')

        PROXY = "socks5://localhost:9050"  # IP:PORT or HOST:PORT
        options = webdriver.ChromeOptions()
        options.add_argument('--proxy-server=%s' % PROXY)
        # options.add_argument('--headless')
        #options.headless = True

        # Driver
        driver = webdriver.Chrome(
            chrome_options=options, executable_path=r'D:\Documents\sel-tester-dummy\chromedriver.exe')

        driver.maximize_window()

        # Get the website
        driver.get(
            "https://thegreatpageantcommunity.com/2021/09/18/episode-1-indias-miss-tgpc-season-10-meet-the-contestants/")
        # driver.get(
        #     "https://www.whatsmyip.org/")

        time.sleep(1)

        # Click Amanda
        # radiobtn = driver.find_element_by_xpath("//*[@id='poll-answer-2183']")
        driver.find_element_by_css_selector(
            "input[type='radio'][value='2183']").click()

        time.sleep(1)

        # Click Vote
        driver.find_element_by_name('vote').click()

        time.sleep(2)
        clear_cache(driver)
        torexe.terminate()
        driver.quit()

except Exception as e:
    print(e)
