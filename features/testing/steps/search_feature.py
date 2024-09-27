import time
from lib2to3.fixes.fix_input import context

from behave import *
from selenium.webdriver import ActionChains

from common.utils import contour_threshold
from pages.employee_search import EmployeePage
from pages.login_page import LoginPage

@given(": Navigate to Home page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.loginPage = LoginPage(context, context.serverPath)
    context.loginPage.open()
    context.loginPage.return_uname_box_element().send_keys(context.user)
    context.loginPage.return_login_password_box_element().send_keys(context.password)
    context.loginPage.return_login_button().click()


@when("Enter the new employee numbers {ssn}")
def step_impl(context,ssn):
    context.employee_searchOBJ = EmployeePage(context)
    context.employee_searchOBJ.click_search_employee()
    context.employee_searchOBJ.return_dashboard_employee_search_employee_search_field().send_keys(ssn)
    context.employee_searchOBJ.return_submit_btn_element().click()
    context.employee_searchOBJ.click_employee_button()


@Then("employee information popup should open")
def stem_impl(context):
    assert context.employee_searchOBJ.is_employee_information_popup_visible()

@when("enter already existing employee {ssn}")
def step_impl(context, ssn):
    context.employee_searchOBJ = EmployeePage(context)
    context.employee_searchOBJ.click_search_employee()
    context.employee_searchOBJ.return_dashboard_employee_search_employee_search_field().send_keys(ssn)
    context.employee_searchOBJ.return_submit_btn_element().click()


@Then("verify the employee button is {disabled}")
def step_impl(context, disabled):
    time.sleep(4)
    if disabled == "true":
        assert context.employee_searchOBJ.is_add_employee_btn_enabled(disabled) == "true"
    elif disabled == "false":
        assert context.employee_searchOBJ.is_add_employee_btn_enabled(disabled) == True



@given("last {option} digit option is selected from dropdown")
def step_impl(context, option:str):
    context.employee_searchOBJ = EmployeePage(context)
    context.employee_searchOBJ.click_search_employee()
    context.employee_searchOBJ = EmployeePage(context)
    context.employee_searchOBJ.select_search_by_dropdown_option(option)

@When ("Enter the {company_name}")
def step_impl(context, company_name):
    context.employee_searchOBJ = EmployeePage(context)
    context.employee_searchOBJ.return_dashboard_employee_company_name().send_keys(company_name)
    ActionChains(context.browser).__enter__().perform()




@Step  ("Enter last 4 digit ssn {last4digits} and last name {lastname}")
def step_impl(context,last4digits:str,lastname:str):
    context.employee_searchOBJ.return_dashboard_last4digitssn().send_keys(last4digits)
    context.employee_searchOBJ.return_dashboard_lastname_element().send_keys(lastname)


@Step("Enter the names {lastname_firstname}")
def step_impl(context, lastname_firstname):
    context.employee_searchOBJ = EmployeePage(context)
    context.employee_searchOBJ.return_firstname_lastname().send_keys(lastname_firstname)
    context.employee_searchOBJ.return_submit_btn_element().click()

@When("user click on add employee button")
def step_impl(context):
    context.employee_searchOBJ.return_submit_btn_element().click()
    context.employee_searchOBJ.click_employee_button()


@step("Enter existing last 4 digit ssn {last4digits} and last name {lastname}")
def step_impl(context, last4digits, lastname):
    context.employee_searchOBJ.return_dashboard_last4digitssn().send_keys(last4digits)
    context.employee_searchOBJ.return_dashboard_lastname_element().send_keys(lastname)
    context.employee_searchOBJ.click_employee_button()


@step("Enter the email  {email}")
def step_impl(context, email):
    context.employee_searchOBJ = EmployeePage(context)
    context.employee_searchOBJ.return_firstname_lastname().send_keys(email)
    context.employee_searchOBJ.return_submit_btn_element().click()

@step("Enter the lastname {lastName}")
def stem_impl(context, lastName):
    context.employee_searchOBJ = EmployeePage(context)
    context.employee_searchOBJ.return_dashboard_employee_search_by_lastname().send_keys(lastName)
    context.employee_searchOBJ.return_submit_btn_element().click()

@step("Enter the firstname  {firstname}")
def step_impl(context, firstname):
    context.employee_searchOBJ = EmployeePage(context)
    context.employee_searchOBJ.return_firstname_lastname().send_keys(firstname)
    context.employee_searchOBJ.return_submit_btn_element().click()


@step("Enter the passportno  {passportno}")
def step_impl(context, passportno):
    context.employee_searchOBJ = EmployeePage(context)
    context.employee_searchOBJ.return_firstname_lastname().send_keys(passportno)
    context.employee_searchOBJ.return_submit_btn_element().click()


@step("Enter the driverlicense  {driverlicense}")
def step_impl(context, driverlicense):
    context.employee_searchOBJ = EmployeePage(context)
    context.employee_searchOBJ.return_firstname_lastname().send_keys(driverlicense)
    context.employee_searchOBJ.return_submit_btn_element().click()


@step("Enter the personId   {personId}")
def step_impl(context, personId):
    context.employee_searchOBJ = EmployeePage(context)
    context.employee_searchOBJ.return_firstname_lastname().send_keys(personId)
    context.employee_searchOBJ.return_submit_btn_element().click()



@step("User the employee_ref_id on search employee page {employee_ref_id}")
def step_impl(context, employee_ref_id):
    context.employee_searchOBJ = EmployeePage(context)
    context.employee_searchOBJ.return_firstname_lastname().send_keys(employee_ref_id)
    context.employee_searchOBJ.return_submit_btn_element().click()


@step("Enter the application_id {application_id}")
def step_impl(context, application_id):
    context.employee_searchOBJ = EmployeePage(context)
    context.employee_searchOBJ.return_firstname_lastname().send_keys(application_id)
    context.employee_searchOBJ.return_submit_btn_element().click()


@step("User the application id on search epage {application_id}")
def step_impl(context, application_id):
    context.employee_searchOBJ = EmployeePage(context)
    context.employee_searchOBJ.return_firstname_lastname().send_keys(application_id)
    context.employee_searchOBJ.return_submit_btn_element().click()

