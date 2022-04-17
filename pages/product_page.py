import math
from .base_page import BasePage
from .locators import ProductPageLocators, MainPageLocators
from selenium.common.exceptions import NoAlertPresentException


class ProductPage(BasePage):
    def go_to_product_page(self):
        self.go_to_product_page()

    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()

    def go_to_basket_from_product_page(self):
        basket = self.browser.find_element(*MainPageLocators.FIND_BASKET)
        basket.click()

    def wait_not_product_in_basket(self):
        assert self.is_not_element_present(*MainPageLocators.ITEM_IN_BASKET), "Items must not be"

    def wait_basket_is_empty(self):
        empty = self.browser.find_element(*MainPageLocators.BASKET_IS_EMPTY)
        return empty

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_product_name(self):
        name_to_product = self.browser.find_element(*ProductPageLocators.NAME_TO_PRODUCT)
        return name_to_product.text

    def should_be_product_price(self):
        price_to_product = self.browser.find_element(*ProductPageLocators.PRICE_TO_PRODUCT)
        return price_to_product.text

    def should_be_push_as_product_name(self):
        push_name = self.browser.find_element(*ProductPageLocators.NAME_TO_PUSH).text
        name_to_product = self.browser.find_element(*ProductPageLocators.NAME_TO_PRODUCT).text
        assert push_name == name_to_product, "Name doesn't match!!!"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_not_be_success_message_is_disappeared(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"


