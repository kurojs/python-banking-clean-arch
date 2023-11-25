from abc import ABC, abstractmethod
from typing import Any

from core.domain.customer import Customer


class CustomerRepository(ABC):
    session: Any

    @abstractmethod
    def create(self, customer: Customer) -> Customer:
        raise NotImplementedError

    @abstractmethod
    def get(self, customer_id: int) -> Customer:
        raise NotImplementedError

    @abstractmethod
    def get_by_account_id(self, account_id: int) -> Customer:
        raise NotImplementedError
