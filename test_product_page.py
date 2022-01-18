from .pages.product_page import ProductPage
import pytest

@pytest.mark.parametrize('offer_number', [*range(7), pytest.param(7, marks=pytest.mark.xfail(reason='bugged link')), *range(8,10)])
def test_guest_can_add_product_to_basket(browser, offer_number):
    link = f"http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer{offer_number}"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_correct_addition_to_basket()
