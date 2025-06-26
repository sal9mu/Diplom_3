import allure
from selenium import webdriver
from locators.locators import MainPageLocatores
from locators.locators import LoginPageLocatores
from pages.base_page import BasePage
from helpers.data import UserData


class LoginPage(BasePage):
    @allure.step('Заполнить поле email')
    def email_input(self):
        self.send_keys_to_input(LoginPageLocatores.email_input, UserData.email)

    @allure.step('Заполнить поле password')
    def password_input(self):
        self.send_keys_to_input(LoginPageLocatores.password_input, UserData.password)
    @allure.step('Подождать пока кнопка Войти будет активной')
    def wait_login_button_to_be_clickable(self):
        self.wait_element_to_be_clickable(LoginPageLocatores.login_button)

    @allure.step('Нажать кнопку Войти')
    def click_login_button(self):
        self.click_on_element(LoginPageLocatores.login_button)





