import logging

from core.element import Element


class Page:
    def __init__(self, context, uri, page_identifier: Element = None):
        # type: (AppContext, str) -> None
        self.context = context
        self.uri = self.context.serverPath + uri
        self.PAGE_IDENTIFIER = page_identifier
        self.log = logging.getLogger(self.__class__.__name__)

    def open(self, refresh=False):
        self.context.browser.get(self.uri)
        loaded = self.PAGE_IDENTIFIER.is_loaded(True)
        if not loaded:
            if refresh:
                self.refresh()
            else:
                raise Exception(f"Unable to open the page with type {type(self).__name__} and uri : {self.uri}!")
        return self

    def refresh(self):
        self.context.browser.refresh()
        if not self.PAGE_IDENTIFIER.is_loaded(True):
            raise Exception(f"Unable to refresh the page with type {type(self).__name__} and uri: {self.uri}!")
        return self

    def get_current_url(self):
        return self.context.browser.current_url