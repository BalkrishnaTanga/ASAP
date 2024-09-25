import time
from lib2to3.fixes.fix_input import context
from lib2to3.pytree import convert


from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from common.left_pannel import LeftPanel
from core.condition.visible import Visible
from core.constants import Constants
from core.element import Element
from core.elements import Elements
from core.page import Page
from pages.employee_imformation import EmployeeInformation


class EmployeePage(Page):
    def __init__(self,context):
        path = "/Person"

        self.Dashboard_Employee_SearchEmployee_SearchField = Element(context, "//input[@name='txt']",
                                       Constants.XPATH)
        self.Dashboard_Employee_SearchEmployee_NewEmployee_HeaderTxt = Element(context, "//h4[normalize-space()='Employee Information']",
                                                           Constants.XPATH)
        self.Dashboard_Employee_SearchEmployee_SearchBt = Element(context, "(//i[@class='fa fa-plus'])[1]",
                                                                  Constants.XPATH)
        self.employee_plus_btn = Element(context, "(//i[@class='fa fa-plus'])[1]/..",
                                                                  Constants.XPATH)
        self.SUBMIT_BTN = Element(context,"//input[@type='submit']", Constants.XPATH)
        self.popup_title = Element(context,"//h4[normalize-space()='Employee Information']", Constants.XPATH)
        self.select_search_by_option = Element(context,"//select[@ng-model='filter.searchBy']", Constants.XPATH)

        self.lastname= Element(context,"//input[@id='txtlastname']",Constants.XPATH)
        self.last_4_digits_ssn= Element(context,"//input[@id='txtlast4ssn']",Constants.XPATH)
        self.lastnameAND_firstname = Element(context,"//input[@id='txtSearch']", Constants.XPATH)

        self.employee_company_name= Element(context,"//input[@placeholder='search company']",Constants.XPATH)
        super().__init__(context, path, Element(context, "//a[normalize-space()='Employee']", Constants.XPATH))
        #//*[@id="page-wrapper"]/div/div[3]/div/div/div[2]/div[1]/form/div[1]/div[1]/select
        #(//div[@class='portlet-body']//select)[1]


    def return_dashboard_employee_company_name(self):
        self.employee_company_name.should_wait_till(Visible(5))
        return  self.employee_company_name


    def click_search_employee(self):
        left_panel = LeftPanel(self.context)
        left_panel.return_dashboard_employee_toggle_element().click()
        left_panel.return_dashboard_employee_search_btn_element().click()

    def return_dashboard_employee_search_employee_search_field(self):
        self.Dashboard_Employee_SearchEmployee_SearchField.should_wait_till(Visible(5))
        return self.Dashboard_Employee_SearchEmployee_SearchField


    def return_dashboard_employee_search_by_lastname(self):
        self.lastnameAND_firstname .should_wait_till(Visible(5))
        return  self.lastnameAND_firstname


    def return_dashboard_employee_search_employee_new_employee_header_txt(self):
        self.Dashboard_Employee_SearchEmployee_NewEmployee_HeaderTxt.should_wait_till(Visible(5))
        return self.Dashboard_Employee_SearchEmployee_NewEmployee_HeaderTxt

    def return_submit_btn_element(self):
        self.SUBMIT_BTN.should_wait_till(Visible(5))
        return self.SUBMIT_BTN

    def click_employee_button(self):
        self.Dashboard_Employee_SearchEmployee_SearchBt.should_wait_till(Visible(5))
        time.sleep(4)
        self.Dashboard_Employee_SearchEmployee_SearchBt.click()

    def is_employee_information_popup_visible(self) ->bool:
        self.popup_title.should_wait_till(Visible(5))
        return self.popup_title.is_visible()

    def is_add_employee_btn_enabled(self, enable):
        if enable == "true":
            return self.employee_plus_btn.get_attribute("disabled")
        elif enable == "false":
            return self.employee_plus_btn.is_clickable()

    def     select_search_by_dropdown_option(self,option: str):
        self.SUBMIT_BTN.should_wait_till(Visible(5))
        self.select_search_by_option.click()
        option_xpath = f'//select[@ng-model="filter.searchBy"]//option[text()="{option}"]'
        Element(self.context,option_xpath,Constants.XPATH).should_wait_till(Visible(5))
        Element(self.context,option_xpath,Constants.XPATH).click()



     # def select_search_by_dropdown_options1(self):
     #     self.select_search_by_option.should_wait_till(Visible(3))
     #     return  self.select_search_by_option


    def return_dashboard_last4digitssn(self):
        self.lastname.should_wait_till(Visible(5))
        return self.last_4_digits_ssn

    def return_dashboard_lastname_element(self):
        self.lastname.should_wait_till(Visible(5))
        return self.lastname

    def return_firstname_lastname(self):
        self.lastnameAND_firstname.should_wait_till(Visible(5))
        return self.lastnameAND_firstname

    def is_add_employee_button_enable(self) -> bool:
        try:
            self.SUBMIT_BTN.should_wait_till(Visible(5))
            return True
        except:
            return False