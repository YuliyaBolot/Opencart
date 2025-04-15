from selenium.webdriver.common.by import By
from diplom_opencart.helper import Product


class ProductPageLocators:

    PHONES_PRODUCT_LIST = (By.XPATH, '//div[@id="product-list"]')

    NEW_ADDED_PRODUCT = (By.XPATH, f'//a[text()="{Product.Name}"]')
