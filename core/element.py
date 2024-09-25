
import logging
import time
from typing import Union, Tuple

import selene.elements
from selene.elements import SeleneElement
from selene.support.conditions import be
from selene.wait import wait_for
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from common.utils import clickable_wait
from common.utils import explicit_wait
from core.constants import Constants
from core.type.appcontext import AppContext



def is_selene_element(element):
    return isinstance(element, selene.elements.SeleneElement)


class Element:
    def __init__(self, context, selector, selector_type):
        # type: (AppContext, str, str) -> None
        self.context = context
        self.selector = selector
        self.selector_type = selector_type

    def is_loaded(self, wait=True):
        try:
            if wait:
                explicit_wait(self.context.browser, self.selector, self.selector_type)
            else:
                self._get_web_element()
            return True
        except:
            return False

    def is_clickable(self):
        try:
            clickable_wait(self.context.browser, self.selector, self.selector_type)
            return True
        except:
            return False

    def should_have(self, condition):
        condition.match(self)

    def should_not_have(self,condition):
        condition.not_match(self)

    def should_wait_till(self, condition):
        condition.wait_till(self)

    def should_wait_till_not(self, condition):
        condition.wait_till_not(self)

    def clear(self):
        self.get_element().clear()

    def click(self, retry=True, override=False):
        try:
            element = self.get_element()
            clickable_wait(self.context.browser, self.selector, self.selector_type)
            element.click()
        except Exception as e:
            logging.exception(f"{self.selector}  ----------   Exception occurred while click : " + str(e))
            if retry:
                logging.info(f"{self.selector}  ----------   Retrying......")
                time.sleep(0.1)
                self.click(retry=False, override=override)
            elif override:
                logging.info(f"{self.selector}  ----------   Trying move and click......")
                wait_for(self.get_element(), be.visible, 4, 1)
                self.move_and_click_to_element(retry=False)
            else:
                raise e

    def double_click(self, retry=True):
        try:
            element = self.get_element()
            clickable_wait(self.context.browser, self.selector, self.selector_type)
            if is_selene_element(element):
                element.double_click()
        except Exception as e:
            logging.exception(f"{self.selector}  ----------   Exception occurred while double click")
            if retry:
                logging.info(f"{self.selector}  ----------   Retrying......")
                time.sleep(0.1)
                self.double_click(retry=False)
            else:
                raise e

    def is_selected(self):
        return self.get_element().is_selected()

    def is_visible(self):
        try:
            return self.get_element().is_displayed()
        except:
            return False

    def get_attribute(self, attr, retry=True):
        try:
            el = self.get_element()
            return el.get_attribute(attr)
        except Exception as e:
            logging.exception(f"{self.selector}  ----------   Exception occurred while getting attr : {attr}")
            if retry:
                logging.info(f"{self.selector}  ----------   Retrying......")
                time.sleep(0.1)
                return self.get_attribute(attr, retry=False)
            else:
                raise e

    def send_keys(self, input_text, retry=True):
        try:
            element = self.get_element()
            clickable_wait(self.context.browser, self.selector, self.selector_type)
            element.send_keys(input_text)
        except Exception as e:
            logging.exception(f"{self.selector}  ----------   Exception occurred while sending keys({input_text})")
            if retry:
                logging.info(f"{self.selector}  ----------   Retrying......")
                time.sleep(0.1)
                self.send_keys(input_text, retry=False)
            else:
                raise e

    def _get_web_element(self) -> WebElement:
        if self.selector_type == Constants.XPATH:
            return self.context.browser.find_element_by_xpath(self.selector)
        elif self.selector_type == Constants.CSS_SELECTOR:
            return self.context.browser.find_element_by_css_selector(self.selector)
        elif self.selector_type == Constants.ID:
            return self.context.browser.find_element_by_id(self.selector)
        elif self.selector_type == Constants.CLASS_NAME:
            return self.context.browser.find_element_by_class_name(self.selector)
        elif self.selector_type == Constants.NAME:
            return self.context.browser.find_element(By.NAME, self.selector)

    def get_element(self, skip_selene=False) -> Union[WebElement, SeleneElement]:
        if not skip_selene and self.selector_type != Constants.ID:
            selene_by_or_selector: Union[Tuple, str] = (
                self.selector_type, self.selector) if self.selector_type is Constants.XPATH else self.selector
            return self.context.selene_browser.element(selene_by_or_selector)

        explicit_wait(self.context.browser, self.selector, self.selector_type)
        return self._get_web_element()

    def move_to_element(self):
        element: WebElement = self.get_element(True)
        action = ActionChains(self.context.browser)
        action.move_to_element(element).perform()

    def switch_to_iframe(self):
        explicit_wait(self.context.browser, self.selector, self.selector_type)
        element = self._get_web_element()
        self.context.browser.switch_to.frame(element)

    def get_text(self, retry=True):
        try:
            return self.get_element().text
        except Exception as e:
            logging.exception(f"{self.selector}  ----------   Exception occurred while getting text")
            if retry:
                logging.info(f"{self.selector}  ----------   Retrying......")
                time.sleep(0.1)
                return self.get_text(retry=False)
            else:
                raise e

    def move_and_click_to_element(self, retry=True):
        try:
            element: WebElement = self.get_element(True)
            action = ActionChains(self.context.browser)
            action.move_to_element(element).click().perform()
        except Exception as e:
            logging.exception(f"{self.selector}  ----------   Exception occurred while moving and clicking on element")
            if retry:
                logging.info(f"{self.selector}  ----------   Retrying......")
                time.sleep(0.1)
                wait_for(self.get_element(), be.visible, 4, 1)
                self.move_and_click_to_element(retry=False)
            else:
                raise e

    def context_click(self, retry=True):
        try:
            element = self.get_element()
            clickable_wait(self.context.browser, self.selector, self.selector_type)
            element.context_click()
        except Exception as e:
            logging.exception(f"{self.selector}  ----------   Exception occurred while context clicking on element with msg")
            if retry:
                logging.info(f"{self.selector}  ----------   Retrying......")
                time.sleep(0.1)
                self.context_click(retry=False)
            else:
                raise e

    def is_enabled(self):
        return self.get_element().is_enabled()