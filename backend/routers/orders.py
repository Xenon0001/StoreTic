from fastapi import APIRouter, HTTPException
from db import SessionLocal
from models import Order, Sale
from datetime import datetime

router = APIRouter(
    prefix="/orders",
    tags=["orders"]
)


@router.get("/pending")
def get_pending_orders():
    db = SessionLocal()
    try:
        return db.query(Order).filter(Order.status == "PENDING").all()
    finally:
        db.close()


@router.post("/{order_id}/confirm")
def confirm_order(order_id: int):
    db = SessionLocal()
    try:
        order = db.query(Order).get(order_id)
        if not order or order.status != "PENDING":
            raise HTTPException(status_code=404, detail="Pedido no válido")

        sale = Sale(
            total=order.total_amount,
            created_at=datetime.utcnow()
        )

        order.status = "CONFIRMED"

        db.add(sale)
        db.commit()

        return {"message": "Pedido confirmado y venta creada"}

    finally:
        db.close()


@router.post("/{order_id}/cancel")
def cancel_order(order_id: int):
    db = SessionLocal()
    try:
        order = db.query(Order).get(order_id)
        if not order or order.status != "PENDING":
            raise HTTPException(status_code=404, detail="Pedido no válido")

        order.status = "CANCELED"
        db.commit()

        return {"message": "Pedido cancelado"}

    finally:
        db.close()
