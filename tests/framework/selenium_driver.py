from typing import Any, Union
from selenium import webdriver
from tests.data.config import settings
from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import tests.utils.custom_logger as cl
import logging
import os

class WebApp:
    instance = None
    log = cl.customLogger(logging.DEBUG)

    @classmethod
    def get_instance ( cls ):
        if cls.instance is None:
            cls.instance = WebApp()
        return cls.instance

    def __init__ ( self ):

        if settings['browser'] == "firefox":
            self.driver = webdriver.Firefox()
        elif settings['browser'] == "chrome":
            self.driver = webdriver.Chrome()
        else:
            self.driver = webdriver.Firefox()

    def get_driver ( self ):
        return self.driver

    def goto_page ( self ):
        self.driver.get(settings['url'])
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

    def screenShot ( self, resultMessage ):
        """
        Takes screenshot of the current open web page
        """
        fileName = resultMessage + "_FAIL.png"
        screenshotDirectory = "../screenshots/"
        relativeFileName = screenshotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info("Screenshot saved to: " + destinationFile)
        except:
            self.log.error("An unexpected exception occurred while taking the screenshot.")
            print_stack()

    def getByType ( self, locatorType ):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type " + locatorType + " not correct/supported")
        return False

    def getElement ( self, locator, locatorType="id" ):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element found with the locator: " + locator + " and  locatorType: " + locatorType)
        except:
            self.log.info("Element not found with locator: " + locator + " and  locatorType: " + locatorType)
        return element

    def elementClick ( self, locator, locatorType="id" ):
        try:
            element = self.getElement(locator, locatorType)
            element.click()
            self.log.info("Clicked on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.info("Cannot click on the element with locator: " + locator + " locatorType: " + locatorType)
            print_stack()

    def sendKeys ( self, data, locator, locatorType="id" ):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info("An input typed into: " + locator + " locatorType: " + locatorType)
        except:
            self.log.info("An exception occured while typing an input into: " + locator +
                          " locatorType: " + locatorType)
            print_stack()

    def isElementPresent ( self, locator, locatorType="id" ):
        try:
            element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("Element Found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            self.log.info("Element not found")
            return False

    def elementPresenceCheck ( self, locator, byType ):
        try:
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                self.log.info("Element Found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            self.log.info("Element not found")
            return False

    def verifyTextContains ( self, actualText: object, expectedText: object ) -> object:

        self.log.info("Actual Text From Application Web UI --> :: " + actualText)
        self.log.info("Expected Text From Application Web UI --> :: " + expectedText)
        if expectedText.lower() in actualText.lower():
            self.log.info("Verification successful! The caption on the element contains the expected value.")
            return True
        else:
            self.log.info("Verification failed. ")
            return False

    def waitForElement ( self, locator, locatorType="id",
                         timeout=10, pollFrequency=0.5 ):
        element = None
        try:
            byType = self.getByType(locatorType)
            self.log.info("Waiting for maximum " + str(timeout) +
                          " seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout, poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType, locator)))
            self.log.info("Element appeared on the web page")
        except:
            self.log.info("Element not appeared on the web page")
            print_stack()
        return element

    def getText ( self, locator="", locatorType="id", element=None, info="" ):

        try:
            if locator:  # This means if locator is not empty
                self.log.debug("In locator condition")
                element = self.getElement(locator, locatorType)
            self.log.debug("Before finding text")
            text = element.text
            self.log.debug("After finding element, size is: " + str(len(text)))
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                self.log.info("Getting text on the element :" + info)
                self.log.info("The caption is:" + text + "'")
                text = text.strip()
        except:
            self.log.error("Failed to get text on element " + info)
            print_stack()
            text = None
        return text

    def webScroll ( self, direction="up" ):

        if direction == "up":
            # Scroll Up
            self.driver.execute_script("window.scrollBy(0, -1000);")

        if direction == "down":
            # Scroll Down
            self.driver.execute_script("window.scrollBy(0, 1000);")

    def close_app( self ):
        self.driver.quit()


webapp: Union[WebApp, Any] = WebApp.get_instance()
