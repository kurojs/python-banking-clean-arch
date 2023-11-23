from datetime import datetime

from pydantic import BaseModel


class Account(BaseModel):
    account_id: int
    customer_id: int
    account_number: str
    balance: float
    created_at: datetime
    updated_at: datetime

    def deposit(self, amount: float):
        self.balance += amount

    def withdraw(self, amount: float):
        self.balance -= amount

    def get_balance(self):
        return self.balance
