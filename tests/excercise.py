import time

from selenium import webdriver
from selenium.webdriver.common.by import By


#intialize driver
driver = webdriver.Chrome(executable_path='..//drivers//chromedriver.exe')

#Minimize browser
driver.minimize_window()

#Maximize browser
driver.maximize_window()

# The Implicit Wait in Selenium is used to tell the web driver to wait for a certain amount of time before it throws a “No Such Element Exception”.
# The default setting is 0.
# Once we set the time, the web driver will wait for the element for that time before throwing an exception.
driver.implicitly_wait(30)

#URL opening
driver.get("https://google.com")

#Opening URL in a new window
driver.switch_to.new_window(type_hint="window")
driver.get("https://sdotbhowmik.github.io")

#Opening URL in a new tab
driver.switch_to.new_window(type_hint='tab')
driver.get("https://opensource-demo.orangehrmlive.com/")

#Older strategy for locating elements which is depricated since Selenium 4
driver.find_element_by_name("txtUsername").send_keys("Admin")
driver.find_element_by_name("txtPassword").send_keys("admin123")

#Using of by class for locating elements
driver.find_element(By.ID,'btnLogin').click()

#Getting current location/url
print(driver.current_url)

#Assertion
assert "https://opensource-demo.orangehrmlive.com/index.php/dashboard" in driver.current_url

#Navigations
driver.back()
driver.forward()
driver.refresh()
driver.fullscreen_window()

driver.find_element(By.ID,"welcome").click()
time.sleep(1)

logout = driver.find_element(By.LINK_TEXT,"Logout").is_displayed()
driver.save_screenshot('../scr/full_page.png')
driver.get_screenshot_as_file('../scr/attribute.png')
driver.get_screenshot_as_png()

print(logout)
welcome = driver.find_element(By.ID,"welcome")
print(welcome)
time.sleep(2)
driver.close()
driver.quit()