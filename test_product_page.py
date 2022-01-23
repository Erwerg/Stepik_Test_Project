from .pages.product_page import ProductPage
from .pages.login_page import LoginPage

import pytest

basic_product_url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"


@pytest.mark.skip
@pytest.mark.parametrize('offer_number',
                         [*range(7), pytest.param(7, marks=pytest.mark.xfail(reason='bugged link')), *range(8, 10)])
def test_guest_can_add_product_to_basket(browser, offer_number):
    link = f"{basic_product_url}?promo=offer{offer_number}"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_correct_addition_to_basket()


@pytest.mark.xfail(reason='negative check')
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = basic_product_url
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = basic_product_url
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_not_be_success_message()


@pytest.mark.xfail(reason='negative check')
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = basic_product_url
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.success_message_should_be_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = basic_product_url
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = basic_product_url
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
