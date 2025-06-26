import allure
from locators.locators import MainPageLocatores
from locators.locators import ListOrderLocatores
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Подождать пока исчезнет оверлей')
    def wait_for_overlay_is_hidden(self):
        self.wait_for_element_hidden(MainPageLocatores.overlay)

    @allure.step('Подождать появления названия страницы "Соберите бургер"')
    def wait_for_page_logo(self):
        self.wait_visibility_of_element(MainPageLocatores.create_burger_label)

    @allure.step('Получение заголовка страницы')
    def check_page_label(self):
        self.get_page_text(MainPageLocatores.create_burger_label)

    @allure.step('Скролл до раздела с соусами')
    def scroll_to_sauce(self):
        self.scroll_to_element(MainPageLocatores.sauce_spicy_x)

    @allure.step('Скролл до раздела с начинкой')
    def scroll_to_filling(self):
        self.scroll_to_element(MainPageLocatores.beef_meteorite)

    @allure.step('Нажать кнопку "Оформить заказ"')
    def click_on_make_an_order_button(self):
        self.click_on_element(MainPageLocatores.make_an_order_button)

    @allure.step('Перетащить булку в корзину')
    def drag_and_drop_buns(self):
        source = self.driver.find_element(*MainPageLocatores.flur_buns)
        target = self.driver.find_element(*MainPageLocatores.constructor_basket)
        self.drag_and_drop_element(source, target)

    @allure.step('Перетащить соус в корзину')
    def drag_and_drop_sauce(self):
        source = self.driver.find_element(*MainPageLocatores.sauce_spicy_x)
        target = self.driver.find_element(*MainPageLocatores.constructor_basket)
        self.drag_and_drop_element(source, target)

    @allure.step('Перетащить начинку в корзину')
    def drag_and_drop_filling(self):
        source = self.driver.find_element(*MainPageLocatores.beef_meteorite)
        target = self.driver.find_element(*MainPageLocatores.constructor_basket)
        self.drag_and_drop_element(source, target)

    @allure.step('Открыть всплывающее окно с деталями')
    def click_on_bun_for_details(self):
        self.click_on_element(MainPageLocatores.flur_buns)

    @allure.step('Проверка отображения окна с деталями')
    def check_details_window(self):
        self.check_displaying_of_element(MainPageLocatores.ingredients_details)

    @allure.step('Закрыть всплывающее окно с деталями')
    def close_details_window(self):
        self.click_on_element(MainPageLocatores.close_ing_details_button)

    @allure.step('Проверка что всплывающее окно с деталями закрыто')
    def check_details_window_is_close(self):
        self.wait_for_element_hidden(MainPageLocatores.ingredients_details)

    @allure.step('Нажать на кнопку "Лента заказов"')
    def click_on_list_an_order_button(self):
        self.click_on_element(MainPageLocatores.list_an_order_button)

    @allure.step('Подождать появления названия страницы "Лента заказов"')
    def wait_for_list_an_order_logo(self):
        self.wait_visibility_of_element(ListOrderLocatores.list_order_label)

    @allure.step('Нажать на кнопку "Конструктор"')
    def click_on_constructor_button(self):
        self.click_on_element(MainPageLocatores.constructor_button)

    @allure.step('Подождать появления счетчика ингредиента')
    def wait_for_count_of_ingredients(self):
        self.wait_visibility_of_element(MainPageLocatores.ingredient_indicator)

    @allure.step('Получить текущее значение счетчика')
    def get_ingredient_counter(self):
        counter = self.driver.find_element(*MainPageLocatores.ingredient_indicator)
        return int(counter.text)

    @allure.step('Ожидание окна успешного заказа')
    def wait_for_successful_order_window(self):
        self.wait_visibility_of_element(MainPageLocatores.window_of_create_order)

    @allure.step('Ожидание кнопки закрытия всплывающего окна')
    def wait_for_close_button_is_clickable(self):
        self.wait_element_to_be_clickable(MainPageLocatores.close_window_create_order_button)

    @allure.step('Закрытие окна успешного заказа')
    def close_successful_order_window(self):
        self.click_on_element(MainPageLocatores.close_window_create_order_button)

    @allure.step('Нажать кнопку Войти в аккаунт')
    def click_on_login_button(self):
        self.click_on_element(MainPageLocatores.login_account_button)

    @allure.step('Получить номер созданного заказа')
    def get_number_of_created_order(self):
        return self.get_counter_value(MainPageLocatores.number_of_created_order)

    @allure.step('Подождать пока кнопка "Войти" будет кликабельна.')
    def wait_for_login_button(self):
        self.wait_element_to_be_clickable(MainPageLocatores.login_account_button)

    def wait_for_button_list_of_order_is_clickable(self):
        self.wait_element_to_be_clickable(MainPageLocatores.list_an_order_button)
