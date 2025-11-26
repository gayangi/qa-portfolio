from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# First Selenium Test
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://example.com")
assert "Example" in driver.title
driver.quit()