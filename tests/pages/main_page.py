from tests.framework.selenium_driver import webapp
import tests.utils.custom_logger as cl
import logging

class mainPage():
    instance = None
    log = cl.customLogger(logging.DEBUG)

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = mainPage()
        return cls.instance

    def __init__(self):
        self.driver = webapp.get_driver()

    #locators
    input_field_id="search_form_input_homepage"
    search_button_id="search_button_homepage"
    result_id="r1-0"

    def search_phrase (self, phrase):
        webapp.waitForElement(self.input_field_id)
        webapp.sendKeys(phrase, self.input_field_id)


    def click_search_button (self):
        webapp.waitForElement(self.search_button_id)
        webapp.elementClick(self.search_button_id)

    def verify_search_result (self, phrase):
        webapp.waitForElement(self.result_id)
        result_text=webapp.getText(self.result_id)
        text_contains: bool=webapp.verifyTextContains(result_text, phrase)
        return text_contains

mp = mainPage.get_instance()
