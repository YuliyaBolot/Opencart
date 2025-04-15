from selenium.webdriver.common.by import By
from random import randint


class OrderPageLocators:

    ORDER_PAGE = (By.XPATH, '//div[@id="order"]')

    ADD_ORDER = (By.XPATH, '//div[@class="float-end"]/a')

    ADD_CUSTOMER_BUTTON = (By.XPATH, '//button[@data-bs-toggle="modal"]')

    ADD_PRODUCT_BUTTON = (By.XPATH, '//table[@class="table table-bordered"]/tfoot/tr/td/button')

    POPUP_ADD_PRODUCT = (By.XPATH, '//form[@id="form-product-add"]')

    PRODUCT_TAB = (By.XPATH, '//div[@class="modal-body"]/ul/li[1]/a')

    CHOOSE_PRODUCT_FIELD = (By.XPATH, '//input[@id="input-product"]')

    PRODUCT = (By.XPATH, '//ul[@id="autocomplete-product"]/li[2]/a')

    QUANTITY_FIELD = (By.XPATH, '//input[@id="input-quantity"]')

    COLOR_OPTIONS_FIELD = (By.XPATH, '//select[@id="input-option-226"]')

    COLOR = (By.XPATH, f'//select[@id="input-option-226"]/option[{randint(2, 3)}]')

    SAVE_PRODUCT_BUTTON = (By.XPATH, '//button[@id="button-product-add"]')

    VOUCHERS = (By.XPATH, '//div[@class="modal-body"]/ul/li[2]/a')

    RECIPIENT_NAME_FIELD = (By.XPATH, '//input[@id="input-to-name"]')

    RECIPIENT_EMAIL_FIELD = (By.XPATH, '//input[@id="input-to-email"]')

    SENDERS_NAME_FIELD = (By.XPATH, '//input[@id="input-from-name"]')

    SENDERS_EMAIL_FIELD = (By.XPATH, '//input[@id="input-from-email"]')

    CERTIFICATE_THEME_FIELD = (By.XPATH, '//select[@id="input-theme"]')

    THEME = (By.XPATH, f'//select[@id="input-theme"]/option[{randint(1, 3)}]')

    CERTIFICATE_AMOUNT = (By.XPATH, '//input[@id="input-amount"]')

    SAVE_VOUCHER_BUTTON = (By.XPATH, '//button[@id="button-voucher-add"]')

    CLOSE_POPUP_PRODUCT_BUTTON = (By.XPATH, '//div[@id="modal-cart"]/div/div/div[1]/button')

    PAYMENT_ADDRESS_BUTTON = (By.XPATH, '//button[@data-bs-target="#modal-payment-address"]')

    PAYMENT_ADDRESS_FORM = (By.XPATH, '//form[@id="form-payment-address"]')

    PAYMENT_FIRST_NAME = (By.XPATH, '//input[@id="input-payment-firstname"]')

    PAYMENT_LAST_NAME = (By.XPATH, '//input[@id="input-payment-lastname"]')

    PAYMENT_ADDRESS = (By.XPATH, '//input[@id="input-payment-address-1"]')

    PAYMENT_CITY = (By.XPATH, '//input[@id="input-payment-city"]')

    PAYMENT_POSTCODE = (By.XPATH, '//input[@id="input-payment-postcode"]')

    PAYMENT_COUNTRY_FIELD = (By.XPATH, '//select[@id="input-payment-country"]')

    PAYMENT_COUNTRY = (By.XPATH, '//select[@id="input-payment-country"]/option[187]')

    PAYMENT_REGION_FIELD = (By.XPATH, '//select[@id="input-payment-zone"]')

    PAYMENT_REGION = (By.XPATH, f'//select[@id="input-payment-zone"]/option[51]')

    SAVE_PAYMENT_DETAILS_BUTTON = (By.XPATH, '//button[@id="button-payment-address"]')

    CLOSE_POPUP_PAYMENT_ADDRESS_BUTTON = (By.XPATH, '//div[@id="modal-payment-address"]/div/div/div[1]/button')

    SHIPPING_ADDRESS_BUTTON = (By.XPATH, '//button[@data-bs-target="#modal-shipping-address"]')

    SHIPPING_ADDRESS_FORM = (By.XPATH, '//form[@id="form-shipping-address"]')

    SHIPPING_FIRST_NAME = (By.XPATH, '//input[@id="input-shipping-firstname"]')

    SHIPPING_LAST_NAME = (By.XPATH, '//input[@id="input-shipping-lastname"]')

    SHIPPING_ADDRESS = (By.XPATH, '//input[@id="input-shipping-address-1"]')

    SHIPPING_CITY = (By.XPATH, '//input[@id="input-shipping-city"]')

    SHIPPING_POSTCODE = (By.XPATH, '//input[@id="input-shipping-postcode"]')

    SHIPPING_COUNTRY_FIELD = (By.XPATH, '//select[@id="input-shipping-country"]')

    SHIPPING_COUNTRY = (By.XPATH, '//select[@id="input-shipping-country"]/option[187]')

    SHIPPING_REGION_FIELD = (By.XPATH, '//select[@id="input-shipping-zone"]')

    SHIPPING_REGION = (By.XPATH, f'//select[@id="input-shipping-zone"]/option[51]')

    SHIPPING_PAYMENT_DETAILS_BUTTON = (By.XPATH, '//button[@id="button-shipping-address"]')

    CLOSE_POPUP_SHIPPING_ADDRESS_BUTTON = (By.XPATH, '//div[@id="modal-shipping-address"]/div/div/div[1]/button')

    SHIPPING_METHOD_BUTTON = (By.XPATH, '//button[@id="button-shipping-methods"]')

    POPUP_SHIPPING_METHOD_FORM = (By.XPATH, '//form[@id="form-shipping-method"]')

    SHIPPING_RATE_CHECKBOX = (By.XPATH, '//input[@id="input-shipping-method-flat-flat"]')

    SHIPPING_METHOD_CONTINUE = (By.XPATH, '//button[@id="button-shipping-method"]')

    CLOSE_POPUP_SHIPPING_METHOD_BUTTON = (By.XPATH, '//div[@id="modal-shipping"]/div/div/div[1]/button')

    PAYMENT_METHOD_BUTTON = (By.XPATH, '//button[@id="button-payment-methods"]')

    POPUP_PAYMENT_METHOD_FORM = (By.XPATH, '//form[@id="form-payment-method"]')

    PAYMENT_METHOD_CHECKBOX = (By.XPATH, '//input[@id="input-payment-method-cod-cod"]')

    PAYMENT_METHOD_CONTINUE = (By.XPATH, '//button[@id="button-payment-method"]')

    CLOSE_POPUP_PAYMENT_METHOD_BUTTON = (By.XPATH, '//div[@id="modal-payment"]/div/div/div[1]/button')

    CONFIRM_ORDER_BUTTON = (By.XPATH, '//button[@id="button-confirm"]')

    ORDERS_LINK = (By.XPATH, '//ol[@class="breadcrumb"]/li[2]/a')

    ORDER_LIST = (By.XPATH, '//form[@id="form-order"]')

    CUSTOMER_NAME = (By.XPATH, '//table[@class="table table-bordered table-hover"]/tbody/tr[1]/td[4]')

    ORDER_STATUS = (By.XPATH, '//table[@class="table table-bordered table-hover"]/tbody/tr[1]/td[5]/label')

    ORDER_CHECKBOX = (By.XPATH, '//table[@class="table table-bordered table-hover"]/tbody/tr[1]/td[1]/input')

    DELETE_ORDER_BUTTON = (By.XPATH, '//div[@class="float-end"]/button[4]')

    ORDER_ID = (By.XPATH, '//table[@class="table table-bordered table-hover"]/tbody/tr[1]/td[2]')
