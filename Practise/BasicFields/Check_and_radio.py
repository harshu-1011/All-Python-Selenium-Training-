import colorama
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

class Check_Radio():
    f = open("e.txt", "r")
    para=f.read()
    def demo_check_radio(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


        file_path = "file://C:\python-selenium\Practise\BasicFields\Check_and_Radio.html"
        driver.get(file_path)
        driver.maximize_window()
        driver.implicitly_wait(10)
        ele=driver.find_element(By.XPATH,"//input[@id='inputField']")
        print(ele.get_attribute("value"))
        ele.send_keys(Check_Radio.para)
        re=ele.is_displayed()
        if re:
            print("Test Case is PASSED for isDisplayed()  Input Field",re)
        else:
            print("Test Case is FAILED for is_Displayed() Input Field",re)
        time.sleep(2)
        kew=ele.get_attribute("value")
        print(kew)
        ch1=driver.find_element(By.ID,"checkboxField")
        ch1.click()
        res1=ch1.is_selected()
        if res1:
            print("Test Case is Passed for CheckBox ",res1)
        else:
            print("Test Case is Failed for CheckBox ",res1)
        ch2=driver.find_element(By.ID,"checkboxField1")
        ch2.click()
        res2=ch2.is_selected()
        if res2:
            print("Test Case is PASSED for CheckBox 1",res2)
        else:
            print("Test Case is FAILED for CheckBox 1",res2)

        driver.close()
cr=Check_Radio()
cr.demo_check_radio()
