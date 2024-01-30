from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

class input_button():
    f = open("e.txt", "r")
    para=f.read()
    def demo_input_button(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        # Use the correct file path with the file:// protocol
        file_path = "file://C:\\python-selenium\Practise\BasicFields\Input_and_Button.html"
        driver.get(file_path)
        time.sleep(5)
        driver.maximize_window()
        inp = driver.find_element(By.XPATH, "//input[@id='inputField']")
        inp.send_keys(input_button.para)
        v1=inp.get_attribute("value")
        print(len(v1))
        if v1 == "Hars":
            print("Test Case is Passed for getAttribute()")
        else:
            print(f"Test Case is Failed for getAttribute(), Actual:{v1}, Expected:{'Hars'}")
        dip=driver.find_element(By.XPATH,"//input[@id='inputField']").is_displayed()
        print(f"Test Case is Passed for is_displayed(),Actual:{dip},Expected:{'True'}")
        if len(v1) > 0:
            var1=driver.find_element(By.XPATH, "//button[normalize-space()='Submit']").is_enabled()
            print(f"Test Case is Pass for Button is Enabled , Actual:{var1},Expected:{'True'}")
            time.sleep(2)
            driver.find_element(By.XPATH, "//button[normalize-space()='Submit']").click()
            time.sleep(2)
        else:
            var2 = driver.find_element(By.XPATH, "//button[normalize-space()='Submit']").is_enabled()
            print(f"Test Case is  Failed for Button is Enabled,Actual:{var2},Expected:{'True'}")
            driver.find_element(By.XPATH, "//button[normalize-space()='Submit']").click()
            time.sleep(2)



        time.sleep(2)
        driver.switch_to.alert.accept()
        print("Test Case 3:Switch To Alert:Pass")
        driver.close()

ib = input_button()
ib.demo_input_button()
