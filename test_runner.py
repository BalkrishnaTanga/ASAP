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

from features.testing.environment import copy_history

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
    print(f"rmdir {cwd}\\allure-results\\history")
    os.system("allure generate allure-results --clean -o allure-report")


def copy_contents(source_dir, dest_dir):
    """
    Copy all contents from source_dir to dest_dir.
    """
    try:
        for item in os.listdir(source_dir):
            src_path = os.path.join(source_dir, item)
            dest_path = os.path.join(dest_dir, item)

            if os.path.isfile(src_path):
                shutil.copy2(src_path, dest_path)
            elif os.path.isdir(src_path):
                shutil.copytree(src_path, dest_path)

        print(f"All contents copied from '{source_dir}' to '{dest_dir}'.")
    except Exception as e:
        print(f"Error copying contents: {e}")


def clear_directory(directory):
    """
    Clear all contents from a given directory.
    """
    try:
        for filename in os.listdir(directory):
            filepath = os.path.join(directory, filename)
            if os.path.isfile(filepath):
                os.remove(filepath)
            elif os.path.isdir(filepath):
                shutil.rmtree(filepath)
        print(f"Directory '{directory}' cleared successfully.")
    except Exception as e:
        print(f"Error clearing directory: {e}")

def run_all_feature_files(tag_value):
    files = glob.glob(os.path.join(cwd, "**/*.feature"), recursive=True)
    files.sort()
    print("Run Aall")
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
    print("Usage : TestRunner.py <tags>")
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