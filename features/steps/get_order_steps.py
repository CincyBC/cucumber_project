# features/steps/get_order_steps.py

from behave import given, when, then
from src.routers.orders import get_order
from unittest.mock import MagicMock


@given("an order exists in the database with ID {order_id:d}")
def step_impl_given_order_exists(context, order_id):
    # Mock the database connection to return a row for the specified order ID
    context.conn = MagicMock()
    context.conn.fetchrow.return_value = {
        "order_id": order_id,
        "customer_id": 101,
        "employee_id": 201,
        "order_date": "2022-02-14",
        "shipper_id": 301,
    }


@when("I request the order with ID {order_id:d}")
async def step_impl_when_request_order(context, order_id):
    # Call the get_order function with the specified order ID
    context.response = await get_order(order_id, context.conn)


@then("the API should return the order details")
def step_impl_then_return_order_details(context):
    # Assert that the response contains the expected order details
    expected_order_details = {
        "order_id": 1,
        "customer_id": 101,
        "employee_id": 201,
        "order_date": "2022-02-14",
        "shipper_id": 301,
    }
    assert context.response == expected_order_details


@given("no order exists in the database with ID {order_id:d}")
def step_impl_given_no_order_exists(context, order_id):
    # Mock the database connection to return None for the specified order ID
    context.conn = MagicMock()
    context.conn.fetchrow.return_value = None


@then("the API should return a 404 error")
async def step_impl_then_return_404_error(context):
    # Assert that the response is a 404 error
    if hasattr(context, "response"):
        # Assert that the response is a 404 error
        response = await context.response
        assert response.status_code == 404
    else:
        raise AssertionError("Response attribute not found in the context")
