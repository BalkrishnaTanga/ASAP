import json
import os
import re
import subprocess
import sys
from behave.model_core import Status
from xml.dom import minidom
import requests
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService, Service
from selene.api import browser
from selenium import webdriver
import allure


cwd = os.path.abspath(os.getcwd())
class Unbuffered(object):
    def __init__(self, stream):
        self.stream = stream

    def write(self, data):
        self.stream.write(data)
        self.stream.flush()

    def writelines(self, datas):
        self.stream.writelines(datas)
        self.stream.flush()

    def __getattr__(self, attr):
        return getattr(self.stream, attr)


def clean_filename(filename):
    return re.sub(r"[/\\?%*:|\"<>\x7F\x00-\x1F]", "-", filename)

def setup_selene(context, driver):
    browser.set_driver(driver)
    context.selene_browser = browser


def clean_up(context):
    context.browser.close()
    context.browser.quit()


def delete_folder_contents(folder_path):
    try:
        for root, dirs, files in os.walk(folder_path, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))

        print(f"All contents deleted from {folder_path}")

    except FileNotFoundError:
        print(f"The folder {folder_path} was not found.")
    except PermissionError:
        print(f"You don't have permission to delete contents from {folder_path}")
    except OSError as e:
        print(f"An error occurred while deleting contents from {folder_path}: {str(e)}")


def run_shell_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        if result.returncode == 0:
            print("Command executed successfully:")
            print(result.stdout.strip())
        else:
            print("Command failed with return code:", result.returncode)
            print("Error output:")
            print(result.stderr.strip())

    except Exception as e:
        print(f"An error occurred while running the command: {str(e)}")


def initialize(context):
    environment_xml = os.path.join(
        os.path.abspath(os.curdir), 'environment.xml')
    if not os.path.exists(environment_xml):
        print("[Error]: Environment xml not fount at " + os.path.abspath(os.curdir))
        exit()
    parse_environment_file(context, environment_xml)
    options = Options()
    options.headless = False
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_experimental_option("prefs", {
        "download.prompt_for_download": False
    })
    #if context.context.browser_information == "Chrome":
    service = Service('D:\\Project\\Selenium\\Browsers\\chromedriver.exe')  # Specify the full path to the correct chromedriver
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    context.browser = driver
    driver.set_page_load_timeout(30)
    setup_selene(context, driver)
    context.browser.get(context.serverPath)
    context.browser.maximize_window()
 #   default_login(context)
    setup_session(context)
    sys.stdout = Unbuffered(sys.stdout)
    sys.stderr = Unbuffered(sys.stderr)


def parse_environment_file(context, environment_xml):
    xmldoc = minidom.parse(environment_xml)
    key_node = xmldoc.getElementsByTagName('key')
    iterator = 0
    for each_key_node in key_node:
        if each_key_node.firstChild.nodeValue == "server_url":
            value_node = xmldoc.getElementsByTagName('value')
            context.serverPath = value_node[iterator].firstChild.nodeValue
            print("server url :" + context.serverPath)
        elif each_key_node.firstChild.nodeValue == "username":
            value_node = xmldoc.getElementsByTagName('value')
            context.user = value_node[iterator].firstChild.nodeValue
        elif each_key_node.firstChild.nodeValue == "password":
            value_node = xmldoc.getElementsByTagName('value')
            context.password = value_node[iterator].firstChild.nodeValue
        elif each_key_node.firstChild.nodeValue == "Regression":
            value_node = xmldoc.getElementsByTagName('value')
            context.regression = value_node[iterator].firstChild.nodeValue
        elif each_key_node.firstChild.nodeValue == "browser":
            value_node = xmldoc.getElementsByTagName('value')
            context.browser_information = value_node[iterator].firstChild.nodeValue
        iterator = iterator + 1

    if not context.serverPath.endswith('/'):
        context.serverPath = context.serverPath + "/"

def result_folder_path(context):
    result_path = cwd + "/result/allure_result"
    context.result_path = result_path



def scenario_screenshot_on_failure(context, current_scenario):
    if current_scenario.status == Status.failed:
        screenshot_path = os.path.join((os.path.abspath(os.curdir)), 'failure_screenshot', clean_filename(str(current_scenario.name)))
        context.browser.get_screenshot_as_file(screenshot_path + ".png")
        allure.attach.file(screenshot_path + ".png", name="failure_screenshot", attachment_type=allure.attachment_type.PNG)


def setup_session(context):
    context.requestSession = requests.Session()