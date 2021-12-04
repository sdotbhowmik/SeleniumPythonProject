from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--disable-extensions")
options.add_argument("--headless")
driver = webdriver.Chrome(executable_path="..//drivers//chromedriver.exe", chrome_options=options)
driver.maximize_window()
driver.set_page_load_timeout(30)
driver.implicitly_wait(30)
driver.get("https://sdotbhowmik.github.io")
assert "SKB Portfolio" in driver.title
print("Test Passed")
driver.close()
driver.quit()