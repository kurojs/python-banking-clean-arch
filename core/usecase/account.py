import uuid

from core.domain.account import Account
from core.repository.account import AccountRepository
from core.repository.customer import CustomerRepository

ErrCustomerNotFound = Exception('Customer not found')


class AccountUseCase:
    account_repo: AccountRepository
    customer_repo: CustomerRepository

    def __init__(self, account_repo: AccountRepository,
                 customer_repo: CustomerRepository):
        self.account_repo = account_repo
        self.customer_repo = customer_repo

    def create_account(self, customer_id: int) -> Account:
        customer = self.customer_repo.get(customer_id=customer_id)
        account = Account(customer_id=customer.id, balance=0,
                          account_number=str(uuid.uuid4()))
        return self.account_repo.create(account)
