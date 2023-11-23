from abc import ABC, abstractmethod

from core.domain.account import Account


class AccountRepository(ABC):
    @abstractmethod
    def create_account(self, account: Account) -> Account:
        pass

    @abstractmethod
    def get_account(self, account_id: int) -> Account:
        pass
