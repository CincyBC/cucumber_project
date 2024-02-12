from fastapi import APIRouter
router = APIRouter(
    prefix="/products",
    tags=["products"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
def get_products():
    pass


@router.get("/{id}")
def get_product(id: int):
    pass


@router.post("/")
def create_product():
    pass


@router.put("/{id}")
def update_product(id: int):
    pass