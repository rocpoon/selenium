from . import URLs

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 7)


def login_orange_hrm():
    driver.get(URLs.ORANGE_HRM_LOGIN)
    credentials = wait.until(EC.visibility_of_all_elements_located(
        (By.XPATH, "//div[contains(@class, 'orangehrm-demo-credentials')]/p")
    ))
    username = credentials[0].text.split()[-1]
    password = credentials[1].text.split()[-1]
    # print(username, password)

    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.XPATH, "//button[contains(@class, 'orangehrm-login-button')]").click()

    header_div = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'header-title')]")))
    # print(header_div.text)
    assert header_div.text == "Dashboard"

    return driver
