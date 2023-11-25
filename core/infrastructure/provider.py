from sqlalchemy import Engine
from sqlalchemy.orm import sessionmaker, scoped_session

from core.infrastructure.postgres import migrate
from core.infrastructure.postgres.account import PgAccountRepository
from core.infrastructure.postgres.customer import PgCustomerRepository
from core.infrastructure.postgres.transaction import PgTransactionRepository
from core.repository.account import AccountRepository
from core.repository.customer import CustomerRepository
from core.repository.transaction import TransactionRepository
from core.setting import setting
from core.setting.db.postgres import initialize_postgres_db

ErrInvalidDBDriver = Exception('DB_DRIVER not supported')


class RepositoryProvider:
    _account_repo: AccountRepository = None
    _transaction_repo: TransactionRepository = None
    _customer_repo: CustomerRepository = None
    engine: Engine = None

    def __init__(self):
        if setting.DB_DRIVER == 'postgres' or setting.DB_DRIVER == 'postgresql':
            self.engine = initialize_postgres_db()
            self.session = scoped_session(sessionmaker(bind=self.engine))
            migrate()

            self._account_repo = PgAccountRepository(self.engine, self.session)
            self._transaction_repo = PgTransactionRepository(self.engine, self.session)
            self._customer_repo = PgCustomerRepository(self.engine, self.session)
        else:
            raise ErrInvalidDBDriver

    def account_repo(self) -> AccountRepository:
        return self._account_repo

    def transaction_repo(self) -> TransactionRepository:
        return self._transaction_repo

    def customer_repo(self) -> CustomerRepository:
        return self._customer_repo
