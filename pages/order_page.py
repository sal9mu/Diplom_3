import allure
from locators.locators import MainPageLocatores
from locators.locators import ListOrderLocatores
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Подождать пока исчезнет оверлей')
    def wait_for_overlay_is_hidden(self):
        self.wait_for_element_hidden(MainPageLocatores.overlay)

    @allure.step('Подождать появления заголовка страницы')
    def wait_for_orders_page_label(self):
        self.wait_visibility_of_element(ListOrderLocatores.list_order_label)

    @allure.step('Проверить общий счетчик заказов')
    def get_counter_all_orders(self):
        return self.get_counter_value(ListOrderLocatores.counter_total_orders)

    @allure.step('Проверить счетчик заказов за текущий день')
    def get_counter_order_today(self):
        return self.get_counter_value(ListOrderLocatores.counter_daily_order)

    @allure.step('Получить список активных заказов')
    def check_number_of_order(self):
        return self.get_page_text(ListOrderLocatores.order_in_line)

    @allure.step('Нажать на кнопку "Конструктор"')
    def click_on_constructor_button(self):
        self.click_on_element(MainPageLocatores.constructor_button)

    @allure.step('Получение заголовка страницы')
    def check_page_label(self):
        return self.check_displaying_of_element(ListOrderLocatores.list_order_label)

    @allure.step('Получить номер заказа "В работе"')
    def get_order_in_line(self):
        return self.get_counter_value(ListOrderLocatores.order_in_line)
