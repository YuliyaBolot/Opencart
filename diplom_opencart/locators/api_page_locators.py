from selenium.webdriver.common.by import By


class ApiPageLocators:

    ADD_API_BUTTON = (By.XPATH, '//div[@class="float-end"]/a')

    API_USERNAME_FIELD = (By.XPATH, '//input[@id="input-username"]')

    API_KEY_FIELD = (By.XPATH, '//textarea[@id="input-key"]')

    GENERATE_BUTTON = (By.XPATH, '//button[@id="button-generate"]')

    API_ADDRESS_TAB = (By.XPATH, '//form[@id="form-api"]/ul/li[2]/a')

    GENERAL_TAB = (By.XPATH, '//form[@id="form-api"]/ul/li[1]/a')

    STATUS_CHECKBOX = (By.XPATH, '//input[@id="input-status"]')

    ADD_IP_BUTTON = (By.XPATH, '//button[@id="button-ip"]')

    IP_FIELD = (By.XPATH, '//input[@name="api_ip[]"]')

    SAVE_API_BUTTON = (By.XPATH, '//button[@form="form-api"]')

    API_CHECKBOX = (By.XPATH, '//table[@class="table table-bordered table-hover"]/tbody/tr/td[1]/input')

    DELETE_API_BUTTON = (By.XPATH, '//div[@class="float-end"]/button')
