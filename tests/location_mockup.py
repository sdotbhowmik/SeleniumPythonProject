import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='..//drivers//chromedriver.exe')
driver.maximize_window()
map_coord = {
    "latitude": 39.73925065383228,
    "longitude": -104.99024801028608,
    "accuracy": 1
}
driver.execute_cdp_cmd("Emulation.setGeolocationOverride", map_coord)
# time.sleep(2)
driver.get("https://google.com")
driver.find_element(By.NAME,"q").send_keys("netflix")
driver.find_element(By.NAME,'q').send_keys(Keys.ENTER)
driver.find_element(By.XPATH,'//div[@class="TbwUpd NJjxre"][1]').click()
print("Geolocation testing with Selenium is complete")

# https://chromedevtools.github.io/devtools-protocol/tot/Emulation/#method-setGeolocationOverride


