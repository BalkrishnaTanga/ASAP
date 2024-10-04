import glob
import logging
import os
import shutil
import subprocess
import sys
import threading

from six import print_

from common.setup import parse_environment_file, result_folder_path

from multiprocessing import context


cwd = os.path.abspath(os.getcwd())
run_whitelist_check = False
environment_xml = os.path.join(os.path.abspath(os.curdir), 'environment.xml')
exclude_feature_files = os.path.join(os.path.abspath(os.curdir), 'exclude_feature_files.txt')

parse_environment_file(context, environment_xml)


def run_each_feature_file(a_files,tag_value):
    for file in a_files:
        logging.info(f"Executing feature file {file}")
        result_command = "behave " + file + " " +tag_value + " --no-capture-stderr --no-logcapture --no-capture --no-skipped -f allure_behave.formatter:AllureFormatter -o " + context.result_path
        logging.info(result_command)
        os.environ["TMPDIR"] = "/tmp"
        os.system(result_command)

def run_history():
    os.makedirs("allure-results\\history", exist_ok=True)
    for filename in os.listdir("allure-report\\history"):
        shutil.copy(os.path.join("allure-report\\history", filename), "allure-results\\history")
    os.system("allure generate allure-results --clean -o allure-report")


def run_all_feature_files(tag_value):
    files = glob.glob(os.path.join(cwd, "**/*.feature"), recursive=True)
    files.sort()
    print("Rrun Aall")
    print(files)
    with open(exclude_feature_files) as file:
        exclude_files = file.readlines()
        exclude_files = [file.rstrip() for file in exclude_files]
        for exclude_file in exclude_files:
            for file in files:
                if (file.rsplit("\\",1)[-1] == exclude_file):
                    logging.info(f"skipping the file: {file}")
                    files.remove(file)
                    break
        file_set_one = files[:len(files) // 2]
        file_set_two = files[len(files) // 2:]

        thread_one = threading.Thread(target=run_each_feature_file, args=(file_set_one,tag_value,))
        thread_two = threading.Thread(target=run_each_feature_file, args=(file_set_two,tag_value,))

        thread_one.start()
        thread_two.start()

        thread_one.join()
        thread_two.join()

if len(sys.argv)<1:
    print("Uusage : TtstRunner.py <tags>")
    sys.exit(1)

print("sys.argv:; ", sys.argv)
tags = sys.argv[1]
print(tags)
tag_value = f'--tags="{tags}"'
result_folder_path(context)
print(context.result_path)
path = "failure_screenshot"
isExist = os.path.exists(path)
if not isExist:
    os.makedirs(path)
run_all_feature_files(tag_value)
run_history()