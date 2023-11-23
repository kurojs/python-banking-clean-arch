import uuid

from pydantic import BaseModel

from core.domain.account import Account
from core.domain.customer import Customer
from core.repository.account import AccountRepository
from core.repository.customer import CustomerRepository


class AccountUseCase(BaseModel):
    account_repo: AccountRepository
    customer_repo: CustomerRepository

    def create_account(
            self,
            customer_id: int,
            name: str, email: str,
            phone_number: str
    ) -> Account:
        customer = self.customer_repo.get(customer_id=customer_id)
        account = Account(customer_id=customer.customer_id, balance=0,
                          account_number=uuid.uuid4())
        return self.account_repo.create(account)
