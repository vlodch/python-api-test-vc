from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import random
import asyncio
import websockets

app = FastAPI()


class OrderInput(BaseModel):
    stoks: str
    quantity: float


class OrderOutput(BaseModel):
    id: str
    stoks: str
    quantity: float
    status: str


orders = {} 


@app.get("/orders")
async def get_orders():
    await asyncio.sleep(random.uniform(0.1, 1))  # Simulate delay
    return list(orders.values())


@app.post("/orders", response_model=OrderOutput, status_code=201)
async def place_order(order: OrderInput):
    order_id = str(random.randint(1000, 9999))
    order_data = dict(order.dict(), id=order_id, status="PENDING")
    orders[order_id] = order_data
    await asyncio.sleep(random.uniform(0.1, 1))  # Simulate delay
    return order_data


@app.get("/orders/{order_id}", response_model=OrderOutput)
async def get_order(order_id: str):
    if order_id not in orders:
        raise HTTPException(status_code=404, detail="Order not found")
    await asyncio.sleep(random.uniform(0.1, 1))  # Simulate delay
    return orders[order_id]


@app.delete("/orders/{order_id}", status_code=204)
async def cancel_order(order_id: str):
    if order_id not in orders:
        raise HTTPException(status_code=404, detail="Order not found")
    del orders[order_id]
    await asyncio.sleep(random.uniform(0.1, 1))

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)
