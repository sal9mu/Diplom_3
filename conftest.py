import pytest
from selenium import webdriver
from helpers.data import UserData
from locators.locators import LoginPageLocatores
from urls.url import url
from pages.login_page import LoginPage
from pages.main_page import MainPage
url = url.main_url


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
        driver.set_window_size(1920, 1080)
        driver.get(url)
    elif request.param == "firefox":
        driver = webdriver.Firefox()
        driver.set_window_size(1920, 1080)
        driver.get(url)
    yield driver
    driver.quit()

@pytest.fixture
def login(driver):
    main_page = MainPage(driver)
    login_page = LoginPage(driver)
    main_page.wait_for_login_button()
    main_page.click_on_login_button()
    login_page.email_input()
    login_page.password_input()
    login_page.wait_login_button_to_be_clickable()
    login_page.click_login_button()
    return driver
