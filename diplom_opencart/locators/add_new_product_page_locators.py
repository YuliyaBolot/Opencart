from selenium.webdriver.common.by import By


class AddNewProductPageLocators:

    ADD_PRODUCT_BUTTON = (By.XPATH, '//div[@class="float-end"]/a')

    ADD_PRODUCT_PAGE = (By.XPATH, '//div[@class="tab-content"]')

    PRODUCT_NAME_FIELD = (By.XPATH, '//input[@id="input-name-1"]')

    IFRAME = (By.XPATH, '//iframe[@class="cke_wysiwyg_frame cke_reset"]')

    DESCRIPTION_FIELD = (By.CSS_SELECTOR, '.cke_show_borders')

    META_TAG_TITLE_FIELD = (By.XPATH, '//input[@id="input-meta-title-1"]')

    META_TAG_DESCRIPTION_FIELD = (By.XPATH, '//textarea[@id="input-meta-description-1"]')

    DATA = (By.XPATH, '//ul[@class="nav nav-tabs"]/li[2]/a')

    MODEL_FIELD = (By.XPATH, '//input[@id="input-model"]')

    PRICE_FIELD = (By.XPATH, '//input[@id="input-price"]')

    QUANTITY_FIELD = (By.XPATH, '//input[@id="input-quantity"]')

    WEIGHT_FIELD = (By.XPATH, '//input[@id="input-weight"]')

    LINKS = (By.XPATH, '//ul[@class="nav nav-tabs"]/li[3]/a')

    MANUFACTURER_FIELD = (By.XPATH, '//input[@id="input-manufacturer"]')

    MANUFACTURER_LINK = (By.XPATH, '//ul[@id="autocomplete-manufacturer"]/li[2]/a')

    CATEGORIES_FIELD = (By.XPATH, '//input[@id="input-category"]')

    CATEGORY_LINK = (By.XPATH, '//ul[@id="autocomplete-category"]/li/a')

    REWARD_POINTS = (By.XPATH, '//ul[@class="nav nav-tabs"]/li[10]/a')

    POINTS_FIELD = (By.XPATH, '//input[@id="input-points"]')

    SEO = (By.XPATH, '//ul[@class="nav nav-tabs"]/li[11]/a')

    KEYWORD_FIELD = (By.XPATH, '//input[@id="input-keyword-0-1"]')

    SAVE_BUTTON = (By.XPATH, '//div[@class="float-end"]/button')

    PRODUCT_LINK = (By.XPATH, '//ol[@class="breadcrumb"]/li[2]/a')

    CHECKBOX_NEW_PRODUCT = (By.XPATH, '//form[@id="form-product"]//tbody/tr[2]/td[1]/input')

    DELETE_BUTTON = (By.XPATH, '//div[@class="float-end"]/button[3]')
