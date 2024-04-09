from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 8).until(expected_conditions.visibility_of_element_located(locator))

        return self.driver.find_element(*locator)

    def click_on_element(self, locator):
        element = self.find_element_with_wait(locator)

        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.click()
        action.perform()

    def send_keys(self, locator, key):
        element = self.find_element_with_wait(locator)
        element.send_keys(key)

    def current_url(self):
        return self.driver.current_url

    def get_text_from_element(self, locator):
        element = self.find_element_with_wait(locator)
        return element.text
