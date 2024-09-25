from lib2to3.fixes.fix_input import context

from behave import *

from pages.employee_search import EmployeePage





@when("search for employee {ssn}")
def step_impl(context, ssn):
    """
    :type context: behave.runner.Context
    :type ssn: str
    """
    raise NotImplementedError(u'STEP: When search for employee <ssn>')