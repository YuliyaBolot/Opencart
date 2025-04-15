import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains


class BasePage:

    @allure.step("Инициализируем драйвер")
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.actions = ActionChains(driver)
        self.logger = driver.logger
        self.class_name = type(self).__name__

    @allure.step("Находим элемент")
    def find_element_located(self, locator):
        self.logger.info("%s: Check if element %s is present" % (self.class_name, str(locator)))
        return self.wait.until(expected_conditions.presence_of_element_located(locator))

    @allure.step("Ожидаем возможности нажатия на элемент")
    def find_element_located_click(self, locator):
        self.logger.info("%s: Click on element: %s" % (self.class_name, str(locator)))
        return self.wait.until(expected_conditions.element_to_be_clickable(locator)).click()

    @allure.step("Устанавливаем чек-бокс")
    def drag_and_drop(self, locator_take, locator_put):
        self.logger.info("%s: Set checkbox: %s, %s" % (self.class_name, str(locator_take), str(locator_put)))
        return self.actions.drag_and_drop(self.find_element_located(locator_take),
                                          self.find_element_located(locator_put)).perform()
