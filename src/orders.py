from fastapi import APIRouter
router = APIRouter(
    prefix="/orders",
    tags=["orders"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
def get_orders():
    pass


@router.get("/{id}")
def get_order(id: int):
    pass


@router.post("/")
def create_order():
    pass


@router.put("/{id}")
def update_order(id: int):
    pass