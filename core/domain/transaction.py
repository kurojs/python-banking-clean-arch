from datetime import datetime
from enum import Enum

from pydantic import BaseModel


class TransactionType(Enum):
    DEPOSIT = "deposit"
    WITHDRAW = "withdraw"


class Transaction(BaseModel):
    id: int
    amount: float
    transaction_type: TransactionType
    account_id: int
    created_at: datetime
    updated_at: datetime
