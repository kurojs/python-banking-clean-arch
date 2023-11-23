from typing import List

from pydantic import BaseModel

from core.domain.account import Account
from core.domain.customer import Customer
from core.domain.transaction import Transaction


class AccountStatement(BaseModel):
    account: Account
    customer: Customer
    transactions: List[Transaction]

    def __str__(self):
        return (f"AccountStatement("
                f"account={self.account}, "
                f"customer={self.customer},"
                f" transactions={self.transactions})")
