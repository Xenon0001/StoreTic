from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from db import SessionLocal
from models import Order
from schemas import OrderCreate


router = APIRouter(
    tags=["web"]
)

templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
def web_home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )

@router.post("/orders")
def create_web_order(order: OrderCreate):
    db = SessionLocal()
    try:
        new_order = Order(
            customer_name=order.customer_name,
            total_amount=order.total_amount,
        )
        db.add(new_order)
        db.commit()
        db.refresh(new_order)
        return {"message": "Pedido enviado al administrador"}
    finally:
        db.close()