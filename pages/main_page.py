from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def go_to_basket_from_main_page(self):
        basket = self.browser.find_element(*MainPageLocators.FIND_BASKET)
        basket.click()

    def wait_not_product_in_basket(self):
        assert self.is_not_element_present(*MainPageLocators.ITEM_IN_BASKET), "Items must not be"

    def wait_basket_is_empty(self):
        empty = self.browser.find_element(*MainPageLocators.BASKET_IS_EMPTY)
        return empty
