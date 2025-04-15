import allure
from diplom_opencart.pages.base_page import BasePage
from diplom_opencart.locators.customer_page_locators import CustomerPageLocators
from diplom_opencart.helper import Customer


class CustomerPage(BasePage):

    @allure.step("Получаем имя клиента")
    def get_customer_name(self):
        return self.find_element_located(CustomerPageLocators.CUSTOMER_NAME).text

    @allure.step("Устанавливаем чек-бокс на клиенте, которого необходимо удалить")
    def click_on_checkbox_customer(self):
        return self.find_element_located_click(CustomerPageLocators.CHECKBOX_CUSTOMER)

    @allure.step("Нажимаем на кнопку удаления клиента")
    def click_on_delete_customer(self):
        return self.find_element_located_click(CustomerPageLocators.DELETE_CUSTOMER)

    @allure.step("Удаляем клиента")
    def delete_customer(self):
        self.click_on_checkbox_customer()
        self.click_on_delete_customer()
        alert = self.driver.switch_to.alert
        alert.accept()
        self.driver.refresh()
        self.logger.info("Customer is deleted")

    @allure.step("Появление всплывающего окна для добавления клиента")
    def appearance_popup_customer_form(self):
        return self.find_element_located(CustomerPageLocators.POPUP_CUSTOMER_FORM)

    @allure.step("Указываем имя покупателя")
    def set_customer_name(self, customer_name):
        self.find_element_located_click(CustomerPageLocators.CUSTOMER_FIRST_NAME_FIELD)
        self.find_element_located(CustomerPageLocators.CUSTOMER_FIRST_NAME_FIELD).clear()
        return self.find_element_located(CustomerPageLocators.CUSTOMER_FIRST_NAME_FIELD).send_keys(customer_name)

    @allure.step("Указываем фамилию покупателя")
    def set_customer_last_name(self, customer_last_name):
        self.find_element_located_click(CustomerPageLocators.CUSTOMER_LAST_NAME_FIELD)
        self.find_element_located(CustomerPageLocators.CUSTOMER_LAST_NAME_FIELD).clear()
        return self.find_element_located(CustomerPageLocators.CUSTOMER_LAST_NAME_FIELD).send_keys(customer_last_name)

    @allure.step("Указываем email покупателя")
    def set_customer_email(self, email):
        self.find_element_located_click(CustomerPageLocators.CUSTOMER_EMAIL)
        self.find_element_located(CustomerPageLocators.CUSTOMER_EMAIL).clear()
        return self.find_element_located(CustomerPageLocators.CUSTOMER_EMAIL).send_keys(email)

    @allure.step("Указываем телефон покупателя")
    def set_customer_phone(self, phone):
        self.find_element_located_click(CustomerPageLocators.CUSTOMER_PHONE)
        self.find_element_located(CustomerPageLocators.CUSTOMER_PHONE).clear()
        return self.find_element_located(CustomerPageLocators.CUSTOMER_PHONE).send_keys(phone)

    @allure.step("Сохраняем данные покупателя")
    def save_customer_information(self):
        return self.find_element_located_click(CustomerPageLocators.SAVE_CUSTOMER)

    @allure.step("Закрываем форму заполнения информации о покупателе")
    def close_customer_form(self):
        return self.find_element_located_click(CustomerPageLocators.CLOSE_CUSTOMER_FORM)

    @allure.step("Добавляем информацию о покупателе")
    def add_customer_information(self):
        self.appearance_popup_customer_form()
        self.set_customer_name(Customer.Name)
        self.set_customer_last_name(Customer.Last_name)
        self.set_customer_email(Customer.Email)
        self.set_customer_phone(Customer.Phone)
        self.save_customer_information()
        self.close_customer_form()
        self.logger.info("Customer's information is added")
