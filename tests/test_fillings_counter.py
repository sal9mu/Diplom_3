import pytest
import allure
from pages.main_page import MainPage


class TestFillingsCounter():
    @allure.title('Проверка что счетчик ингредиента увеличивается при добавлении')
    def test_fillings_counter_is_increasing(self, driver):
        with allure.step("Открытие главной страницы"):
            main_page = MainPage(driver)
        with allure.step("Ожидание закрытия оверлея"):
            main_page.wait_for_overlay_is_hidden()
        with allure.step("Проверка названия страницы"):
            main_page.check_page_label()
        with allure.step("Проверка отображения счетчика ингредиента"):
            main_page.wait_for_count_of_ingredients()
        with allure.step('Получение значения счетчика ингредиента до добавления'):
            initial_count = main_page.get_ingredient_counter()
        with allure.step("Добавление ингредиента в корзину"):
            main_page.drag_and_drop_buns()
        with allure.step("Проверка отображения счетчика ингредиента"):
            main_page.wait_for_count_of_ingredients()
        with allure.step('Получение значения счетчика ингредиента после добавления'):
            final_count = main_page.get_ingredient_counter()
        with allure.step("Проверка что счетчик ингредиента увеличился"):
            assert initial_count < final_count
