from typing import Optional

from sqlalchemy import ForeignKey, Integer, String, Float
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from core.domain.account import Account
from core.repository.account import AccountRepository


class AccountModel(DeclarativeBase):
    __tablename__ = 'account'
    account_id: Mapped[int] = mapped_column('account_id', Integer,
                                            primary_key=True)
    customer_id: Mapped[int] = mapped_column(
        'customer_id',
        Integer, ForeignKey('customer.customer_id'))
    account_number: Mapped[str] = mapped_column('account_number', String(255))
    balance: Mapped[float] = mapped_column('balance', Float, default=0.0)


class AccountMapper:
    @staticmethod
    def to_domain(account: AccountModel) -> Account:
        return Account(
            account_id=account.account_id,
            customer_id=account.customer_id,
            account_number=account.account_number,
            balance=account.balance,
        )

    @staticmethod
    def to_model(account: Account) -> AccountModel:
        return AccountModel(
            account_id=account.account_id,
            customer_id=account.customer_id,
            account_number=account.account_number,
            balance=account.balance,
        )


class AccountRepositoryImpl(AccountRepository):
    def __init__(self, session):
        self.session = session

    def create(self, account: Account) -> Account:
        account_model = AccountMapper.to_model(account)
        self.session.add(account_model)
        self.session.commit()
        self.session.refresh(account_model)
        return AccountMapper.to_domain(account_model)

    def get(self, account_id: int) -> Optional[Account]:
        account_model = self.session.query(AccountModel).filter(
            AccountModel.account_id == account_id).first()
        if account_model is None:
            return None
        return AccountMapper.to_domain(account_model)

    def save(self, account: Account) -> Account:
        account_model = AccountMapper.to_model(account)
        self.session.merge(account_model)
        self.session.commit()
        self.session.refresh(account_model)
        return AccountMapper.to_domain(account_model)
