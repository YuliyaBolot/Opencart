import pytest
import requests
import mysql.connector
from diplom_opencart.helper import IP_ADDRESS, Constants, Urls
from diplom_opencart.pages.admin_login_page import AdminLoginPage
from diplom_opencart.pages.admin_main_page import AdminMainPage
from diplom_opencart.pages.api_page import ApiPage
from diplom_opencart.pages.order_page import OrderPage
from diplom_opencart.pages.customer_page import CustomerPage


@pytest.fixture()
def base_url():
    return f"http://{IP_ADDRESS}/index.php?route=api"


@pytest.fixture()
def get_api_key(browser):
    """
    фикстура, возвращающая API KEY
    """
    admin_page = AdminMainPage(browser)
    admin_page.go_to_api_page()
    api_page = ApiPage(browser)
    api_page.add_api_information(Constants.ADMIN_LOGIN, Constants.IP_ADDRESS_APPLICATION)
    api_key = api_page.get_api_key()
    return api_key


@pytest.fixture()
def get_api_token(get_api_key, base_url):
    """
    фикстура, возвращающая API TOKEN
    """
    payload = f'username={Constants.ADMIN_LOGIN}&key={get_api_key}'
    response = requests.post(f"{base_url}/account/login", data=payload, verify=False)
    token = response.json()['api_token']
    return token


@pytest.fixture()
def delete_api_and_order(browser):
    """
    фикстура, удаляющая API и заказ
    """
    browser.get(Urls.URL_LOGIN_TO_ADMIN)
    auth_admin = AdminLoginPage(browser)
    auth_admin.authorization_admin(Constants.ADMIN_LOGIN, Constants.ADMIN_PASSWORD)
    yield delete_api_and_order
    order_page = OrderPage(browser)
    order_page.delete_order()
    admin_page = AdminMainPage(browser)
    admin_page.go_to_api_page()
    api_page = ApiPage(browser)
    api_page.delete_api()


@pytest.fixture()
def create_order(browser):
    """
   фикстура, создающая заказ и возвращающая его ID
   """
    admin_page = AdminMainPage(browser)
    admin_page.go_to_orders_page()
    order_page = OrderPage(browser)
    order_page.start_add_new_order()
    customer_page = CustomerPage(browser)
    customer_page.add_customer_information()
    order_page.add_product_for_api()
    order_page.add_payment_information()
    order_page.add_shipping_information()
    order_page.add_information_about_shipping_method()
    order_page.add_information_about_payment_method()
    order_page.completion_of_order_creation()
    id_order = order_page.get_order_id()
    return id_order


@pytest.fixture()
def delete_api(browser):
    """
    фикстура, удаляющая API
    """
    browser.get(Urls.URL_LOGIN_TO_ADMIN)
    auth_admin = AdminLoginPage(browser)
    auth_admin.authorization_admin(Constants.ADMIN_LOGIN, Constants.ADMIN_PASSWORD)
    yield delete_api
    admin_page = AdminMainPage(browser)
    admin_page.go_to_api_page()
    api_page = ApiPage(browser)
    api_page.delete_api()


@pytest.fixture()
def conn_oc_order():
    """
    фикстура подключения к базе данных (для заказов)
    """
    conn = mysql.connector.connect(
        host='localhost',
        port='3306',
        user='bn_opencart',
        database='bitnami_opencart',
        charset='utf8mb4',
        collation='utf8mb4_unicode_ci'
    )
    yield conn
    conn.close()


@pytest.fixture()
def conn_oc_cart(browser, base_url):
    """
    фикстура подключения к базе данных (для корзины)
    """
    conn = mysql.connector.connect(
        host='localhost',
        port='3306',
        user='bn_opencart',
        database='bitnami_opencart',
        charset='utf8mb4',
        collation='utf8mb4_unicode_ci'
    )
    yield conn
    with conn.cursor(buffered=True) as cursor:
        cursor.execute("SELECT cart_id, session_id FROM oc_cart")
        result = cursor.fetchone()
        requests.post(f'{base_url}/sale/cart.remove&api_token={result[1]}', data=f'key={result[0]}', verify=False)
    conn.close()
