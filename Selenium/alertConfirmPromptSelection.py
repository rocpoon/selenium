import time
from datetime import datetime

## Basic webdriver components (selector and key)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

## Wait support for explicit wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

## Unique webElement
from selenium.webdriver.support.select import Select


TEST_AUTOMATION_URL = "https://testautomationpractice.blogspot.com/"

# Chrome specific options
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)



if __name__ == "__main__":
    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 3)
    driver.get(TEST_AUTOMATION_URL)

    alert_list = ["Alert", "Confirm Box", "Prompt"]
    alert_button = driver.find_element(By.XPATH, f"//button[text()='{alert_list[2]}']")
    alert_button.click()

    # START - Alert Window
    # When an alert is on the webpage, use "switch_to" function on driver
    # *** NOTE: After accept/dismiss an Alert, driver will automatically switch back to the main/original window
    alert_window = driver.switch_to.alert

    ### Messages on Alert window
    print(alert_window.text)

    ### Input text into prompt text field
    ALERT_INPUT = "Kitty"
    alert_window.send_keys(ALERT_INPUT)

    # ### Alert button options: accept(Ok)/dismiss(Cancel)
    alert_window.accept()
    # alert_window.dismiss()
    # END - Alert Window

    # Verify correct alert selection output is displayed in main window
    demo = driver.find_element(By.XPATH, "//p[@id='demo']")
    print(demo.text)
    assert demo.text == f'Hello {ALERT_INPUT}! How are you today?'

    driver.quit()
