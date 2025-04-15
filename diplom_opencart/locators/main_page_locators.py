from selenium.webdriver.common.by import By


class MainPageLocators:

    MAIN_PAGE = (By.XPATH, '//div[@id="common-home"]')

    PHONES_AND_PDAs_LOGO = (By.XPATH, '//div[@id="narbar-menu"]/ul/li[6]/a')

    MY_ACCOUNT = (By.XPATH, '//ul[@class="list-inline"]/li[2]/div/a/span')

    REGISTER = (By.XPATH, '//ul[@class="dropdown-menu dropdown-menu-right show"]/li[1]/a')
