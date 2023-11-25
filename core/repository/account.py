from abc import ABC, abstractmethod
from typing import Any

from core.domain.account import Account


class AccountRepository(ABC):
    session: Any

    @abstractmethod
    def create(self, account: Account) -> Account:
        raise NotImplementedError

    @abstractmethod
    def get(self, account_id: int) -> Account:
        raise NotImplementedError

    @abstractmethod
    def save(self, account) -> Account:
        raise NotImplementedError
