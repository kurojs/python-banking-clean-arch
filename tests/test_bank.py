from unittest import TestCase

from sqlalchemy.orm import declarative_base

from core.app.bank import BankApp
from core.infrastructure.provider import RepositoryProvider
from core.setting import setting
from core.usecase.account import AccountUseCase
from core.usecase.account_statement import AccountStatementUseCase
from core.usecase.customer import CustomerUseCase
from core.usecase.transaction import TransactionUseCase


class TestStringMethods(TestCase):
    app: BankApp = None

    def setUp(self):
        self.configure()

        provider = RepositoryProvider()

        # Clear database
        Base = declarative_base()
        Base.metadata.drop_all(provider.engine)

        self.app = BankApp(
            account_usecase=AccountUseCase(
                account_repo=provider.account_repo(),
                customer_repo=provider.customer_repo(),
            ),
            customer_usecase=CustomerUseCase(
                customer_repo=provider.customer_repo(),
            ),
            transaction_usecase=TransactionUseCase(
                account_repo=provider.account_repo(),
                transaction_repo=provider.transaction_repo(),
            ),
            statement_usecase=AccountStatementUseCase(
                account_repo=provider.account_repo(),
                customer_repo=provider.customer_repo(),
                transaction_repo=provider.transaction_repo(),
            )
        )

    def configure(self):
        setting.DB_DRIVER = 'postgres'
        setting.DB_HOST = 'localhost'
        setting.DB_PORT = 5432
        setting.DB_USER = 'postgres'
        setting.DB_PASSWORD = 'postgres'
        setting.DB_NAME = 'postgres'

    def test_full_flow(self):
        customer = self.app.create_customer(
            name='John Doe',
            email='john@gmail.com',
            phone_number='0000000001',
        )
        self.assertIsNotNone(customer.id)
        self.assertEqual(customer.name, 'John Doe')
        self.assertEqual(customer.email, 'john@gmail.com')
        self.assertEqual(customer.phone_number, '0000000001')

        account = self.app.create_account(
            customer_id=customer.id,
        )
        self.assertIsNotNone(account.id)
        self.assertEqual(account.customer_id, customer.id)
        self.assertEqual(account.balance, 0)
        self.assertIsNotNone(account.account_number)

        self.app.deposit(
            account_id=account.id,
            amount=100,
        )

        statement = self.app.statement_usecase.get_statements(account.id)
        self.assertEqual(len(statement.transactions), 1)
        self.assertEqual(statement.transactions[0].amount, 100)

        self.app.withdraw(
            account_id=account.id,
            amount=50,
        )
        statement = self.app.statement_usecase.get_statements(account.id)
        self.assertEqual(len(statement.transactions), 2)
        self.assertEqual(statement.transactions[1].amount, 50)
        return account
