from blog_page_po import ClickHelper
import time


def test_blog_buttons(browser, url):
    blog_page = ClickHelper(browser)
    blog_page.go_to_path(url, "/blog/")
    blog_page.click_cookie_button()
    blog_page.click_agile_methodology_tag()
    #actions = ActionHelper(browser)
    assert blog_page.get_current_url() == "https://inoxoft.com/blog/?tag=agile-methodology", "No success"


