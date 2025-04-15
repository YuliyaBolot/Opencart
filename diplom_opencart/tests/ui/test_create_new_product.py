import allure
from diplom_opencart.helper import Product, Urls
from diplom_opencart.pages.admin_main_page import AdminMainPage
from diplom_opencart.pages.main_page import MainPage
from diplom_opencart.pages.product_page import ProductPage
from diplom_opencart.pages.add_new_product_page import AddNewProductPage


class TestCreateNewProduct:

    @allure.epic("Тестирование заведения нового товара")
    @allure.title("Создание нового товара")
    def test_create_new_products(self, browser, admin_authorization, delete_product_from_admin):
        admin_page = AdminMainPage(driver=browser)
        admin_page.go_to_admin_product_page()
        add_new_product_page = AddNewProductPage(driver=browser)
        add_new_product_page.create_new_product()
        browser.get(Urls.URL_HOME)
        main_page = MainPage(driver=browser)
        main_page.move_to_product_page()
        product_page = ProductPage(driver=browser)
        product_page.loading_product_list()
        new_product = product_page.find_new_added_product().text
        assert new_product == Product.Name
