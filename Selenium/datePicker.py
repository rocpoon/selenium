from util import URLs

from selenium import webdriver
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

MONTH = {
    "January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6,
    "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12
}


# If datepicker element cannot type the date manually
def change_date_manually(dd, mm, yyyy):
    driver.get(URLs.JQUERYUI_DATEPICKER)
    driver.switch_to.frame(0)

    datepicker = driver.find_element(By.ID, "datepicker")  # mm/dd/yyyy eg. 09/13/2023
    datepicker.click()
    c_mm = MONTH[driver.find_element(By.CLASS_NAME, "ui-datepicker-month").text]
    c_yyyy = driver.find_element(By.CLASS_NAME, "ui-datepicker-year").text

    # Find the number of clicks needed
    click_amount = (yyyy - int(c_yyyy)) * 12
    click_amount += mm - c_mm

    # Find the direction of click
    if click_amount > 0:
        direction = "Next"
    else:
        direction = "Prev"
        click_amount *= -1

    # Go to the correct month/year
    for _ in range(click_amount):
        # This element is dynamically changing everytime it was clicked, thus, find_element is needed for each click
        driver.find_element(By.XPATH, f"//a[@title='{direction}']").click()
    # Select the expected day
    driver.find_element(By.XPATH, f"//td/a[text()={dd}]").click()

    print(f"{mm:02d}/{dd}/{yyyy} ==", datepicker.get_attribute("value"))
    assert f"{mm:02d}/{dd}/{yyyy}" == datepicker.get_attribute("value")


if __name__ == "__main__":
    dd, mm, yyyy = 21, 9, 2023
    change_date_manually(dd, mm, yyyy)





