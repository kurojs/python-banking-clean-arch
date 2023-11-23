from pydantic import BaseModel
from typing import List

from core.domain.account import Account
from core.domain.customer import Customer
from core.domain.transaction import Transaction


class AccountStatement(BaseModel):
    account: Account
    customer: Customer
    transactions: List[Transaction]

    def __str__(self):
        return f"AccountStatement(account={self.account}, customer={self.customer}, transactions={self.transactions})"
