import os

from selenium import webdriver
import pytest


drivers = (
    'Chrome',
    'Edge',
    'Firefox',
    'IE',
    'ios',
    'Safari',
    'WebKitGTK',
    'Galaxy S20'
)


def pytest_addoption(parser):
    parser.addoption('--driver',
                     action='store',
                     choices=drivers,
                     dest='drivers',
                     metavar='DRIVER',
                     help='driver to run tests against ()')
    parser.addoption("--os",
                     action="store",
                     dest="os",
                     help="OS to test against")
    parser.addoption("--os-version",
                     action='store',
                     dest="os_version",
                     help="Version of OS")
    parser.addoption('--browser-args', action='store', dest='args',
                     help='arguments to start the browser with')


@pytest.fixture(scope='function')
def login(driver):

    class Login():

        def __init__(self):
            from selenium.webdriver.common.by import By
            from selenium.common.exceptions import NoSuchElementException
            driver.get("http://bs-local.com:8000/polls")
            try:
                driver.find_element(By.ID, "id_username").send_keys("bs-demo")
                driver.find_element(By.ID, "id_password").send_keys("hunter1234")
                driver.find_element(By.ID, "login").click()
            except NoSuchElementException:
                # If we can't find these elements then we've probably have
                # got through without needing to login
                pass

    return Login()


@pytest.fixture(scope='function')
def remote_login(remote):

    class Login():

        def __init__(self):
            from selenium.webdriver.common.by import By
            from selenium.common.exceptions import NoSuchElementException
            remote.get("http://bs-local.com:8000/polls")
            try:
                remote.find_element(By.ID, "id_username").send_keys("bs-demo")
                remote.find_element(
                    By.ID, "id_password").send_keys("hunter1234")
                remote.find_element(By.ID, "login").click()
            except NoSuchElementException:
                # If we can't find these elements then we've probably have
                # got through without needing to login
                pass

    return Login()



@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Firefox()
    driver.get("http://bs-local.com:8000/polls/")
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def remote(request):
    browser = request.config.getoption('drivers')
    _os = request.config.getoption("os")
    os_version = request.config.getoption('os_version')
    desired_cap = {
        "build": "parallel",
        "project": "Summer of Learning",
        "browser": browser,
        "browserstack.local": "true",
        "name": "Parallel with {} on {}".format(browser, os_version),
    }
    if browser == "Galaxy S20":
        del desired_cap['browser']
        desired_cap["device"] = "Samsung Galaxy S20"
        desired_cap["real_mobile"] = "true"
        desired_cap["os_version"] = "10.0"

    if browser == "ios":
        del desired_cap['browser']
        desired_cap["device"] = "iPhone XS"
        desired_cap["real_mobile"] = "true"

    if os_version:
        desired_cap["os"] = "Windows"
        desired_cap["os_version"] = os_version

    if _os:
        desired_cap["os"] = _os
        desired_cap["os_version"] = os_version

    bs_username = os.environ['BSUSERNAME']
    bs_password = os.environ['BSPASSWORD']
    if bs_username is None or bs_password is None:
        raise Exception("Username and Password env vars need setting")
    bs_endpoint = "https://{}:{}@hub-cloud.browserstack.com/wd/hub"\
        .format(bs_username, bs_password)
    driver = webdriver.Remote(
        command_executor=bs_endpoint, desired_capabilities=desired_cap)
    driver.get("http://bs-local.com:8000/polls/")
    yield driver
    driver.quit()
