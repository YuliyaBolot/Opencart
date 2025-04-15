from selenium.webdriver.common.by import By


class AdminPageLocators:

    NAVIGATION = (By.XPATH, '//nav[@id="column-left"]')

    CATALOG = (By.XPATH, '//li[@id="menu-catalog"]/a')

    PRODUCTS = (By.XPATH, '//li[@id="menu-catalog"]/ul/li[2]/a')

    CUSTOMERS_TAB = (By.XPATH, '//li[@id="menu-customer"]/a')

    CUSTOMERS = (By.XPATH, '//li[@id="menu-customer"]/ul/li[1]/a')

    SALES = (By.XPATH, '//li[@id="menu-sale"]/a')

    ORDERS = (By.XPATH, '//li[@id="menu-sale"]/ul/li[1]/a')

    SYSTEM = (By.XPATH, '//li[@id="menu-system"]/a')

    USERS = (By.XPATH, '//li[@id="menu-system"]/ul/li[2]/a')

    API = (By.XPATH, '//ul[@id="collapse-7-1"]/li[3]/a')
