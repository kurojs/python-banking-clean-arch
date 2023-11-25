from typing import Optional

from pydantic import BaseModel


class Customer(BaseModel):
    id: Optional[int] = None
    name: str
    email: str
    phone_number: str
