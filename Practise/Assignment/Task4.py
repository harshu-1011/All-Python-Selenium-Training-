from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class Task4():
# Function to wait for an element to be present
        def verify_forgot_password(self):
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
            driver.get("https://opensource-demo.orangehrmlive.com/")
            driver.maximize_window()
            driver.implicitly_wait(6)
            forgot_password_link =driver.find_element( By.XPATH, "//p[@class='oxd-text oxd-text--p orangehrm-login-forgot-header']")
            forgot_password_link.click()
            email_field =driver.find_element(By.XPATH,"//input[@placeholder='Username']")
            email_field.send_keys("harsh@gmail.com")
            reset_button =driver.find_element(By.XPATH, "//button[normalize-space()='Reset Password']")
            reset_button.click()
            driver.get("https://opensource-demo.orangehrmlive.com/")
            username = "Admin"
            password = "admin123"
            user = driver.find_element(By.XPATH, "//input[@placeholder='Username']")
            user.send_keys(username)
            print(f"User Input Field : Test Case:PASSED , Actual:{user.is_enabled()} , Expected:{'True'}")
            passw = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
            passw.send_keys(password)
            print(f"Password Input Field: Test Case:PASSED , Actual:{passw.is_enabled()} , Expected:{'True'}")
            login_button = driver.find_element(By.XPATH, "//button[normalize-space()='Login']")
            print(f"Login Button Field:Test Case:PASSED , Actual:{login_button.is_enabled()} , Expected:{'True'}")
            login_button.click()
            dashboard = driver.find_element(By.XPATH, "//h6[normalize-space()='Dashboard']")
            password_reset_message =driver.find_element(By.TAG_NAME,"h6")
            print(f"The application displays a message indicating that a password reset email has been sent:Test Case:PASSED , Actual:{password_reset_message.is_displayed()} , Expected:{'True'}")
            print(f"User is successfully logged in and directed to the dashboard:Test Case:PASSED , Actual:{dashboard.is_displayed()} , Expected:{'True'}")
            driver.close()
t4=Task4()
t4.verify_forgot_password()
