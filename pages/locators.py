from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    FIND_BASKET = (By.XPATH, "//span/a[contains(@href, '/basket/')]")
    ITEM_IN_BASKET = (By.CSS_SELECTOR, "basket-items")
    BASKET_IS_EMPTY = (By.XPATH, "//p/a[contains(@href, '/')]")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    NAME_TO_PRODUCT = (By.CSS_SELECTOR, ".product_main>h1")
    PRICE_TO_PRODUCT = (By.CSS_SELECTOR, "div.product_main>.price_color")
    NAME_TO_PUSH = (By.CSS_SELECTOR, "#messages>div:nth-child(1) strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages :nth-child(1)")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
