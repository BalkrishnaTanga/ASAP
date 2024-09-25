from behave import *

from common.setup import initialize, scenario_screenshot_on_failure
from pages.login_page import LoginPage


@given("Open application and enter {username} with {password}")
def step_impl(context, username, password):
    """
    :type context: behave.runner.Context
    """
    context.loginPage = LoginPage(context, context.serverPath)
    context.loginPage.open()
    context.loginPage.return_uname_box_element().send_keys(username)
    context.loginPage.return_login_password_box_element().send_keys(password)



@when("user clicks on login button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.loginPage.return_login_button().click()


@then("Verify the user is successfully login")
def step_impl(context):
    actual_string = context.loginPage.return_login_employee().get_text()
    assert "Employee" == actual_string




@then("Fail the test case")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert False

@given("user opens the browser and fails the test case")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """

@then ("Verify the use is not able to login")
def step_impl(context):
    assert context.loginPage.return_login_validation_msg().get_text() == "Invalid User name and/or Password"
    """
    :type context: behave.runner.Context
    """



@given("fail the test case")
def step_impl(context):
    assert False

