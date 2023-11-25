from core.domain.account_statement import AccountStatement
from core.repository.account import AccountRepository
from core.repository.customer import CustomerRepository
from core.repository.transaction import TransactionRepository


class AccountStatementUseCase:
    account_repo: AccountRepository
    customer_repo: CustomerRepository
    transaction_repo: TransactionRepository

    def __init__(self, account_repo: AccountRepository,
                 customer_repo: CustomerRepository,
                 transaction_repo: TransactionRepository):
        self.account_repo = account_repo
        self.customer_repo = customer_repo
        self.transaction_repo = transaction_repo

    def generate_account_statement(self, account_id: int) -> AccountStatement:
        account = self.account_repo.get(account_id=account_id)
        customer = self.customer_repo.get_by_account_id(
            account_id=account_id)
        transactions = self.transaction_repo.list_by_account_id(
            account_id=account_id)

        return AccountStatement(account=account, customer=customer,
                                transactions=transactions)

    def get_statements(self, account_id):
        account = self.account_repo.get(account_id=account_id)
        customer = self.customer_repo.get_by_account_id(account_id=account_id)
        transactions = self.transaction_repo.list_by_account_id(account_id)
        return AccountStatement(account=account, customer=customer,
                                transactions=transactions)
