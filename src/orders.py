from fastapi import APIRouter, HTTPException, Depends
from dependencies.database import get_database_connection
from models.orders import OrdersInDB

router = APIRouter(
    prefix="/orders",
    tags=["orders"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
def get_orders(conn=Depends(get_database_connection)):
    pass


@router.get("/{id}")
async def get_order(id: int, conn=Depends(get_database_connection)):
    try:
        query = "SELECT * FROM orders WHERE order_id = $1"
        row = await conn.fetchrow(query, id)
        if row:
            return OrdersInDB(**row)
        raise HTTPException(status_code=404, detail="Order not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/")
def create_order(conn=Depends(get_database_connection)):
    pass


@router.put("/{id}")
def update_order(id: int, conn=Depends(get_database_connection)):
    pass
