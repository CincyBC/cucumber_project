from fastapi import APIRouter, FastAPI
from router import orders, products

app = FastAPI()

api = APIRouter(
    prefix="/api",
    tags=["api"],
    responses={404: {"description": "Not found"}},
)

api.include_router(orders.router)
api.include_router(products.router)
