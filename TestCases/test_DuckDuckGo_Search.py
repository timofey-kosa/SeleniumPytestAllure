from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import allure
import pytest
from test_fixture1 import browser


@allure.title('Бесполезный сценарий')
@allure.severity(severity_level='blocker')

class Test1():
    @pytest.mark.regression
    def test_duckduckgo(self, browser):
        with allure.step('Открытие поисковика'):
            browser.get('https://duckduckgo.com/')

        with allure.step('Поиск N+1'):
            search_input = browser.find_element_by_xpath('//input[@id="search_form_input_homepage"]')
            search_input.send_keys('n+1')
            search_button = browser.find_element_by_xpath('//input[@id="search_button_homepage"]')
            search_button.click()

        with allure.step('Проверка кол-ва результатов поиска'):
            search_results = browser.find_elements_by_xpath('//div[@id="links"]/div[@class="result results_links_deep highlight_d result--url-above-snippet"]')
            assert len(search_results) == 10

        with allure.step('Открытие первой ссылки в новом окне'):
            a = search_results[0].find_element_by_xpath('.//div/h2/a')
            link = a.get_attribute('href')
            browser.execute_script("window.open('');")
            browser.switch_to.window(browser.window_handles[1])
            browser.get(link)
        with allure.step('Проверка тайтла'):
            assert browser.title == 'N+1: научные статьи, новости, открытия'
