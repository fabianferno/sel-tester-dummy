from selenium import webdriver
import os
import subprocess
import time
from selenium.webdriver.support.ui import WebDriverWait


def clear_cache(driver, torexe, timeout=60):
    """Clear the cookies and cache for the ChromeDriver instance."""
    # navigate to the settings page
    # driver.get('chrome://settings/clearBrowserData')

   # try:
    # time.sleep(1)
    # driver.find_element_xpath(
    # "//*[@id='clearBrowsingDataConfirm']").click()
   # except Exception as e:
    print("error in finding clear cache button")
    driver.delete_all_cookies()
    torexe.terminate()
    driver.close()
    autos()


def autos():
    torexe = subprocess.Popen(
        r'C:\Users\david\Desktop\Tor Browser\Browser\TorBrowser\Tor\tor.exe')
    PROXY = "socks5://localhost:9050"  # IP:PORT or HOST:PORT
    options = webdriver.ChromeOptions()
    options.add_argument('--proxy-server=%s' % PROXY)
    # options.add_argument('--headless')
    #options.headless = True

    # Driver
    driver = webdriver.Chrome(
        chrome_options=options, executable_path=r'C:\Users\david\Documents\chromedriver\chromedriver.exe')
    driver.maximize_window()

    # Get the website
    driver.get("https: // thegreatpageantcommunity.com / 2021 / 09 / 18 / episode - 1 - indias - miss - tgpc - season - 10 - meet - the - contestants / %22)

    time.sleep(1)

    # Click Amanda
    try:
        driver.find_element_by_css_selector(
            "input[type='radio'][value='2183']").click()

        time.sleep(1)

        # Click Vote
        driver.find_element_by_name('vote').click()
        time.sleep(1)

    except Exception as e:
        print("error in finding amanda button")
        clear_cache(driver, torexe)
        driver.delete_all_cookies()
        torexe.terminate()
        driver.close()
        autos()


try:
    for i in range(0, 100):
        autos()

except Exception as e:
    print(e)
