import time

from util import URLs
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
act = ActionChains(driver)


def mouse_double_click():
    driver.get(URLs.TEST_AUTOMATION)
    # Perform double click action
    double_click_button = driver.find_element(By.XPATH, "//button[text()='Copy Text']")
    copy_from_field = driver.find_element(By.ID, "field1")
    copy_to_field = driver.find_element(By.ID, "field2")

    # ActionChain
    act.double_click(double_click_button).perform()
    assert copy_to_field.get_attribute('value') == copy_from_field.get_attribute('value')


def drag_and_drop_01():
    driver.get(URLs.TEST_AUTOMATION)
    # Click and hold element_a and release at element_b location
    draggable = driver.find_element(By.XPATH, "//div[@id='draggable']")
    droppable = driver.find_element(By.XPATH, "//div[@id='droppable']")
    assert droppable.text == "Drop here"

    # ActionChain
    act.drag_and_drop(draggable, droppable).perform()
    assert droppable.text == "Dropped!"


def drag_and_drop_02():
    MULTI_DRAG_AND_DROP = "http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html"
    tuple_list = [('box1', 'box101'), ('box2', 'box102'), ('box3', 'box103'), ('box4', 'box104'),
                  ('box5', 'box105'), ('box6', 'box106'), ('box7', 'box107')]
    driver.get(MULTI_DRAG_AND_DROP)
    for s_id, t_id in tuple_list:
        # ActionChain
        act.drag_and_drop(driver.find_element(By.ID, s_id), driver.find_element(By.ID, t_id)).perform()


def hold_and_move_by_offset():
    driver.get(URLs.JQUERYSCRIPT_SLIDER)
    # Move element by offset(x,y)
    left_slider = driver.find_element(By.XPATH, "//div[@id='slider-range']/span[1]")
    right_slider = driver.find_element(By.XPATH, "//div[@id='slider-range']/span[2]")

    print("Location of element before move")
    print(f"L:{left_slider.location}\nR:{right_slider.location}")

    # ActionChain
    act.drag_and_drop_by_offset(left_slider, 60, 0).perform()
    act.drag_and_drop_by_offset(right_slider, -100, 0).perform()

    print("Location of element after move (L x+60, R x-100)")
    print(f"L:{left_slider.location}\nR:{right_slider.location}")

    expected_result = "Here List of products will be shown which are cost between 2000 and 6800."
    assert driver.find_element(By.ID, "searchResults").text == expected_result


def scroll_by_pixel(x, y):
    driver.get(URLs.TEST_AUTOMATION)
    print(f"Page scroll Y position: {driver.execute_script('return window.pageYOffset')} pixel")

    # Scroll x and y pixel in the page
    driver.execute_script(f"window.scrollTo({x}, {y})")
    y_offset = driver.execute_script('return window.pageYOffset')
    print(f"Page scroll Y position: {y_offset} pixel")
    assert y_offset == y

    # Scroll to the bottom of the page (document.body.scrollHeight --> gives the max scrollHeight)
    driver.execute_script(f"window.scrollTo(0, document.body.scrollHeight)")
    print(f"Page scroll Y position: {driver.execute_script('return window.pageYOffset')} pixel")


def scroll_to_element():
    driver.get(URLs.TEST_AUTOMATION)
    # Scroll to specific element
    target_element = driver.find_element(By.XPATH, "//label[text() = 'Colors:']")
    driver.execute_script("arguments[0].scrollIntoView();", target_element)
    y_offset = driver.execute_script('return window.pageYOffset')
    print(f"Page scroll Y position: {y_offset} pixel")
    print(target_element.location)

    # Check browser indeed scroll to element's location (sometime there will be 1 pixel difference)
    assert y_offset-1 < target_element.location.get('y') < y_offset+1


if __name__ == "__main__":
    # mouse_double_click()
    # drag_and_drop_01()
    # drag_and_drop_02()
    # hold_and_move_by_offset()
    # scroll_by_pixel(0, 300)
    scroll_to_element()

    driver.quit()
