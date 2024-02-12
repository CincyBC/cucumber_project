from fastapi import APIRouter, FastAPI
from routers import orders, products

api = FastAPI()

api = APIRouter(
    prefix="/api",
    tags=["api"],
    responses={404: {"description": "Not found"}},
)

api.include_router(orders.router)
api.include_router(products.router)
