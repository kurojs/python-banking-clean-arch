from typing import Optional

from sqlalchemy import Integer, String, Float, Engine
from sqlalchemy.orm import Mapped, mapped_column, Session, declarative_base

from core.domain.account import Account
from core.repository.account import AccountRepository

Base = declarative_base()


class AccountModel(Base):
    __tablename__ = 'account'

    id: Mapped[int] = mapped_column('id', Integer, primary_key=True)
    customer_id: Mapped[int] = mapped_column('customer_id', Integer)
    account_number: Mapped[str] = mapped_column('account_number', String(255))
    balance: Mapped[float] = mapped_column('balance', Float, default=0.0)


class PgAccountRepository(AccountRepository):
    session: Session

    def __init__(self, engine: Engine, session: Session):
        Base.metadata.create_all(engine)
        self.session = session

    def create(self, account: Account) -> Account:
        account_model = AccountMapper.to_model(account)
        self.session.add(account_model)
        self.session.commit()
        self.session.refresh(account_model)
        return AccountMapper.to_domain(account_model)

    def get(self, account_id: int) -> Optional[Account]:
        account_model = self.session.query(AccountModel).filter(
            AccountModel.id == account_id).first()
        if account_model is None:
            return None
        return AccountMapper.to_domain(account_model)

    def save(self, account: Account) -> Account:
        old_account = (self.session.query(AccountModel)
                       .filter(AccountModel.id == account.id)
                       .first())
        if old_account is None:
            raise Exception("Account not found")

        old_account.balance = account.balance
        old_account.customer_id = account.customer_id
        old_account.account_number = account.account_number
        self.session.merge(old_account)
        self.session.commit()
        self.session.refresh(old_account)
        return AccountMapper.to_domain(old_account)


class AccountMapper:
    @staticmethod
    def to_domain(account: AccountModel) -> Account:
        return Account(
            id=account.id,
            customer_id=account.customer_id,
            account_number=account.account_number,
            balance=account.balance,
        )

    @staticmethod
    def to_model(account: Account) -> AccountModel:
        return AccountModel(
            id=account.id,
            customer_id=account.customer_id,
            account_number=account.account_number,
            balance=account.balance,
        )
