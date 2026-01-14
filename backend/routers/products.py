# Products router
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import SessionLocal
from models import Product
from schemas import ProductCreate

router = APIRouter(prefix="/products")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    return {"message": "Producto creado"}

@router.get("/")
def list_products(db: Session = Depends(get_db)):
    return db.query(Product).all()
