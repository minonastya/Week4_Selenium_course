import time
from part1 import locators as _locators

def test_item_button(browser):
        #Data
        browser.get(_locators.main_page_link)
        time.sleep(5)

        #Act
        search_input = browser.find_element_by_css_selector(_locators.input_search)
        search_input.send_keys(_locators.search_text)
        button_search = browser.find_element_by_css_selector(_locators.button_search)
        button_search.click()

        product_in_search = browser.find_element_by_css_selector(_locators.name_of_product)
        product_in_search.click()
        button_add_to_basket = browser.find_element_by_css_selector(_locators.btn_add_to_basket)

        #Assert
        assert button_add_to_basket != None, "Test failed. Button not find."
        time.sleep(5)
