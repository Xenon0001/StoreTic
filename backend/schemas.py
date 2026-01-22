# Pydantic schemas
from pydantic import BaseModel
from typing import List
from datetime import datetime


class ProductCreate(BaseModel):
    name: str
    price: float
    stock: int

class ProductOut(ProductCreate):
    id: int

    class Config:
        from_attributes = True

class SaleItemCreate(BaseModel):
    product_id: int
    quantity: int

class SaleItemOut(BaseModel):
    id: int
    product_id: int
    quantity: int
    price: float

    class Config:
        from_attributes = True

class SaleCreate(BaseModel):
    items: List[SaleItemCreate]

class SaleOut(BaseModel):
    id: int
    total: float
    date: str
    items: List[SaleItemOut]

    class Config:
        from_attributes = True

class SalesSummary(BaseModel):
    total_sales_count: int
    total_amount: float
    average_sale: float

# PEDIDOS
class OrderCreate(BaseModel):
    customer_name: str
    total_amount: float


class OrderResponse(BaseModel):
    id: int
    customer_name: str
    total_amount: float
    status: str
    created_at: datetime

    class Config:
        from_attributes = True