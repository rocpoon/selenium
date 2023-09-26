from util import commonMethods, URLs

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def print_all_hrm_user_status(driver):
    driver.get(URLs.ORANGE_HRM)
    if "dashboard" in driver.current_url:
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Admin"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//i[@class='oxd-icon bi-trash']")))
        records_status = driver.find_elements(By.XPATH, "//div[text()='Status']/following-sibling::div")
        print([record.text for record in records_status])
    else:
        print(f"Please login to {URLs.ORANGE_HRM}")


def bookstore_info(driver):
    driver.get(URLs.TEST_AUTOMATION)
    book_table = driver.find_element(By.NAME, "BookTable")

    # Find all rows in table
    table_rows = book_table.find_elements(By.TAG_NAME, "tr")
    print(f"Number of record rows: {len(table_rows) - 1}")  # minus 1 for header row

    # Find number of columns in table (First row (table_rows[0]) is the column row, so tag name is <th>)
    table_headers = table_rows[0].find_elements(By.TAG_NAME, "th")
    print(f"Number of columns: {len(table_headers)}")

    print()
    # Print everything in the table (Column name and row records)
    for row in table_rows:
        print(row.text)

    # Print records with Author name equal to "Mukesh"
    print(f'\n{table_rows[0].text}')
    for row in table_rows[1:]:
        # Author column is index 1 (2nd column)
        if row.find_elements(By.TAG_NAME, "td")[1].text == "Mukesh":
            print(row.text)


if __name__ == "__main__":
    driver = commonMethods.login_orange_hrm()
    wait = WebDriverWait(driver, 7)
    print_all_hrm_user_status(driver)

    driver.quit()
