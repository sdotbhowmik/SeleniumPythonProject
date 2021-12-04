from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.maximize_window()
driver.set_page_load_timeout(30)
driver.implicitly_wait(30)
driver.get("https://sdotbhowmik.github.io")

# Assert using condition

# Assert with error message
assert driver.title == "SKB Portfolio", "Title should be 'SKB Portfolio'"

# Assert using in
assert "SKB Portfolio" in driver.title

#AssertIs
assertIs ("SKB Portfolio", driver.title, "Title should be 'SKB Portfolio")


print("Test passed")
driver.close()
driver.quit()