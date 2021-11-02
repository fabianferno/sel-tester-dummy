import tbselenium.common as cm
from tbselenium.tbdriver import TorBrowserDriver
from tbselenium.utils import launch_tbb_tor_with_stem
import time

tbb_dir = "D:\Softwares\TOR\Tor Browser\Browser"
tor_process = launch_tbb_tor_with_stem(tbb_path=tbb_dir)
with TorBrowserDriver(tbb_dir, tor_cfg=cm.USE_STEM) as driver:
    driver.load_url(
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


tor_process.kill()
