import time

from core.condition.visible import Visible
from core.constants import Constants
from core.element import Element
from core.page import Page


class LoginPage(Page):
    def __init__(self, context, uri):
        path = "/Account/Login"
        self.Login_user = Element(context, "//input[@id='LoginId']",
                                  Constants.XPATH)
        self.Login_password = Element(context, "//input[@id='Password']",
                                  Constants.XPATH)
        self.Login_validationmsg = Element(context, "//li[normalize-space()='Invalid User name and/or Password']",
                                      Constants.XPATH)
        self.Login_Employee= Element(context,"//a[normalize-space()='Employee']",Constants.XPATH)

        self.Login_button = Element(context, "//input[@value='Log in']", Constants.XPATH)
        super().__init__(context, path,
                         Element(context, "//input[@id='LoginId']", Constants.XPATH))
       # self.Login_validatioin = Element(context,""),Constants.XPATH)


    def return_uname_box_element(self):
        self.Login_user.should_wait_till(Visible(5))
        return self.Login_user

    def return_login_password_box_element(self):
        self.Login_password.should_wait_till(Visible(5))
        return self.Login_password

    def return_login_button(self):
        self.Login_button.should_wait_till(Visible(8))
        #time.sleep(5)
        return self.Login_button


    def return_login_validation_msg(self):
        self.Login_validationmsg.should_wait_till(Visible(5))
        return self.Login_validationmsg


    def return_login_employee(self):
        self.Login_Employee.should_wait_till(Visible(10))
        return self.Login_Employee