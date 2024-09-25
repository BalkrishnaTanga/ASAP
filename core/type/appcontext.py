import requests
from behave.runner import Context
from selene.api import browser
from selenium import webdriver


class AppContext(Context):

    def __init__(self, runner):
        super().__init__(runner)
        self.browser: webdriver.Chrome = None
        self.selene_browser: browser = None
        self.requestSession: requests.Session = None
        self.serverPath: str = None
        self.CSRFToken: str = None
