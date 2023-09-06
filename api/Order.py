from pydantic import BaseModel


class OrderModel(BaseModel):
    order_id: str
    symbol: str
    quantity: float
    status: str


order_data = {
    "order_id": "12345",
    "symbol": "EURUSD",
    "quantity": 100.0,
    "status": "PENDING"
}

order_model = OrderModel(**order_data)
print(order_model.dict())


class Order:
    def __init__(self, order_id, symbol, quantity, status):
        self.order_id = order_id
        self.symbol = symbol
        self.quantity = quantity
        self.status = status

    def to_dict(self):
        return {
            'order_id': self.order_id,
            'symbol': self.symbol,
            'quantity': self.quantity,
            'status': self.status,
        }

    def __str__(self):
        return f"Order ID: {self.order_id}, Symbol: {self.symbol}, Quantity: {self.quantity}, Status: {self.status}"


order = Order(order_id="12345", symbol="EURUSD", quantity=100, status="PENDING")
print(order.to_dict())
print(str(order))
