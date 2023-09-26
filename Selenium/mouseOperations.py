from util import URLs
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

if __name__ == "__main__":
    driver.get(URLs.TEST_AUTOMATION)
    act = ActionChains(driver)

    # Perform double click action
    double_click_button = driver.find_element(By.XPATH, "//button[text()='Copy Text']")
    copy_from_field = driver.find_element(By.ID, "field1")
    copy_to_field = driver.find_element(By.ID, "field2")
    act.double_click(double_click_button).perform()
    assert copy_to_field.get_attribute('value') == copy_from_field.get_attribute('value')

    # Click and hold element_a and release at element_b location
    draggable = driver.find_element(By.XPATH, "//div[@id='draggable']")
    droppable = driver.find_element(By.XPATH, "//div[@id='droppable']")
    assert droppable.text == "Drop here"
    act.drag_and_drop(draggable, droppable).perform()
    assert droppable.text == "Dropped!"
