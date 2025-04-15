from selenium.webdriver.common.by import By


class AdminLoginPageLocators:

    LOGIN_ADMIN_PAGE = (By.XPATH, '//div[@class="container-fluid"]')

    USERNAME_FIELD = (By.XPATH, '//input[@name="username"]')

    PASSWORD_FIELD = (By.XPATH, '//input[@name="password"]')

    LOGIN_BUTTON = (By.XPATH, '//button[@class="btn btn-primary"]')
