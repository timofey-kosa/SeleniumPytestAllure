import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

links = [
"https://stepik.org/lesson/236895/step/1",
"https://stepik.org/lesson/236896/step/1",
"https://stepik.org/lesson/236897/step/1",
"https://stepik.org/lesson/236898/step/1",
"https://stepik.org/lesson/236899/step/1",
"https://stepik.org/lesson/236903/step/1",
"https://stepik.org/lesson/236904/step/1",
"https://stepik.org/lesson/236905/step/1",
]

answer = math.log(int(time.time()))


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('slink', links)
def test_guest_should_see_login_link(browser, slink):
    link = f"{slink}"
    browser.get(link)
    a = WebDriverWait(browser, 10).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, '.textarea')))
    field = browser.find_element_by_css_selector('.textarea')
    field.send_keys(str(math.log(int(time.time()))))
    submit_button = browser.find_element_by_xpath('//*[@class="submit-submission"]')
    submit_button.click()
    b = WebDriverWait(browser, 10).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint")))
    text = browser.find_element_by_xpath('//*[@class="smart-hints__hint"]').text
    assert text == "Correct!"






