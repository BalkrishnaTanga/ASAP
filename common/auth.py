
from core.constants import Constants
from core.element import Element


def default_login(context):
    open_application(context)


def open_application(context):
    context.browser.get(context.serverPath)
