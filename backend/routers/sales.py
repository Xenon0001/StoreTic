from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from db import SessionLocal
from models import Sale, SaleItem, Product
from schemas import SaleCreate, SaleOut, SalesSummary

router = APIRouter(prefix="/sales", tags=["sales"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=dict)
def create_sale(sale: SaleCreate, db: Session = Depends(get_db)):
    """
    Crear una venta con validación de stock:
    1. Validar productos y stock disponible
    2. Crear venta y items
    3. Actualizar stock
    """
    total = 0.0
    sale_items_data = []

    # Validar y recopilar información
    for item in sale.items:
        product = db.query(Product).filter(Product.id == item.product_id).first()

        if not product:
            raise HTTPException(status_code=404, detail=f"Producto {item.product_id} no encontrado")
        
        if product.stock < item.quantity:
            raise HTTPException(
                status_code=400, 
                detail=f"Stock insuficiente para {product.name}. Disponible: {product.stock}"
            )

        subtotal = product.price * item.quantity
        total += subtotal
        sale_items_data.append({
            "product": product,
            "quantity": item.quantity,
            "price": product.price
        })

    # Crear la venta
    new_sale = Sale(total=total)
    db.add(new_sale)
    db.flush()  # Obtener el ID sin hacer commit

    # Crear items y actualizar stock
    for item_data in sale_items_data:
        sale_item = SaleItem(
            sale_id=new_sale.id,
            product_id=item_data["product"].id,
            quantity=item_data["quantity"],
            price=item_data["price"]
        )
        db.add(sale_item)
        item_data["product"].stock -= item_data["quantity"]

    db.commit()

    return {"message": "Venta registrada", "sale_id": new_sale.id, "total": total}

@router.get("/summary")
def get_sales_summary(db: Session = Depends(get_db)):
    """Obtener resumen de ventas: total de ventas, cantidad de ventas, promedio"""
    sales = db.query(Sale).all()
    
    total_count = len(sales)
    total_amount = db.query(func.sum(Sale.total)).scalar() or 0.0
    average_sale = total_amount / total_count if total_count > 0 else 0.0
    
    return {
        "total_sales_count": total_count,
        "total_amount": total_amount,
        "average_sale": average_sale
    }