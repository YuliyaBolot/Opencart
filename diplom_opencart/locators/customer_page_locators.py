from selenium.webdriver.common.by import By


class CustomerPageLocators:

    CUSTOMER_NAME = (By.XPATH, '//form[@id="form-customer"]/div[1]/table/tbody/tr/td[2]')

    CHECKBOX_CUSTOMER = (By.XPATH, '//form[@id="form-customer"]/div[1]/table/tbody/tr/td[1]/input')

    DELETE_CUSTOMER = (By.XPATH, '//div[@class="float-end"]/button[2]')

    POPUP_CUSTOMER_FORM = (By.XPATH, '//div[@class="modal-content"]')

    CUSTOMER_FIRST_NAME_FIELD = (By.XPATH, '//input[@id="input-firstname"]')

    CUSTOMER_LAST_NAME_FIELD = (By.XPATH, '//input[@id="input-lastname"]')

    CUSTOMER_EMAIL = (By.XPATH, '//input[@id="input-email"]')

    CUSTOMER_PHONE = (By.XPATH, '//input[@id="input-telephone"]')

    SAVE_CUSTOMER = (By.XPATH, '//button[@id="button-customer"]')

    CLOSE_CUSTOMER_FORM = (By.XPATH, '//div[@class="modal-header"]/button')
