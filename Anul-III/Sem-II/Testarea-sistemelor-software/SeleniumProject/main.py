import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("http://demo.automationtesting.in/Windows.html")

print(driver.title)
print(driver.current_url)
driver.find_element(by=By.XPATH, value="//*[@id=\"Tabbed\"]/a/button").click()
time.sleep(5)
print(driver.title)
print(driver.current_url)
# print(driver.page_source)

driver.close()
# driver.quit()
