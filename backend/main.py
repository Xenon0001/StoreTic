# Backend main entry point
from fastapi import FastAPI
from db import Base, engine
from routers import products, sales, auth

app = FastAPI(title="StoreTic API")

app.include_router(products.router)
app.include_router(sales.router)
app.include_router(auth.router)

Base.metadata.create_all(bind=engine)
