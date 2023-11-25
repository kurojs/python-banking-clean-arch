from typing import Optional

from pydantic import BaseModel


class Account(BaseModel):
    id: Optional[int] = None
    account_number: Optional[str]
    customer_id: int
    balance: float = 0

    def deposit(self, amount: float):
        self.balance += amount

    def withdraw(self, amount: float):
        self.balance -= amount

    def get_balance(self):
        return self.balance
