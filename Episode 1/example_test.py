from selenium import webdriver
from selenium.webdriver.common.by import By


def test_run_example_firefox():
    browser = webdriver.Firefox()
    browser.get("http://127.0.0.1:8000/polls")
    login = browser.find_element(By.ID, "id_username")
    login.send_keys("bs-demo")
    browser.quit()


def test_run_example_chrome():
    browser = webdriver.chrome()
    browser.get("http://127.0.0.1:8000/polls")
    login = browser.find_element(By.ID, "id_username")
    login.send_keys("bs-demo")
    browser.quit()
