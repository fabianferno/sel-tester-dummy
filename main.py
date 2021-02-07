import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://fabianferno.tech/")
# elem = driver.find_element_by_name("q")
# elem.send_keys("Username")
# elem.send_keys(Keys.RETURN)

print(driver.title)
