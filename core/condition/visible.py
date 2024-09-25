from core.element import Element, is_selene_element
from selene.support.conditions import be
from selene.wait import wait_for

class Visible:

    def __init__(self, value):
        self.timeout = value

    def wait_till(self, guides_el: Element):
        el = guides_el.get_element()
        if is_selene_element(el):
            wait_for(el, be.visible, self.timeout, 1)
        # else:
        # TODO

    def wait_till_not(self, guides_el: Element):
        el = guides_el.get_element()
        if is_selene_element(el):
            wait_for(el, be.not_(be.visible), self.timeout, 1)
        # else:
        # TODO