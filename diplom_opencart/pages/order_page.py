import allure
from diplom_opencart.pages.base_page import BasePage
from diplom_opencart.locators.order_page_locators import OrderPageLocators
from diplom_opencart.helper import Customer, Product, Recipient, Sender


class OrderPage(BasePage):

    @allure.step("Загрузка страницы заказов")
    def loading_order_page(self):
        self.logger.info("Orders page is loaded")
        return self.find_element_located(OrderPageLocators.ORDER_PAGE)

    @allure.step("Нажимаем на кнопку добавления нового заказа")
    def click_on_add_order(self):
        return self.find_element_located_click(OrderPageLocators.ADD_ORDER)

    @allure.step("Нажимаем на кнопку добавления покупателя")
    def click_on_add_customer(self):
        return self.find_element_located_click(OrderPageLocators.ADD_CUSTOMER_BUTTON)

    @allure.step("Приступаем к заведению заказа")
    def start_add_new_order(self):
        self.loading_order_page()
        self.click_on_add_order()
        self.click_on_add_customer()
        self.logger.info("Order's page is loaded")

    @allure.step("Нажимаем на кнопку добавления товара")
    def click_on_add_product_button(self):
        return self.find_element_located_click(OrderPageLocators.ADD_PRODUCT_BUTTON)

    @allure.step("Появление всплывающего окна для добавления товара")
    def appearance_popup_add_product(self):
        return self.find_element_located(OrderPageLocators.POPUP_ADD_PRODUCT)

    @allure.step("Нажимаем на поле выбора товара")
    def click_on_choose_product_field(self):
        return self.find_element_located_click(OrderPageLocators.CHOOSE_PRODUCT_FIELD)

    @allure.step("Выбираем необходимый товар")
    def choose_product(self):
        return self.find_element_located_click(OrderPageLocators.PRODUCT)

    @allure.step("Указываем количество товара")
    def set_product_quantity(self, quantity):
        self.find_element_located_click(OrderPageLocators.QUANTITY_FIELD)
        self.find_element_located(OrderPageLocators.QUANTITY_FIELD).clear()
        return self.find_element_located(OrderPageLocators.QUANTITY_FIELD).send_keys(quantity)

    @allure.step("Нажимаем на поле выбора цвета")
    def click_on_choose_color_field(self):
        return self.find_element_located_click(OrderPageLocators.COLOR_OPTIONS_FIELD)

    @allure.step("Указываем цвет")
    def choose_color(self):
        return self.find_element_located_click(OrderPageLocators.COLOR)

    @allure.step("Сохраняем товар")
    def click_on_save_product_button(self):
        return self.find_element_located_click(OrderPageLocators.SAVE_PRODUCT_BUTTON)

    @allure.step("Добавляем товар")
    def add_product(self):
        self.back_to_product_tab()
        self.click_on_choose_product_field()
        self.choose_product()
        self.set_product_quantity(Product.Quantity)
        self.click_on_choose_color_field()
        self.choose_color()
        self.click_on_save_product_button()
        self.close_product_form()
        self.logger.info("Product is added")

    @allure.step("Переходим на вкладку 'Ваучеры'")
    def go_to_vouchers_tab(self):
        return self.find_element_located_click(OrderPageLocators.VOUCHERS)

    @allure.step("Указываем имя получателя")
    def set_recipient_name(self, recipient_name):
        self.find_element_located_click(OrderPageLocators.RECIPIENT_NAME_FIELD)
        self.find_element_located(OrderPageLocators.RECIPIENT_NAME_FIELD).clear()
        return self.find_element_located(OrderPageLocators.RECIPIENT_NAME_FIELD).send_keys(recipient_name)

    @allure.step("Указываем email получателя")
    def set_recipient_email(self, recipient_email):
        self.find_element_located_click(OrderPageLocators.RECIPIENT_EMAIL_FIELD)
        self.find_element_located(OrderPageLocators.RECIPIENT_EMAIL_FIELD).clear()
        return self.find_element_located(OrderPageLocators.RECIPIENT_EMAIL_FIELD).send_keys(recipient_email)

    @allure.step("Указываем имя отправителя")
    def set_sender_name(self, sender_name):
        self.find_element_located_click(OrderPageLocators.SENDERS_NAME_FIELD)
        self.find_element_located(OrderPageLocators.SENDERS_NAME_FIELD).clear()
        return self.find_element_located(OrderPageLocators.SENDERS_NAME_FIELD).send_keys(sender_name)

    @allure.step("Указываем email отправителя")
    def set_sender_email(self, sender_email):
        self.find_element_located_click(OrderPageLocators.SENDERS_EMAIL_FIELD)
        self.find_element_located(OrderPageLocators.SENDERS_EMAIL_FIELD).clear()
        return self.find_element_located(OrderPageLocators.SENDERS_EMAIL_FIELD).send_keys(sender_email)

    @allure.step("Нажимаем на поле выбора темы ваучера")
    def click_on_certificate_theme_field(self):
        return self.find_element_located_click(OrderPageLocators.CERTIFICATE_THEME_FIELD)

    @allure.step("Выбираем тему ваучера")
    def choose_certificate_theme(self):
        return self.find_element_located_click(OrderPageLocators.THEME)

    @allure.step("Указываем сумму сертификата")
    def put_certificate_amount(self, certificate_amount):
        self.find_element_located_click(OrderPageLocators.CERTIFICATE_AMOUNT)
        self.find_element_located(OrderPageLocators.CERTIFICATE_AMOUNT).clear()
        return self.find_element_located(OrderPageLocators.CERTIFICATE_AMOUNT).send_keys(certificate_amount)

    @allure.step("Сохраняем ваучер")
    def save_voucher(self):
        return self.find_element_located_click(OrderPageLocators.SAVE_VOUCHER_BUTTON)

    @allure.step("Возвращаемся на вкладку товаров")
    def back_to_product_tab(self):
        return self.find_element_located_click(OrderPageLocators.PRODUCT_TAB)

    @allure.step("Закрываем форму заведения товара")
    def close_product_form(self):
        return self.find_element_located_click(OrderPageLocators.CLOSE_POPUP_PRODUCT_BUTTON)

    @allure.step("Добавляем ваучер")
    def add_voucher(self):
        self.click_on_add_product_button()
        self.appearance_popup_add_product()
        self.go_to_vouchers_tab()
        self.set_recipient_name(Recipient.Recipient_name)
        self.set_recipient_email(Recipient.Recipient_email)
        self.set_sender_name(Sender.Sender_name)
        self.set_sender_email(Sender.Sender_email)
        self.click_on_certificate_theme_field()
        self.choose_certificate_theme()
        self.put_certificate_amount(Recipient.Amount)
        self.save_voucher()
        self.logger.info("Voucher is added")

    @allure.step("Нажимаем на кнопку добавления адреса оплаты")
    def click_on_add_payment_address(self):
        return self.find_element_located_click(OrderPageLocators.PAYMENT_ADDRESS_BUTTON)

    @allure.step("Появление всплывающего окна для указания адреса оплаты")
    def appearance_payment_address_form(self):
        return self.find_element_located(OrderPageLocators.PAYMENT_ADDRESS_FORM)

    @allure.step("Указываем имя плательщика")
    def set_payment_name(self, payment_name):
        self.find_element_located_click(OrderPageLocators.PAYMENT_FIRST_NAME)
        self.find_element_located(OrderPageLocators.PAYMENT_FIRST_NAME).clear()
        return self.find_element_located(OrderPageLocators.PAYMENT_FIRST_NAME).send_keys(payment_name)

    @allure.step("Указываем фамилию плательщика")
    def set_payment_last_name(self, payment_last_name):
        self.find_element_located_click(OrderPageLocators.PAYMENT_LAST_NAME)
        self.find_element_located(OrderPageLocators.PAYMENT_LAST_NAME).clear()
        return self.find_element_located(OrderPageLocators.PAYMENT_LAST_NAME).send_keys(payment_last_name)

    @allure.step("Указываем адресс плательщика")
    def set_payment_address(self, payment_address):
        self.find_element_located_click(OrderPageLocators.PAYMENT_ADDRESS)
        self.find_element_located(OrderPageLocators.PAYMENT_ADDRESS).clear()
        return self.find_element_located(OrderPageLocators.PAYMENT_ADDRESS).send_keys(payment_address)

    @allure.step("Указываем город плательщика")
    def set_payment_city(self, payment_city):
        self.find_element_located_click(OrderPageLocators.PAYMENT_CITY)
        self.find_element_located(OrderPageLocators.PAYMENT_CITY).clear()
        return self.find_element_located(OrderPageLocators.PAYMENT_CITY).send_keys(payment_city)

    @allure.step("Указываем почтовый код получателя")
    def set_payment_postcode(self, payment_postcode):
        self.find_element_located_click(OrderPageLocators.PAYMENT_POSTCODE)
        self.find_element_located(OrderPageLocators.PAYMENT_POSTCODE).clear()
        return self.find_element_located(OrderPageLocators.PAYMENT_POSTCODE).send_keys(payment_postcode)

    @allure.step("Нажимаем на поле выбора страны плательщика")
    def click_on_payment_country_field(self):
        return self.find_element_located_click(OrderPageLocators.PAYMENT_COUNTRY_FIELD)

    @allure.step("Указываем страну плательщика")
    def choose_payment_country(self):
        return self.find_element_located_click(OrderPageLocators.PAYMENT_COUNTRY)

    @allure.step("Нажимаем на поле выбора региона плательщика")
    def click_on_payment_region_field(self):
        return self.find_element_located_click(OrderPageLocators.PAYMENT_REGION_FIELD)

    @allure.step("Указываем регион плательщика")
    def choose_payment_region(self):
        return self.find_element_located_click(OrderPageLocators.PAYMENT_REGION)

    @allure.step("Сохраняем информацию о плательщике")
    def save_information_about_payer(self):
        return self.find_element_located_click(OrderPageLocators.SAVE_PAYMENT_DETAILS_BUTTON)

    @allure.step("Закрываем форму добавления адреса плательщика")
    def close_payment_details_form(self):
        return self.find_element_located_click(OrderPageLocators.CLOSE_POPUP_PAYMENT_ADDRESS_BUTTON)

    @allure.step("Вносим информацию о плательщике")
    def add_payment_information(self):
        self.click_on_add_payment_address()
        self.appearance_payment_address_form()
        self.set_payment_name(Customer.Name)
        self.set_payment_last_name(Customer.Last_name)
        self.set_payment_address(Customer.Address)
        self.set_payment_city(Customer.City)
        self.set_payment_postcode(Customer.Postcode)
        self.click_on_payment_country_field()
        self.choose_payment_country()
        self.click_on_payment_region_field()
        self.choose_payment_region()
        self.save_information_about_payer()
        self.close_payment_details_form()
        self.logger.info("Payment address is added")

    @allure.step("Нажимаем на кнопку добавления адреса доставки")
    def click_on_add_shipping_address(self):
        return self.find_element_located_click(OrderPageLocators.SHIPPING_ADDRESS_BUTTON)

    @allure.step("Появление всплывающего окна для указания адреса доставки")
    def appearance_shipping_address_form(self):
        return self.find_element_located(OrderPageLocators.SHIPPING_ADDRESS_FORM)

    @allure.step("Указываем имя получателя")
    def set_shipping_name(self, shipping_name):
        self.find_element_located_click(OrderPageLocators.SHIPPING_FIRST_NAME)
        self.find_element_located(OrderPageLocators.SHIPPING_FIRST_NAME).clear()
        return self.find_element_located(OrderPageLocators.SHIPPING_FIRST_NAME).send_keys(shipping_name)

    @allure.step("Указываем фамилию получателя")
    def set_shipping_last_name(self, shipping_last_name):
        self.find_element_located_click(OrderPageLocators.SHIPPING_LAST_NAME)
        self.find_element_located(OrderPageLocators.SHIPPING_LAST_NAME).clear()
        return self.find_element_located(OrderPageLocators.SHIPPING_LAST_NAME).send_keys(shipping_last_name)

    @allure.step("Указываем адресс получателя")
    def set_shipping_address(self, shipping_address):
        self.find_element_located_click(OrderPageLocators.SHIPPING_ADDRESS)
        self.find_element_located(OrderPageLocators.SHIPPING_ADDRESS).clear()
        return self.find_element_located(OrderPageLocators.SHIPPING_ADDRESS).send_keys(shipping_address)

    @allure.step("Указываем город получателя")
    def set_shipping_city(self, shipping_city):
        self.find_element_located_click(OrderPageLocators.SHIPPING_CITY)
        self.find_element_located(OrderPageLocators.SHIPPING_CITY).clear()
        return self.find_element_located(OrderPageLocators.SHIPPING_CITY).send_keys(shipping_city)

    @allure.step("Указываем почтовый код получателя")
    def set_shipping_postcode(self, shipping_postcode):
        self.find_element_located_click(OrderPageLocators.SHIPPING_POSTCODE)
        self.find_element_located(OrderPageLocators.SHIPPING_POSTCODE).clear()
        return self.find_element_located(OrderPageLocators.SHIPPING_POSTCODE).send_keys(shipping_postcode)

    @allure.step("Нажимаем на поле выбора страны получателя")
    def click_on_shipping_country_field(self):
        return self.find_element_located_click(OrderPageLocators.SHIPPING_COUNTRY_FIELD)

    @allure.step("Указываем страну получателя")
    def choose_shipping_country(self):
        return self.find_element_located_click(OrderPageLocators.SHIPPING_COUNTRY)

    @allure.step("Нажимаем на поле выбора региона получателя")
    def click_on_shipping_region_field(self):
        return self.find_element_located_click(OrderPageLocators.SHIPPING_REGION_FIELD)

    @allure.step("Указываем регион получателя")
    def choose_shipping_region(self):
        return self.find_element_located_click(OrderPageLocators.SHIPPING_REGION)

    @allure.step("Сохраняем информацию о получателе")
    def save_information_about_recipient(self):
        return self.find_element_located_click(OrderPageLocators.SHIPPING_PAYMENT_DETAILS_BUTTON)

    @allure.step("Закрываем форму добавления адреса получателя")
    def close_shipping_details_form(self):
        return self.find_element_located_click(OrderPageLocators.CLOSE_POPUP_SHIPPING_ADDRESS_BUTTON)

    @allure.step("Вносим информацию о получателе")
    def add_shipping_information(self):
        self.click_on_add_shipping_address()
        self.appearance_shipping_address_form()
        self.set_shipping_name(Recipient.Recipient_name)
        self.set_shipping_last_name(Recipient.Recipient_last_name)
        self.set_shipping_address(Recipient.Recipient_address)
        self.set_shipping_city(Recipient.Recipient_city)
        self.set_shipping_postcode(Recipient.Recipient_postcode)
        self.click_on_shipping_country_field()
        self.choose_shipping_country()
        self.click_on_shipping_region_field()
        self.choose_shipping_region()
        self.save_information_about_recipient()
        self.close_shipping_details_form()
        self.logger.info("Shipping address is added")

    @allure.step("Выбираем способ доставки")
    def click_on_shipping_method_button(self):
        shipping_method_button = self.find_element_located(OrderPageLocators.SHIPPING_METHOD_BUTTON)
        self.driver.execute_script("arguments[0].click();", shipping_method_button)

    @allure.step("Появление формы выбора метода доставки")
    def appearance_shipping_method_form(self):
        return self.find_element_located(OrderPageLocators.POPUP_SHIPPING_METHOD_FORM)

    @allure.step("Ставим чекбокс напротив стоимости доставки")
    def click_on_shipping_rate_checkbox(self):
        return self.find_element_located_click(OrderPageLocators.SHIPPING_RATE_CHECKBOX)

    @allure.step("Нажимаем на кнопку continue")
    def click_on_shipping_continue_button(self):
        return self.find_element_located_click(OrderPageLocators.SHIPPING_METHOD_CONTINUE)

    @allure.step("Закрываем форму способа доставки")
    def close_shipping_method_form(self):
        return self.find_element_located_click(OrderPageLocators.CLOSE_POPUP_SHIPPING_METHOD_BUTTON)

    @allure.step("Вносим информацию о методе доставки")
    def add_information_about_shipping_method(self):
        self.click_on_shipping_method_button()
        self.appearance_shipping_method_form()
        self.click_on_shipping_rate_checkbox()
        self.click_on_shipping_continue_button()
        self.close_shipping_method_form()
        self.logger.info("Information about shipping method is added")

    @allure.step("Выбираем способ оплаты")
    def click_on_payment_method_button(self):
        payment_method_button = self.find_element_located(OrderPageLocators.PAYMENT_METHOD_BUTTON)
        self.driver.execute_script("arguments[0].click();", payment_method_button)

    @allure.step("Появление формы выбора способа оплаты")
    def appearance_payment_method_form(self):
        return self.find_element_located(OrderPageLocators.POPUP_PAYMENT_METHOD_FORM)

    @allure.step("Ставим чекбокс напротив способа оплаты")
    def click_on_payment_method_checkbox(self):
        return self.find_element_located_click(OrderPageLocators.PAYMENT_METHOD_CHECKBOX)

    @allure.step("Нажимаем на кнопку continue")
    def click_on_payment_continue_button(self):
        return self.find_element_located_click(OrderPageLocators.PAYMENT_METHOD_CONTINUE)

    @allure.step("Закрываем форму способа оплаты")
    def close_payment_method_form(self):
        return self.find_element_located_click(OrderPageLocators.CLOSE_POPUP_PAYMENT_METHOD_BUTTON)

    @allure.step("Вносим информацию о способе оплаты")
    def add_information_about_payment_method(self):
        self.click_on_payment_method_button()
        self.appearance_payment_method_form()
        self.click_on_payment_method_checkbox()
        self.click_on_payment_continue_button()
        self.close_payment_method_form()
        self.logger.info("Information about payment method is added")

    @allure.step("Нажимаем на кнопку подтверждения заказа")
    def click_on_confirm_order_button(self):
        confirm_order_button = self.find_element_located(OrderPageLocators.CONFIRM_ORDER_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView();", confirm_order_button)
        return self.driver.execute_script("arguments[0].click();", confirm_order_button)

    @allure.step("Переходим на общую страницу заказов")
    def go_to_order_page(self):
        return self.find_element_located_click(OrderPageLocators.ORDERS_LINK)

    @allure.step("Загрузка списка заказов")
    def loading_orders_list(self):
        return self.find_element_located(OrderPageLocators.ORDER_LIST)

    @allure.step("Завершение создания заказа")
    def completion_of_order_creation(self):
        self.click_on_confirm_order_button()
        self.logger.info("Confirm button is pressed")
        self.go_to_order_page()
        self.loading_orders_list()
        self.logger.info("Order is created")

    @allure.step("Получаем имя клиента")
    def get_customer_name(self):
        return self.find_element_located(OrderPageLocators.CUSTOMER_NAME).text

    @allure.step("Получаем статус заказа")
    def get_order_status(self):
        return self.find_element_located(OrderPageLocators.ORDER_STATUS).text

    @allure.step("Устанавливаем чекбокс напротив созданного заказа")
    def click_on_order_checkbox(self):
        return self.find_element_located_click(OrderPageLocators.ORDER_CHECKBOX)

    @allure.step("Нажимаем на кнопку удаления заказа")
    def click_on_delete_order_button(self):
        return self.find_element_located_click(OrderPageLocators.DELETE_ORDER_BUTTON)

    @allure.step("Удаляем заказ")
    def delete_order(self):
        self.click_on_order_checkbox()
        self.click_on_delete_order_button()
        alert = self.driver.switch_to.alert
        alert.accept()
        self.driver.refresh()
        self.logger.info("Order is deleted")

    @allure.step("Добавление заказа для АПИ")
    def add_product_for_api(self):
        self.click_on_add_product_button()
        self.appearance_popup_add_product()
        self.click_on_choose_product_field()
        self.choose_product()
        self.set_product_quantity(Product.Quantity)
        self.click_on_choose_color_field()
        self.choose_color()
        self.click_on_save_product_button()
        self.close_product_form()

    @allure.step("Получаем ID заказа")
    def get_order_id(self):
        return self.find_element_located(OrderPageLocators.ORDER_ID).text
