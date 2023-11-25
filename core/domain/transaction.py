from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel


class TransactionType(Enum):
    DEPOSIT = "deposit"
    WITHDRAW = "withdraw"


class Transaction(BaseModel):
    id: Optional[int] = None
    amount: float
    transaction_type: TransactionType
    account_id: int
    created_at: datetime = datetime.now()
