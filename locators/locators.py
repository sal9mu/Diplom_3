from selenium.webdriver.common.by import By


class MainPageLocatores:
    login_account_button = (By.XPATH, "//button[text() = 'Войти в аккаунт']")  # кнопка "Войти в аккаунт"
    constructor_button = (By.XPATH, "//a[@class='AppHeader_header__link__3D_hX' and @href='/']") # Кнопка Конструктор
    stellar_burgers_label = (By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']/a[@href='/']")  # Логотип Stellar Burgers
    list_an_order_button = (By.XPATH, "//a[@class='AppHeader_header__link__3D_hX' and @href='/feed']") # Кнопка Лента заказов
    ingredients_details = (By.XPATH, "//div[@class='Modal_modal__contentBox__sCy8X pt-10 pb-15']") # Окно описания ингредиента
    close_ing_details_button = (By.XPATH, "//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']") # Кнопка закрытия описания ингредиента
    ingredient_counter = (By.XPATH, "//p[@class='counter_counter__num__3nue1']") # Счетчик ингредиента
    constructor_basket = (By.CSS_SELECTOR, "ul[class*='BurgerConstructor_basket__list__l9dp_']") # Корзина заказа
    make_an_order_button = (By.XPATH, "//button[text() = 'Оформить заказ']")  # кнопка Оформления заказа
    overlay = (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div") # Прогрузка страницы
    choose_sauces_section = (By.XPATH, "//div[contains(@class, 'tab')]//span[text()='Соусы']")  # Переход к разделу выбора соусов
    choose_fillings_section = (By.XPATH, "//div[contains(@class, 'tab')]//span[text()='Начинки']")  # Переход к разделу выбора начинки
    flur_buns = (By.CSS_SELECTOR, "img[alt='Флюоресцентная булка R2-D3']") # Флюоресцентная булочка
    sauce_spicy_x = (By.CSS_SELECTOR, "img[alt='Соус Spicy-X']") # Соус Spicy-X
    beef_meteorite = (By.CSS_SELECTOR, "img[alt='Говяжий метеорит (отбивная)']") # Начинка Говяжий метеорит
    create_burger_label = (By.XPATH, "//h1[text() = 'Соберите бургер']") # Надпись Соберите бургер
    window_of_create_order = (By.XPATH, "//div[@class='Modal_modal__contentBox__sCy8X pt-30 pb-30']") # Окно с номером заказа
    number_of_created_order = (By.XPATH, "//div[@class='Modal_modal__contentBox__sCy8X pt-30 pb-30']/h2[contains(@class, 'Modal_modal__title_shadow__3ikwq')]")
    close_window_create_order_button = (By.CLASS_NAME, "Modal_modal__close_modified__3V5XS") # Кнопка закрытия окна успешного создания заказ


class LoginPageLocatores:
    email_input = (By.XPATH, "//label[text() = 'Email']/following-sibling::input")  # поле ввода Email
    password_input = (By.XPATH, "//label[text() = 'Пароль']/following-sibling::input")  # поле ввода Пароль
    login_button = (By.XPATH, "//button[text() = 'Войти']")  # кнопка Войти

class ListOrderLocatores:
    list_order_label = (By.XPATH, "//h1[text()='Лента заказов']") # Надпись "Лента заказов"
    order_in_line = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady__1YFem')]/li[@class='text text_type_digits-default mb-2']") # Поле с заказами в работе
    counter_total_orders = (By.XPATH, ".//div[@class='undefined mb-15']/p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']") # Счетчик заказов общий
    counter_daily_order = (By.XPATH, ".//p[text()='Выполнено за сегодня:']/following-sibling::p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']") # Счетчик сегодняшних заказов


