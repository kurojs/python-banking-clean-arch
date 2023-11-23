from pydantic import BaseModel

from core.domain.account_statement import AccountStatement
from core.repository.account import AccountRepository
from core.repository.customer import CustomerRepository
from core.repository.transaction import TransactionRepository


class AccountStatementUseCase(BaseModel):
    account_repo: AccountRepository
    customer_repo: CustomerRepository
    transaction_repo: TransactionRepository

    def generate_account_statement(self, account_id: int) -> AccountStatement:
        account = self.account_repo.get(account_id=account_id)
        customer = self.customer_repo.get_by_account_id(
            account_id=account_id)
        transactions = self.transaction_repo.list_by_account_id(
            account_id=account_id)

        return AccountStatement(account=account, customer=customer,
                                transactions=transactions)
