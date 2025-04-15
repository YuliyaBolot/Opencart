import string
from random import choice, randint
from faker import Faker

fake = Faker('ru_RU')

IP_ADDRESS = '192.168.0.192'


class Constants:
    ADMIN_LOGIN = 'user'
    ADMIN_PASSWORD = 'bitnami'
    IP_ADDRESS_APPLICATION = '192.168.65.1'


class Urls:
    URL_LOGIN_TO_ADMIN = f"http://{IP_ADDRESS}//administration"
    URL_HOME = f'http://{IP_ADDRESS}/en-gb?route=common/home'


class Product:
    Name = 'Apple Iphone 15'
    Description = 'New Iphone 15'
    Title = 'Iphone 15'
    Meta_description = 'IPHONE 15'
    Product_model = 'Iphone 15'
    Product_price = 1200.00
    Quantity = 1
    Product_weight = 0.5
    Manufacturer = 'Apple'
    Category = 'Phones & PDAs'
    Reward_points = 120
    Keyword = ''.join(choice(string.ascii_lowercase) for _ in range(64))


class User:
    Name = fake.first_name()
    Last_name = fake.last_name()
    Email = fake.email()
    Password = fake.password()


class Customer:
    Name = fake.first_name()
    Last_name = fake.last_name()
    Email = fake.email()
    Phone = fake.phone_number()
    Address = fake.address()
    City = fake.city()
    Postcode = randint(0, 999999)


class Recipient:
    Recipient_name = fake.first_name()
    Recipient_last_name = fake.last_name()
    Recipient_email = fake.email()
    Amount = randint(1, 1000)
    Recipient_address = fake.address()
    Recipient_city = fake.city()
    Recipient_postcode = randint(0, 999999)


class Sender:
    Sender_name = fake.first_name()
    Sender_email = fake.email()


class Data:
    comment = (f'comment=%D0%9F%D0%BE%D0%B6%D0%B0%D0%BB%D1%83%D0%B9%D1%81%D1%82%D0%B0%2C%20%D1'
               f'%83%D0%BF%D0%B0%D0%BA%D1%83%D0%B9%D1%82%D0%B5%20%D1%82%D0%BE%D0%B2%D0%B0%D1'
               f'%80%20%D0%B2%20%D0%BF%D0%BE%D0%B4%D0%B0%D1%80%D0%BE%D1%87%D0%BD%D1%83%D1'
               f'%8E%20%D0%B1%D1%83%D0%BC%D0%B0%D0%B3%D1%83.%20%D0%98%20%D0%BE%D1%82%D0%BF%D1'
               f'%80%D0%B0%D0%B2%D1%8C%D1%82%D0%B5%20%D0%BA%D0%B0%D0%BA%20%D0%BC%D0%BE%D0%B6%D0%BD%D0%BE%20%D1'
               f'%81%D0%BA%D0%BE%D1%80%D0%B5%D0%B5!')

    voucher = {'from_name': fake.first_name(),
               'from_email': fake.email(),
               'to_name': fake.first_name(),
               'to_email': fake.email(),
               'voucher_theme_id': f'{randint(6, 8)}',
               'message': 'Congratulations!',
               'amount': '1'}

    comment_from_db = 'Пожалуйста, упакуйте товар в подарочную бумагу. И отправьте как можно скорее!'
