from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Create Chrome webdriver with specific options
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10)

URL_WITH_FRAME = "https://docs.oracle.com/javase/8/docs/api/"
TEST_AUTOMATION_URL = "https://testautomationpractice.blogspot.com/"


def switch_frame_test():
    driver.get(URL_WITH_FRAME)
    PACKAGE_NAME = "java.applet"

    # You can switch to frame by frame's index, name, or webelement
    # classFrame = driver.find_element(By.XPATH, "//*[@name='classFrame']")
    driver.switch_to.frame('classFrame')
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@name='trustarc_cm']")))
    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Accept all']"))).click()
    driver.switch_to.default_content()

    # Find the frame and switch_to.frame
    driver.switch_to.frame("packageListFrame")
    driver.find_element(By.LINK_TEXT, PACKAGE_NAME).click()
    driver.switch_to.default_content()

    # Verify packageFrame is updated based on the above action
    driver.switch_to.frame("packageFrame")
    frame_title = wait.until(EC.visibility_of_element_located((By.XPATH, "//h1/a")))
    assert frame_title.text == PACKAGE_NAME


def switch_window_test():
    driver.get(TEST_AUTOMATION_URL)

    print("Check window handles before opening a new one")
    print(driver.window_handles)

    # Open a new window
    driver.find_element(By.XPATH, "//button[text()='New Browser Window']").click()

    print("***Switch to newly opened window")
    # Latest created window will always be the last in the list
    driver.switch_to.window(driver.window_handles[-1])

    print("Check window handles after opening a new one")
    print(driver.window_handles)
    print(driver.current_url)

    print("Perform: Close current focused window")
    driver.close()

    # Initial window will always be the first in the list (If it was not closed)
    print("Check window handles after closing one")
    print(driver.window_handles)

    print("***Switch to first window***")
    driver.switch_to.window(driver.window_handles[0])
    print(driver.current_url)


if __name__ == "__main__":
    # switch_frame_test()
    switch_window_test()

    driver.quit()
