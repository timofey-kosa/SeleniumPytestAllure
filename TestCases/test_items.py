import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


def test_languages_should_bee_working(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    time.sleep(10)
    a = WebDriverWait(browser, 10).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".add-to-basket")))
    assert browser. find_element_by_css_selector(".add-to-basket")
