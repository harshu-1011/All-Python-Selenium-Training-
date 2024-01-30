from selenium import webdriver
import time
chrome_service=webdriver.chrome.service.Service(executable_path="C:\\browserdriver\\chromedriver-win32\\chromedriver.exe")
driver=webdriver.Chrome(service=chrome_service)
# Above Lines are mandatory to write in every code
driver.get("https://www.google.com")
print(driver.title)
print(driver.current_url)
driver.maximize_window()
time.sleep(5)
input("Press Enter to Exit")


driver.close()