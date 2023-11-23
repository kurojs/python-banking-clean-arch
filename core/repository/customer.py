from abc import ABC, abstractmethod

from core.domain.customer import Customer


class CustomerRepository(ABC):
    @abstractmethod
    def create(self, customer: Customer) -> Customer:
        pass

    @abstractmethod
    def get(self, customer_id: int) -> Customer:
        pass

    @abstractmethod
    def get_by_account_id(self, account_id: int) -> Customer:
        pass
