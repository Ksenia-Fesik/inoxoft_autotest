from base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class Locators:
    AGILE_METHODOLOGY_TAG = (By.CLASS_NAME, "tag-id-368")


class ClickHelper(BasePage):

    def click_agile_methodology_tag(self):
        return self.find_element(Locators.AGILE_METHODOLOGY_TAG, time=2).click()


#class ActionHelper(BasePage):

    #def get_notification_success_converted(self):
        #wait = WebDriverWait(self.driver, timeout=5)
        #alert = wait.until(expected_conditions.presence_of_element_located(Locators.NOTIFICATION_SUCCESS_CONVERTED_MESSAGE))
        #return alert




