import requests
from pydantic import BaseModel
from typing import List


class SuccessResponseVoucher(BaseModel):
    success: str

    @classmethod
    def validate_response_voucher(cls, response: requests.Response):
        response.raise_for_status()
        return cls(**response.json())


class SuccessResponseOrder(BaseModel):
    order_id: int
    success: str
    points: int
    commission: str

    @classmethod
    def validate_response_order(cls, response: requests.Response):
        response.raise_for_status()
        return cls(**response.json())


class Products(BaseModel):
    cart_id: str
    product_id: str
    name: str
    model: str
    option: List
    subscription: str
    quantity: str
    stock: bool
    minimum: bool
    reward: int
    price: str
    total: str


class Totals(BaseModel):
    title: str
    text: str


class SuccessResponseCart(BaseModel):
    products: List[Products]
    vouchers: List
    totals: List[Totals]
    shipping_required: bool

    @classmethod
    def validate_response_cart(cls, response: requests.Response):
        response.raise_for_status()
        return cls(**response.json())
