# Backend main entry point
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from db import Base, engine
from routers import products, sales, auth, orders
from app.routers import web

app = FastAPI(title="StoreTic API")

app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static"
)


app.include_router(products.router)
app.include_router(orders.router)
app.include_router(sales.router)
app.include_router(auth.router)
app.include_router(web.router, prefix="/web")

Base.metadata.create_all(bind=engine)
