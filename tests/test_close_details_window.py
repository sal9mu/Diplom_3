import pytest
import allure
from pages.main_page import MainPage


class TestCloseDetailsWindow():
    @allure.title('Проверка закрытия окна описания ингредиента')
    def test_check_details_window(self, driver):
        with allure.step("Открытие главной страницы"):
            main_page = MainPage(driver)
        with allure.step("Ожидание закрытия оверлея"):
            main_page.wait_for_overlay_is_hidden()
        with allure.step("Нажатие на булочку"):
            main_page.click_on_bun_for_details()
        with allure.step("Проверка отображения окна описания ингредиента"):
            main_page.check_details_window()
        with allure.step("Закрытие окна описания ингредиента"):
            main_page.close_details_window()
        with allure.step("Проверка что окно описания закрыто"):
            assert main_page.check_details_window_is_close
