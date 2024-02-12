from datetime import datetime
from fastapi import HTTPException
from routers.orders import get_order
from models.orders import OrdersInDB
import pytest
from unittest.mock import MagicMock, AsyncMock


@pytest.mark.asyncio
async def test_get_order_found():
    # Mock database connection
    conn = MagicMock()
    # Mock data returned from the database
    mock_row = {
        "order_id": 1,
        "customer_id": 101,
        "employee_id": 201,
        "order_date": datetime.now(),
        "shipper_id": 301,
    }
    conn.fetchrow = AsyncMock(return_value=mock_row)

    # Call the function with a valid order id
    response = await get_order(1, conn)

    # Assert that the response is correct
    assert response == OrdersInDB(**mock_row)


@pytest.skip
@pytest.mark.asyncio
async def test_get_order_not_found():
    # Mock database connection
    conn = MagicMock()
    conn.fetchrow = AsyncMock(return_value=None)

    # Call the function with a non-existent order id
    with pytest.raises(HTTPException) as exc_info:
        await get_order(999, conn)

    # Assert that the correct HTTP status code and detail message are raised
    assert exc_info.value.status_code == 404
    assert exc_info.value.detail == "Order not found"


@pytest.mark.asyncio
async def test_get_order_error():
    # Mock database connection to raise an exception
    conn = MagicMock()
    conn.fetchrow = AsyncMock(side_effect=Exception("Database error"))

    # Call the function and assert that it raises an HTTPException with status code 500
    with pytest.raises(HTTPException) as exc_info:
        await get_order(1, conn)

    assert exc_info.value.status_code == 500
