from home_page_po import ClickHelper
import time


def test_hover_company_buttons(browser, url):
    home_page_po = ClickHelper(browser)
    home_page_po.go_to_site(url)
    home_page_po.click_cookie_button()
    home_page_po.hover_company_button()
    #actions = ActionHelper(browser)
    assert home_page_po.aboutus_button_is_displayed(), "Is not visible"


def test_view_all_clients(browser, url):
    home_page_po = ClickHelper(browser)
    home_page_po.go_to_site(url)
    home_page_po.click_view_all_clients()
    assert home_page_po.get_current_url() == "https://inoxoft.com/clients/", "No success"