import time

from util import URLs
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
act = ActionChains(driver)


def select_all_copy_tab_paste():
    driver.get(URLs.TEST_AUTOMATION)
    name = driver.find_element(By.ID, "name")
    email = driver.find_element(By.ID, "name")
    name.send_keys("type something ")

    # NOTE: key_down() needs to pair with key_up(), else the key_down key will always be there
    # but this also means I could perform ctrl+A and ctrl+C as follows

    # Keyboard action: ctrl + A, ctrl + C
    act.key_down(Keys.CONTROL).send_keys("ac").key_up(Keys.CONTROL).perform()
    # Keyboard action: Tab
    act.send_keys(Keys.TAB).perform()
    # Keyboard action: ctrl + V
    act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

    assert name.get_attribute("value") == email.get_attribute("value")


if __name__ == "__main__":
    select_all_copy_tab_paste()
