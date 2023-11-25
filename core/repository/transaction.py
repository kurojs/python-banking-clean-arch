from abc import ABC, abstractmethod
from typing import List, Any

from core.domain.transaction import Transaction


class TransactionRepository(ABC):
    session: Any

    @abstractmethod
    def create(self, transaction: Transaction) -> Transaction:
        raise NotImplementedError

    @abstractmethod
    def list_by_account_id(self, account_id: int) -> List[Transaction]:
        raise NotImplementedError
