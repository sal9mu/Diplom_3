import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage



class TestTransitionOnOrdersListButton():
    @allure.title('Проверка перехода по кнопке "Лента заказов" в хэдере')
    def test_transition_on_list_orders_button(self, driver):
        with allure.step("Открытие главной страницы"):
            main_page = MainPage(driver)
        with allure.step("Ожидание закрытия оверлея"):
            main_page.wait_for_overlay_is_hidden()
        with allure.step("Нажатие на кнопку 'Лента заказов' в хэдере"):
            main_page.click_on_list_an_order_button()
            order_page = OrderPage(driver)
        with allure.step("Ожидание закрытия оверлея"):
            order_page.wait_for_overlay_is_hidden()
        with allure.step("Ожидание появления названия страницы"):
            order_page.wait_for_orders_page_label()
        with allure.step("Проверка отображения названия страницы 'Лента заказов'"):
            assert order_page.check_page_label()
