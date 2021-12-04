import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='..//drivers//chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("https://opensource-demo.orangehrmlive.com/")
# assert "OrangeHRM" in driver.title
driver.find_element_by_name("txtUsername").send_keys("Admin")
driver.find_element_by_name("txtPassword").send_keys("admin123")
# driver.find_element_by_id("btnLogin").click()
driver.find_element(By.ID,'btnLogin').click()
print(driver.current_url)
assert "https://opensource-demo.orangehrmlive.com/index.php/dashboard" in driver.current_url
driver.back()
driver.forward()
driver.refresh()
driver.fullscreen_window()

driver.find_element(By.ID,"welcome").click()
time.sleep(1)

logout = driver.find_element(By.LINK_TEXT,"Logout").is_displayed()
driver.save_screenshot('../scr/file_name.png')
driver.get_screenshot_as_png()

print(logout)
welcome = driver.find_element(By.ID,"welcome")
print(welcome)
time.sleep(2)
driver.close()
driver.quit()