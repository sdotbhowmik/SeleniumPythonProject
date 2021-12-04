from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.maximize_window()
driver.implicitly_wait(30)
driver.set_page_load_timeout(30)
driver.get("https://sdotbhowmik.github.io")
assert "SKB Portfolio" in driver.title
print("Test Passed")
driver.close()
driver.quit()
