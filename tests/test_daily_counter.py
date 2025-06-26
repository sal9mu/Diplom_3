import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage



class TestDailyCounter():
    @allure.title('Проверка увеличения счетчика "Выполнено за все время"')
    def test_daily_counter_increased(self, login, driver):
        with allure.step("Открытие главной страницы"):
            main_page = MainPage(login)
        with allure.step("Ожидание закрытия оверлея"):
            main_page.wait_for_overlay_is_hidden()
        with allure.step("Переход на страницу 'Лента заказов'"):
            main_page.click_on_list_an_order_button()
            order_page = OrderPage(driver)
        with allure.step("Ожидание закрытия оверлея"):
            order_page.wait_for_overlay_is_hidden()
        with allure.step("Получить количества заказов за сегодня"):
            initial_count = order_page.get_counter_order_today()
        with allure.step("Переход на страницу конструктора бургера"):
            order_page.click_on_constructor_button()
        with allure.step("Ожидание закрытия оверлея"):
            order_page.wait_for_overlay_is_hidden()
        with allure.step("Добавление булочки в корзину"):
            main_page.drag_and_drop_buns()
        with allure.step("Переход в раздел с соусами"):
            main_page.scroll_to_sauce()
        with allure.step("Добавление соуса в корзину"):
            main_page.drag_and_drop_sauce()
        with allure.step("Переход к разделу с начинкой"):
            main_page.scroll_to_filling()
        with allure.step("Добавление начинки в корзину"):
            main_page.drag_and_drop_filling()
        with allure.step("Нажать кнопку 'Оформить заказ'"):
            main_page.click_on_make_an_order_button()
        with allure.step('Ожидание окна успешного создания заказа'):
            main_page.wait_for_successful_order_window()
        with allure.step("Ожидание закрытия оверлея"):
            main_page.wait_for_overlay_is_hidden()
        with allure.step('Подождать пока кнопка закрытия окна будет кликабельна'):
            main_page.wait_for_close_button_is_clickable()
        with allure.step("Закрыть всплывающее окно с номером заказа"):
            main_page.close_successful_order_window()
        with allure.step('Ожидание закрытия оверлея'):
            main_page.wait_for_overlay_is_hidden()
        with allure.step('Подождать пока кнопка "Лента заказов" будет кликабельна'):
            main_page.wait_for_button_list_of_order_is_clickable()
        with allure.step("Переход на страницу 'Лента заказов'"):
            main_page.click_on_list_an_order_button()
        with allure.step("Ожидание закрытия оверлея"):
            order_page.wait_for_overlay_is_hidden()
        with allure.step("Получить количества заказов за сегодня"):
            final_count = order_page.get_counter_order_today()
        with allure.step("Проверить что общее число заказов увеличилось"):
            assert initial_count < final_count
