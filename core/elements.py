from typing import List, Union, Tuple

import selene.elements
from selenium.webdriver.remote.webelement import WebElement
from selene.elements import SeleneElement
from common.utils import explicit_wait
from core.constants import Constants
from core.element import Element
from core.type.appcontext import AppContext


def are_selene_elements(elements):
    if(len(elements)>=1):
        return isinstance(elements[0], selene.elements.SeleneElement)
    return True


class Elements:
    def __init__(self, context:AppContext, selector: str, selector_type: str):
        self.context: AppContext = context
        self.selector = selector
        self.selector_type = selector_type

    def are_loaded(self, wait=True):
        return Element(self.context, self.selector, Constants.XPATH).is_loaded(wait)

    def _get_elements(self, skip_selene=False)-> List[Union[SeleneElement, WebElement]]:
        if not skip_selene and self.selector_type != Constants.ID:
            selene_by_or_selector: Union[Tuple, str] = (self.selector_type, self.selector) if self.selector_type is Constants.XPATH else self.selector
            return self.context.selene_browser.elements(selene_by_or_selector)
        explicit_wait(self.context.browser, self.selector_type)
        return self._get_web_elements()

    def _get_web_elements(self) -> List[WebElement]:
        if self.selector_type == Constants.XPATH:
            return self.context.browser.find_element_by_xpath(self.selector)
        elif self.selector_type == Constants.CSS_SELECTOR:
            return self.context.browser.find_element_by_css_selector(self.selector)
        elif self.selector_type == Constants.ID:
            return self.context.browser.find_element_by_id(self.selector)
        elif self.selector_type == Constants.CLASS_NAME:
            return self.context.browser.find_element_by_class_name(self.selector)
        elif self.selector_type == Constants.NAME:
            return self.context.browser.find_element_by_tag_name(self.selector)

    def size(self):
        elements = self._get_elements()
        return len(elements)

    def get_attr(self, atr: str) -> List[str]:
        elements = self._get_elements()
        result = []
        if are_selene_elements(elements):
            for i in elements:
                result.append(i.get_attribute(str))

        return result

    def get_element(self, index: int):
        if self.selector_type is not Constants.XPATH:
            raise Exception("Only XPATH is supported")
        return Element(self.context, f"({self.selector})[{index}]", Constants.XPATH)