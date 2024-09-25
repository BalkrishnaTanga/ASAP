import logging

from core.element import Element


class Widget:

    def __init__(self, context, selector=None, selector_type=None):
        self.context = context
        self.selector = selector
        self.selector_type = selector_type
        self.log = logging.getLogger(self.__class__.__name__)
        if selector is not  None and selector_type is not None:
            self.WIDGET_IDENTIFIER = Element(self.context, selector, selector_type)

    def is_widget_open(self):
        if self.WIDGET_IDENTIFIER is not None:
            return self.WIDGET_IDENTIFIER.is_loaded()
        else:
            raise AttributeError("Selector attribute not defined")

    def is_visible(self):
        if self.WIDGET_IDENTIFIER is not None:
            return self.WIDGET_IDENTIFIER.is_visible()
        else:
            raise AttributeError("Selector attribute not defined")