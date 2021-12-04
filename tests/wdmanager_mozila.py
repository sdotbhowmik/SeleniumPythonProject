from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.maximize_window()
driver.set_page_load_timeout(30)
driver.implicitly_wait(30)
driver.get("https://sdotbhowmik.github.io")
assert "SKB Portfolio" in driver.title
print("Test passed")
driver.close()
driver.quit()