import allure
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seletools.actions import drag_and_drop


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Подождать появления элемента')
    def wait_visibility_of_element(self, locator):
        return WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located(locator))

    @allure.step('Нажать на элемент')
    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Получить заголовок страницы')
    def get_element_text(self, locator, time=10):
        element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))
        return element.text

    @allure.step('Проверка отображения элемента')
    def check_displaying_of_element(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    @allure.step('Подождать пока элемент станет невидимым')
    def wait_for_element_hidden(self, locator):
        WebDriverWait(self.driver, timeout=10).until(EC.invisibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Перетащить элемент в корзину')
    def drag_and_drop_element(self, source_locator, target_locator):
        source = self.driver.find_element(*source_locator)
        target = self.driver.find_element(*target_locator)
        drag_and_drop(self.driver, source, target)

    @allure.step('Заполнить поле')
    def send_keys_to_input(self, locator, data):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(data)

    def wait_element_to_be_clickable(self, locator):
        return WebDriverWait(self.driver, timeout=10).until(EC.element_to_be_clickable(locator))

    def get_counter_value(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element.text

    @allure.step('Скролл до элемента')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)
