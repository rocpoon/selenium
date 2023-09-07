# Basic webdriver and By selector
import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By

# Wait support for explicit wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.select import Select

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

test_automation = "https://testautomationpractice.blogspot.com/"
open_cart = "https://www.opencart.com/index.php?route=account/register"


def select_dropdown(driver):
    if driver.current_url != test_automation:
        driver.get(test_automation)

    # Create a Select object by passing web element with <select> tag
    country_dropdown = Select(driver.find_element(By.XPATH, "//select[@id='country']"))
    print(len(country_dropdown.options))

    # Different ways to select the select options
    country_dropdown.select_by_index(0)
    print(country_dropdown.first_selected_option.text)

    country_dropdown.select_by_value("japan")
    print(country_dropdown.first_selected_option.text)

    country_dropdown.select_by_visible_text("United Kingdom")
    print(country_dropdown.first_selected_option.text)

    # Check for single select dropdown, only last selected option displayed
    # By checking there is only total 1 option selected with the correct text
    selected_options = country_dropdown.all_selected_options
    print(selected_options)
    assert len(selected_options) == 1
    assert selected_options[0].text == "United Kingdom"

    return driver

def select_checkbox(driver):
    if driver.current_url != test_automation:
        driver.get(test_automation)
    # # Find all day checkbox elements, select all of them and verify all day element is selected
    # days_checkboxes = driver.find_elements(By.XPATH, '//*[text()="Days:"]/following-sibling::div/input')
    # for day in days_checkboxes:
    #     day.click()
    #
    # for day in days_checkboxes:
    #     assert day.is_selected()
    #
    return driver

def select_date(driver):
    if driver.current_url != test_automation:
        driver.get(test_automation)
    date = driver.find_element(By.XPATH, "//input[@id='datepicker']")
    date.click()
    today = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'ui-state-highlight')]")))
    today.click()
    # Verify today's date is displayed on date input field
    assert date.get_attribute("value") == datetime.now().strftime('%m/%d/%Y')
    return driver

def select_form(driver):
    if driver.current_url != test_automation:
        driver.get(test_automation)
    # Find Green options in color and select it
    green_option = driver.find_element(By.XPATH, "//select[@id='colors']/option[@value='green']")
    green_option.click()
    assert green_option.is_selected()

    # Find Color Select tag and select ALL colors
    color_select = Select(driver.find_element(By.XPATH, "//select[@id='colors']"))
    for color_option in color_select.options:
        if not color_option.is_selected():
            print(f"Color option to select: {color_option.text}")
            color_option.click()

    for selected_option in color_select.all_selected_options:
        print(f"Color option remain selected: {selected_option.text}")

    return driver


if __name__ == "__main__":
    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 3)
    print(f"Current_url Before get: {driver.current_url}")
    driver.get(open_cart)
    driver = select_form(driver)



    # time.sleep(3)
    driver.quit()
