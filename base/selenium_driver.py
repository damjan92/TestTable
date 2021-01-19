from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import utilities.custom_logger as cl
from selenium.webdriver import ActionChains
import time
import os
import logging

class SeleniumDriver():

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == 'id':
            return By.ID
        elif locatorType == "xpath":
            return  By.XPATH
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "tag":
            return By.TAG_NAME
        else:
            self.log.warning("Locator type: " + locatorType + " is not supported")
        return False

    def getElement(self, locator, locatorType = 'id'):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            #self.log.info("Element is found")
        except:
            self.log.info("#GET#Element is not found")
        return element


    def getElements(self, locator, locatorType = "id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_elements(byType, locator)
        except:
            self.log.info("Element is not found")
        return element



    def elementClick(self, locator, locatorType = 'id'):
        try:
            element = self.getElement(locator, locatorType)
            element.click()
        except:
            self.log.info("#CLICK# Element is not found")
            print_stack()

    def sendKeys(self, data, locator, locatorType):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(data)
        except:
            self.log.info("Can not send: " + data + " data")
            print_stack()

    def isElementPresent(self, locator, locatorType):
        try:
            element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("Element is presented")
                return True
            else:
                self.log.warning("#IsElementPresent# Element is not present")
                return False
        except:
            self.log.warning("## Element is not present")
            print_stack()



    def waitForElement(self, locator, locatorType="id",
                       timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            print("Waiting for maximum :: " + str(timeout) +
                          " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType, locator)))
            self.log.info("Element appeared on the web page")
        except:
            self.log.info("Element not appeared on the web page")
            print_stack()
        return element

    def screenshot(self, resultMessage):

        fileName = resultMessage + "." + str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "..\\screenshots"
        relativeFileName = screenshotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile =   os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshots(destinationFile)
            self.log.info("Scrennshot is save to " + destinationFile)
        except:
            self.log.error("### Exception occuried")
            print_stack()


