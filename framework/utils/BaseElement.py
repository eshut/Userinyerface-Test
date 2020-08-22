from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from framework.logger.logger import Logger
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

logger = Logger(logger="BaseElement").getlog()

from framework.Browser import *
from abc import ABC

WaitTime = jsonGetter.GetJson.getFile(CONFIG,"WaitTime")


class BaseElement(ABC):

    def __init__(self, locatorType, locator):
        self.locatorType = locatorType
        self.locator = locator
        self.driver = RunBrowser().driver

    def _find(self, WaitTime = WaitTime):
        '''
        :param WaitTime: time in seconds while the driver will try to find an element
        :return: element
        '''
        wait = WebDriverWait(self.driver, WaitTime)

        try:
            wait.until(EC.presence_of_element_located((self.locatorType, self.locator)))
        except TimeoutException:
            logger.warn("Cannot find such an element!" + self.locator)
        self.element = self.driver.find_element(self.locatorType, self.locator)
        return self.element


    def _finds(self, WaitTime = WaitTime):
        '''
        :param WaitTime: time in seconds while the driver will try to find an element
        :return: Many elements
        '''
        wait = WebDriverWait(self.driver, WaitTime)
        try:
            wait.until(EC.presence_of_element_located((self.locatorType, self.locator)))
        except TimeoutException:
            logger.warn("Cannot find such an element!" + self.locator)
        self.elements = self.driver.find_elements(self.locatorType, self.locator)

        return self.elements

    def click(self):
        '''
        :return: nothing
        Find and click to element
        '''
        self._find()
        self.element.click()

    def move(self):
        '''
        Moves mouse to an element
        '''
        self.__find()
        hov = ActionChains(self.driver).move_to_element((self.element)).perform()