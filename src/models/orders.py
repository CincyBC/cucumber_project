from pydantic import BaseModel
from datetime import datetime


class Orders(BaseModel):
    customer_id: int
    employee_id: int
    order_date: str
    shipper_id: int


class OrdersInDB(BaseModel):
    order_id: int
    customer_id: int
    employee_id: int
    order_date: datetime
    shipper_id: int

    @classmethod
    def from_db(cls, row):
        row["order_date"] = str(row["order_date"])
        return cls(**row)
