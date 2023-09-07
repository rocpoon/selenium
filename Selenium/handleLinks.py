import httpx
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# Setup Driver and WebDriverWait
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 3)

url = "https://testautomationpractice.blogspot.com/"
dead_links_home = "http://www.deadlinkcity.com/"



def httpx_check(driver):
    count_400_plus = 0
    all_a = driver.find_elements(By.TAG_NAME, 'a')
    for a in all_a:
        url = a.get_attribute('href')
        if url:
            print(a.text, end=': ')
            try:
                response = httpx.get(a.get_attribute('href'))
            except httpx.RequestError as exc:
                print(f"\n\t*** An error occurred while requesting: {exc.request.url!r}. ***")
                continue

            if response.status_code >= 400:
                print(f"{response.status_code} Invalid link: {url}")
                count_400_plus += 1
            else:
                print(f"{response.status_code} Valid link: {url}")
    print(f"Total of {count_400_plus} 400+ responses")
    driver.quit()



if __name__ == "__main__":
    driver.get(dead_links_home)
    # //button[text()="New Browser Window"]
    # new_browser_link = driver.find_element(By.PARTIAL_LINK_TEXT, "New Browser")
    # print(new_browser_link.text)
    httpx_check(driver)


