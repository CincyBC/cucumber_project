from fastapi import APIRouter, FastAPI
from routers import orders, products
from dependencies import database

app = FastAPI()

app = APIRouter(
    prefix="/api",
    tags=["api"],
    responses={404: {"description": "Not found"}},
)

app.include_router(orders.router)
app.include_router(products.router)

app.add_event_handler("startup", database.get_database_connection)
