
import polling

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


WAIT_TIME = 10
Width = 1000
Height = 650
contour_threshold = 200


def explicit_wait(driver, selector, selector_type, wait_time=WAIT_TIME):
    WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((selector_type, selector)))


def clickable_wait(driver, selector, selector_type):
    WebDriverWait(driver, WAIT_TIME).until(EC.element_to_be_clickable((selector_type, selector)))


def poll_for_condition(condition):
    """
    This will poll for condition.check() method which should return a truthy value, will poll in steps of 1 second
    :param condition: condition object
    :param timeout: Timeout in seconds
    :return: None
    :raises: TimeoutException
    """
    polling.poll(lambda: condition.check(), step=condition.stepTime, timeout=condition.timeout)


def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text


def switch_to_default_content(self):
    self.context.browser.switch_to.default_content()


def assert_multiple_string(actual_or_assertions, expected_values): #This function asserts multiple string values
    """Asserts that actual values match expected values.

    :param actual_or_assertions: The list of actual values to evaluate.
    :param expected_values: The list of expected values to match against.
    Returns True if all actual values match expected values, False otherwise.
    """
    if len(actual_or_assertions) != len(expected_values):
        raise ValueError("Number of actuals and expected values must be equal")

    if actual_or_assertions == expected_values:
        return True
    else:
        return False