import pytest
from fastapi.testclient import TestClient
from api.app import app

client = TestClient(app)

order_data = {
    "stoks": "EURUSD",
    "quantity": 100.0
}


def test_create_order():
    response = client.post("/orders", json=order_data)
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["stoks"] == order_data["stoks"]
    assert data["quantity"] == order_data["quantity"]
    assert data["status"] == "PENDING"


def test_get_all_orders():
    response = client.get("/orders")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


def test_get_order_by_id():
    response = client.post("/orders", json=order_data)
    order_id = response.json()["id"]

    response = client.get(f"/orders/{order_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == order_id
    assert data["stoks"] == order_data["stoks"]
    assert data["quantity"] == order_data["quantity"]
    assert data["status"] == "PENDING"


def test_cancel_order():
    response = client.post("/orders", json=order_data)
    order_id = response.json()["id"]

    response = client.delete(f"/orders/{order_id}")
    assert response.status_code == 204


# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from enum import Enum
# import random
# import asyncio
# import websockets
# import uvicorn
# app = FastAPI()
#
# # In-memory database for orders
# orders = {}
#
#
# class OrderStatus(str, Enum):
#     PENDING = "PENDING"
#     EXECUTED = "EXECUTED"
#     CANCELLED = "CANCELLED"
#
#
# class Order(BaseModel):
#     stoks: str
#     quantity: float
#     status: OrderStatus = OrderStatus.PENDING
#
#
# @app.get("/orders", response_model=list[Order])
# async def get_orders():
#     await asyncio.sleep(random.uniform(0.1, 1))
#     return list(orders.values())
#
#
# @app.post("/orders", response_model=Order, status_code=201)
# async def create_order(order: Order):
#     order_id = str(random.randint(1000, 9999))
#     orders[order_id] = order
#     await asyncio.sleep(random.uniform(0.1, 1))
#     return order
#
#
# @app.get("/orders/{order_id}", response_model=Order)
# async def read_order(order_id: str):
#     if order_id not in orders:
#         raise HTTPException(status_code=404, detail="Order not found")
#     await asyncio.sleep(random.uniform(0.1, 1))
#     return orders[order_id]
#
#
# @app.delete("/orders/{order_id}", status_code=204)
# async def cancel_order(order_id: str):
#     if order_id not in orders:
#         raise HTTPException(status_code=404, detail="Order not found")
#     del orders[order_id]
#     await asyncio.sleep(random.uniform(0.1, 1))
#
#
# connected_clients = set()
#
#
# async def notify_clients(order_id: str, status: OrderStatus):
#     if not connected_clients:
#         return
#     message = f"Order {order_id} status: {status}"
#     await asyncio.gather(
#         *[client.send(message) for client in connected_clients]
#     )
#
#
# @app.websocket("/ws/{client_id}")
# async def websocket_endpoint(websocket, client_id: str):
#     await websocket.accept()
#     connected_clients.add(websocket)
#     try:
#         while True:
#             data = await websocket.receive_text()
#             # Process WebSocket messages if needed
#     except websockets.exceptions.ConnectionClosed:
#         pass
#     finally:
#         connected_clients.remove(websocket)
#
#
# if __name__ == "__main__":
#
#     from api.app import app  # Adjust the import path accordingly
#
#     uvicorn.run(app, host="0.0.0.0", port=8080)