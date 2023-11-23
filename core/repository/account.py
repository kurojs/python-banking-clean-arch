from abc import ABC, abstractmethod

from core.domain.account import Account


class AccountRepository(ABC):
    @abstractmethod
    def create(self, account: Account) -> Account:
        pass

    @abstractmethod
    def get(self, account_id: int) -> Account:
        pass

    @abstractmethod
    def save(self, account) -> Account:
        pass
