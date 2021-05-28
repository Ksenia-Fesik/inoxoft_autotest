from base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class Locators:
    COMPANY_BUTTON = (By.LINK_TEXT, "Company")
    ABOUT_US_BUTTON = (By.LINK_TEXT, "About Us")
    VIEW_ALL_CLIENTS = (By.LINK_TEXT, "View All")
    COOKIE_BUTTON = (By.ID, "cn-accept-cookie")



class ClickHelper(BasePage):

    def hover_company_button(self):
        element = self.find_element(Locators.COMPANY_BUTTON, time=2)
        return ActionChains(self.driver).move_to_element(element).perform()

    def aboutus_button_is_displayed(self):
        return self.find_element(Locators.ABOUT_US_BUTTON, time=2).is_displayed()

    def click_cookie_button(self):
        return self.find_element(Locators.COOKIE_BUTTON, time=2).click()

    def click_view_all_clients(self):
        return self.find_element(Locators.VIEW_ALL_CLIENTS, time=2).click()



#class ActionHelper(BasePage):

    #def get_notification_success_converted(self):
        #wait = WebDriverWait(self.driver, timeout=5)
        #alert = wait.until(expected_conditions.presence_of_element_located(Locators.NOTIFICATION_SUCCESS_CONVERTED_MESSAGE))
        #return alert




