from selenium.webdriver.common.by import By


class RegisterPageLocators:

    REGISTER_PAGE = (By.XPATH, '//div[@id="account-register"]')

    FIRST_NAME_FIELD = (By.XPATH, '//input[@name="firstname"]')

    LAST_NAME_FIELD = (By.XPATH, '//input[@name="lastname"]')

    EMAIL_FIELD = (By.XPATH, '//input[@name="email"]')

    PASSWORD_FIELD = (By.XPATH, '//input[@name="password"]')

    SUBSCRIBE = (By.XPATH, '//input[@id="input-newsletter"]')

    PRIVACY_POLICY_CHECKBOX = (By.XPATH, '//input[@name="agree"]')

    CONTINUE_BUTTON = (By.XPATH, '//button[@class="btn btn-primary"]')

    CONGRATULATION_WITH_REGISTRATION = (By.XPATH, '//h1[text()="Your Account Has Been Created!"]')

    NEXT_CONTINUE_BUTTON = (By.XPATH, '//div[@id="content"]/div/a')

    PERSONAL_ACCOUNT = (By.XPATH, '//div[@id="account-account"]')
