import time
from datetime import datetime

## Basic webdriver and By selector
from selenium import webdriver
from selenium.webdriver.common.by import By

## Wait support for explicit wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

## Unique webElement
from selenium.webdriver.support.select import Select

test_automation = "https://testautomationpractice.blogspot.com/"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

if __name__ == "__main__":
    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 3)
    print(f"Current_url Before get(): {driver.current_url}")
    driver.get(test_automation)
    print(f"Current_url After get(): {driver.current_url}")

    alert_list = ["Alert", "Confirm Box", "Prompt"]
    alert_button = driver.find_element(By.XPATH, f"//button[text()='{alert_list[1]}']")
    alert_button.click()

    # When an alert is on the webpage, use "switch_to" function on driver
    alert_window = driver.switch_to.alert
    ### Messages on Alert window
    print(alert_window.text)

    # ### Input text into prompt text field
    # alert_window.send_keys("Check it out")

    ### Click on Cancel button
    alert_window.dismiss()

    # ### Click on Ok button
    # alert_window.accept()

    # demo = driver.find_element(By.XPATH, "//p[@id='demo']")
    # print(demo.text)

    time.sleep(2)
    driver.quit()