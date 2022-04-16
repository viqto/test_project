from .pages.product_page import ProductPage
import pytest


@pytest.mark.skip
@pytest.mark.parametrize('piece_link', ["offer0", "offer1", "offer2", "offer3", "offer4", "offer5", "offer6",
                                        pytest.param("offer7", marks=pytest.mark.xfail), "offer8", "offer9"])
def test_guest_can_add_product_to_basket(browser, piece_link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={piece_link}"
    page = ProductPage(browser, link)
    page.open()  # открываем страницу
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_product_name()
    page.should_be_product_price()
    page.should_be_push_as_product_name()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()  # открываем страницу
    page.add_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()  # открываем страницу
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()  # открываем страницу
    page.add_to_basket()
    page.should_not_be_success_message_is_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
