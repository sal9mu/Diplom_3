import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage



class TestTransitionOnConstructorButton():
    @allure.title('Проверка перехода по кнопке "Конструктор" в хэдере')
    def test_transition_on_constructor_button(self, driver):
        with allure.step("Открытие главной страницы"):
            main_page = MainPage(driver)
        with allure.step("Ожидание закрытия оверлея"):
            main_page.wait_for_overlay_is_hidden()
        with allure.step("Нажатие на кнопку 'Лента заказов' в хэдере"):
            main_page.click_on_list_an_order_button()
            order_page = OrderPage(driver)
        with allure.step("Ожидание закрытия оверлея"):
            order_page.wait_for_overlay_is_hidden()
        with allure.step("Нажатие на кнопку 'Конструктор' в хэдере"):
            order_page.click_on_constructor_button()
        with allure.step("Ожидание появления названия страницы"):
            main_page.wait_for_page_logo()
        with allure.step("Проверка отображения названия страницы 'Соберите бургер'"):
            assert main_page.check_page_label
