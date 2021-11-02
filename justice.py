from selenium import webdriver
import os
from selenium import webdriver
import time
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


for i in range(0, 100):
    # Open Browser
    torexe = os.popen(
        r'D:\Softwares\TOR\Tor Browser\Browser\TorBrowser\Tor\tor.exe')
    PROXY = "socks5://localhost:9050"  # IP:PORT or HOST:PORT
    options = webdriver.ChromeOptions()
    options.add_argument('--proxy-server=%s' % PROXY)

    driver = webdriver.Chrome(
        ChromeDriverManager().install(), chrome_options=options)

    # Open URL
    driver.get(
        "WEBSITE_URL_HERE")

    time.sleep(1)

    # Click Amanda
    radiobtn = driver.find_element_by_xpath("//*[@id='answer-2183']")
    radiobtn.click()

    time.sleep(1)

    # Click Vote
    votebtn = driver.find_element_by_xpath(
        "//*[@id='test-48-ans']/p[1]/input")
    votebtn.click()

    time.sleep(2)
    driver.close()
