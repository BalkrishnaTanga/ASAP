import os

from common.setup import initialize, scenario_screenshot_on_failure, clean_up, delete_folder_contents, run_shell_command


def before_all(context):
    allure_result_path = os.path.join((os.path.abspath(os.curdir)), 'failure_screenshot')
    delete_folder_contents(allure_result_path)
    allure_report_path = os.path.join((os.path.abspath(os.curdir)), 'result', 'allure-report')
    delete_folder_contents(allure_report_path)
    allure_result_path = os.path.join((os.path.abspath(os.curdir)), 'result', 'allure_result')
    delete_folder_contents(allure_result_path)
    print("Before all tests")
    initialize(context)


def after_scenario(context, scenario):
    print("After scenario")
    scenario_screenshot_on_failure(context, scenario)


def after_all(context):
    print("After all tests")
    clean_up(context)
    command = os.path.join('allure generate ',(os.path.abspath(os.curdir)), 'result/allure_result --clean -o ',(os.path.abspath(os.curdir)), 'result/allure-report')
    print()
    run_shell_command("allure generate C:\\Python-Selenium\\Python_SeleniumBDD\\Python_Selenium\\result\\allure_result --clean -o C:\\Python-Selenium\\Python_SeleniumBDD\\Python_Selenium\\allure-report")
