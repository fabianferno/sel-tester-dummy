import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

from http_request_randomizer.requests.proxy.requestProxy import RequestProxy


from selenium import webdriver
PROXY = proxies[0].get_address()
webdriver.DesiredCapabilities.CHROME['proxy'] = {
    "httpProxy": PROXY,
    "ftpProxy": PROXY,
    "sslProxy": PROXY,
    "proxyType": "MANUAL",

}

# you may get different number of proxy when  you run this at each time
req_proxy = RequestProxy()
proxies = req_proxy.get_proxy_list()  # this will create proxy list


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("WEBSITE_URL_HERE")
radiobtn = driver.find_element_by_xpath("//*[@id='answer-2183']")
radiobtn.click()

time.sleep(1)

votebtn = driver.find_element_by_xpath("//*[@id='test-48-ans']/p[1]/input")
votebtn.click()
