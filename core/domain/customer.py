from pydantic import BaseModel


class Customer(BaseModel):
    customer_id: int
    name: str
    email: str
    phone_number: str
