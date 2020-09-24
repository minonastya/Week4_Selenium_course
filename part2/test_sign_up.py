from selenium import webdriver
from part2 import locators as _locators
import pytest

@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

def test_sign_up(browser):
        #Arrange
        browser.get(_locators.login_page)
        login_input = browser.find_element_by_css_selector(_locators.new_email_input)
        password_input = browser.find_element_by_css_selector(_locators.new_password_input)
        repeat_password_input = browser.find_element_by_css_selector(_locators.repeat_new_password_input)
        registration_submit_button = browser.find_element_by_css_selector(_locators.button_sign_up)

        #Act
        login_input.send_keys(_locators.new_email)
        password_input.send_keys(_locators.safety_password)
        repeat_password_input.send_keys(_locators.safety_password)
        registration_submit_button.click()

        #Assert
        assert browser.current_url == _locators.main_page, \
            "Registration finished with an error"
