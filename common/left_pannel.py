from core.condition.visible import Visible
from core.constants import Constants
from core.element import Element


class LeftPanel():
    def __init__(self, context):
     self.Dashboard_EmployeeToggle = Element(context, "//a[normalize-space()='Employee']",
                              Constants.XPATH)
     self.Dashboard_Employee_SearchEmployee= Element(context, "//a[normalize-space()='Search Employee']",
                              Constants.XPATH)



    def return_dashboard_employee_toggle_element(self):
        self.Dashboard_EmployeeToggle.should_wait_till(Visible(5))
        return self.Dashboard_EmployeeToggle

    def return_dashboard_employee_search_btn_element(self):
        self.Dashboard_Employee_SearchEmployee.should_wait_till(Visible(5))
        return self.Dashboard_Employee_SearchEmployee