import pytest
import allure
from pages.main_page import MainPage



class TestCheckDetailsWindow():
    @allure.title('Проверка появления окна описания ингредиента')
    def test_check_details_window(self, driver):
        with allure.step("Открытие главной страницы"):
            main_page = MainPage(driver)
        with allure.step("Ожидание закрытия оверлея"):
            main_page.wait_for_overlay_is_hidden()
        with allure.step("Нажатие на булочку"):
            main_page.click_on_bun_for_details()
        with allure.step("Проверка отображения окна с деталями ингредиента"):
            assert main_page.check_details_window()
