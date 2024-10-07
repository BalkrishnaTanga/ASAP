import glob
import os
import shutil

from common.setup import initialize, scenario_screenshot_on_failure, clean_up, delete_folder_contents, run_shell_command
source_directory = os.path.join(os.getcwd(),"\\allure-results")
destination_directory = os.path.join(os.getcwd(),"\\allure-results\\history")
file_extensions = ('.png','.json')
cwd = os.getcwd()

def before_all(context):
    copy_history(context, f"{cwd}\\allure-results" , f"{cwd}\\allure-results\\history",file_extensions)
    allure_result_path = os.path.join((os.path.abspath(os.curdir)), 'failure_screenshot')
    delete_folder_contents(allure_result_path)
    allure_report_path = os.path.join((os.path.abspath(os.curdir)), 'allure-results')
    #delete_folder_contents(allure_report_path)
    print("Before all tests")
    initialize(context)


def after_scenario(context, scenario):
    print("After scenario")
    scenario_screenshot_on_failure(context, scenario)


def after_all(context):
    print("After all tests")
    clean_up(context)
    files_to_delete = [
        #f"{cwd}\\allure-results\\history\\categories-trend.json",
        f"{cwd}\\allure-results\\history\\duration-trend.json",
        f"{cwd}\\allure-results\\history\\history.json",
        f"{cwd}\\allure-results\\history\\history-trend.json",
        f"{cwd}\\allure-results\\history\\retry-trend.json"
    ]
    for file_path in files_to_delete:
        os.remove((file_path))
    files_to_copy = [
             f"{cwd}\\allure-report\\history\\categories-trend.json",
             f"{cwd}\\allure-report\\history\\duration-trend.json",
             f"{cwd}\\allure-report\\history\\history.json",
             f"{cwd}\\allure-report\\history\\history-trend.json",
             f"{cwd}\\allure-report\\history\\retry-trend.json"
    ]

    for copy_file in files_to_copy:
        if os.path.exists(copy_file):
            shutil.copy2(copy_file,f"{cwd}\\allure-results\\history")
            print(copy_file+" :copied")


def copy_history(context,src_dir, dest_dir, extensions=['*.json','*.png']):
    os.makedirs(dest_dir, exist_ok=True)
    files = []
    result_json_files = glob.glob(os.path.join(src_dir, "*-result.json"), recursive=False)
    attachment_png_files = glob.glob(os.path.join(src_dir, "*-attachment.png"), recursive=False)
    files = result_json_files + attachment_png_files
    for file_name in files:
        if file_name.endswith(extensions):
            full_file_name = os.path.join(src_dir, file_name)
            if os.path.isfile(full_file_name):
                shutil.copy(full_file_name, dest_dir)
                os.remove(full_file_name)
                print(f"copied {full_file_name} to {dest_dir}")

def copy_specific_files(source_dir, dest_dir):
    result_json_files = glob.glob(os.path.join(source_dir, "*.result.json", recursive=f))