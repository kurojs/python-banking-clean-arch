from core.domain.account import Account
from core.domain.customer import Customer
from core.domain.transaction import TransactionType
from core.usecase.account import AccountUseCase
from core.usecase.account_statement import AccountStatementUseCase
from core.usecase.customer import CustomerUseCase
from core.usecase.transaction import TransactionUseCase


class BankApp:
    account_usecase: AccountUseCase = None
    transaction_usecase: TransactionUseCase = None
    statement_usecase: AccountStatementUseCase = None

    def __init__(self, account_usecase: AccountUseCase,
                 customer_usecase: CustomerUseCase,
                 transaction_usecase: TransactionUseCase,
                 statement_usecase: AccountStatementUseCase):
        self.customer_usecase = customer_usecase
        self.account_usecase = account_usecase
        self.transaction_usecase = transaction_usecase
        self.statement_usecase = statement_usecase

    def create_customer(self, name: str, email: str,
                        phone_number: str) -> Customer:
        return self.customer_usecase.create(name, email, phone_number)

    def create_account(self, customer_id: int) -> Account:
        return self.account_usecase.create_account(customer_id)

    def deposit(self, account_id: int, amount: float):
        return (self.transaction_usecase.make_transaction(
            account_id, amount,
            transaction_type=TransactionType.DEPOSIT)
        )

    def withdraw(self, account_id: int, amount: float):
        return (self.transaction_usecase.make_transaction(
            account_id, amount,
            transaction_type=TransactionType.WITHDRAW)
        )

    def get_statement(self, account_id: int):
        return self.statement_usecase.get_statements(account_id)

    def get_customer(self, customer_id):
        return self.customer_usecase.get_customer(customer_id)
