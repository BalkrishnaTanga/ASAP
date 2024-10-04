import os
import shutil

from common.setup import initialize, scenario_screenshot_on_failure, clean_up, delete_folder_contents, run_shell_command
source_directory = os.path.join(os.getcwd(),"\\allure-results")
destination_directory = os.path.join(os.getcwd(),"\\allure-results\\history")
file_extensions = ('.png','.json')
cwd = os.getcwd()

def before_all(context):
    #shutil.copy("allure-report/history", "result/allure_result/history")
    allure_result_path = os.path.join((os.path.abspath(os.curdir)), 'failure_screenshot')
    delete_folder_contents(allure_result_path)
    allure_report_path = os.path.join((os.path.abspath(os.curdir)), 'allure-results')
    delete_folder_contents(allure_report_path)


    #allure_result_path = os.path.join((os.path.abspath(os.curdir)), 'result', 'allure_result')
    #copy_history(context, source_directory, destination_directory, ".png")
    #delete_folder_contents(allure_result_path)
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
    run_shell_command(f"allure generate {cwd}\\allure-results --clean -o {cwd}\\allure-report")

def copy_history(context,src_dir, dest_dir, extensions):
    os.makedirs(dest_dir, exist_ok=True)
    for file_name in os.listdir(src_dir):
        if file_name.endswith(extensions):
            full_file_name = os.path.join(src_dir, file_name)
            if os.path.isfile(full_file_name):
                shutil.copy(full_file_name, dest_dir)
                print(f"copied {full_file_name} to {dest_dir}")
