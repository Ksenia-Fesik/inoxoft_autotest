import pytest
from selenium import webdriver
import platform
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-setuid-sandbox')


def pytest_addoption(parser):
    parser.addoption("--driver", action="store", default="Chrome")
    parser.addoption("--url", action="store", default="https://inoxoft.com/blog/", help="url")
    parser.addoption("--username", action="store", default="manager", help="username")
    parser.addoption("--password", action="store", default="test", help="password")


def _select_firefox_driver(os):
    if os == 'Linux':
        return webdriver.Firefox(executable_path="./webdriver/firefox/geckodriver_linux64")
    elif os == 'Windows':
        return webdriver.Firefox(executable_path="./webdriver/firefox/geckodriver_win32")
    elif os == 'Darwin':
        return webdriver.Firefox(executable_path="./webdriver/firefox/geckodriver_mac")


def _select_chrome_driver(os):
    if os == 'Linux':
        return webdriver.Chrome(executable_path="./webdriver/chrome/chromedriver_linux64", chrome_options=options)
    elif os == 'Windows':
        return webdriver.Chrome(executable_path="./webdriver/chrome/chromedriver_win32")
    elif os == 'Darwin':
        return webdriver.Chrome(executable_path="./webdriver/chrome/chromedriver_mac")


def get_driver(browser_name, os):
    if browser_name == "Firefox":
        return _select_firefox_driver(os)
    else:
        return _select_chrome_driver(os)


@pytest.fixture(scope="session")
def browser(pytestconfig):
    os = platform.system()
    browser_name = pytestconfig.getoption("driver")
    driver = get_driver(browser_name, os)

    yield driver
    driver.quit()


