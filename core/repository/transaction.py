from abc import ABC, abstractmethod
from typing import List

from core.domain.transaction import Transaction


class TransactionRepository(ABC):
    @abstractmethod
    def create(self, transaction: Transaction) -> Transaction:
        pass

    @abstractmethod
    def list_by_account_id(self, account_id: int) -> List[Transaction]:
        pass
