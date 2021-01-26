from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import allure


@allure.title('Бесполезный сценарий')
@allure.severity(severity_level='blocker')
def test_duckduckgo():
    driver = webdriver.Chrome()
    driver.maximize_window()

    with allure.step('Открытие поисковика'):
        driver.get('https://duckduckgo.com/')

    with allure.step('Поиск N+1'):
        search_input = driver.find_element_by_xpath('//input[@id="search_form_input_homepage"]')
        search_input.send_keys('n+1')
        search_button = driver.find_element_by_xpath('//input[@id="search_button_homepage"]')
        search_button.click()

    with allure.step('Проверка кол-ва результатов поиска'):
        search_results = driver.find_elements_by_xpath('//div[@id="links"]/div[@class="result results_links_deep highlight_d result--url-above-snippet"]')
        assert len(search_results) == 10

    with allure.step('Открытие первой ссылки в новом окне'):
        a = search_results[0].find_element_by_xpath('.//div/h2/a')
        link = a.get_attribute('href')
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        driver.get(link)
    with allure.step('Проверка тайтла'):
        assert driver.title == 'N+1: научные статьи, новости, открытия'
