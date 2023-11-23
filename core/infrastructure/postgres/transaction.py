from typing import List

from sqlalchemy import Integer, String, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from core.domain.transaction import Transaction
from core.repository.transaction import TransactionRepository


class TransactionModel(DeclarativeBase):
    __tablename__ = 'transaction'
    transaction_id: Mapped[int] = mapped_column('transaction_id', Integer,
                                                primary_key=True)
    account_id: Mapped[int] = mapped_column('account_id', Integer)
    amount: Mapped[float] = mapped_column('amount', Integer)
    transaction_type: Mapped[str] = mapped_column('transaction_type',
                                                  String(255))
    created_at: Mapped[str] = mapped_column('created_at', DateTime)


class TransactionMapper:
    @staticmethod
    def to_domain(transaction: TransactionModel) -> Transaction:
        return Transaction(
            transaction_id=transaction.transaction_id,
            account_id=transaction.account_id,
            amount=transaction.amount,
            transaction_type=transaction.transaction_type,
            created_at=transaction.created_at,
        )

    @staticmethod
    def to_model(transaction: Transaction) -> TransactionModel:
        return TransactionModel(
            transaction_id=transaction.transaction_id,
            account_id=transaction.account_id,
            amount=transaction.amount,
            transaction_type=transaction.transaction_type,
            created_at=transaction.created_at,
        )


class TransactionRepositoryImpl(TransactionRepository):
    def __init__(self, session):
        self.session = session

    def create(self, transaction: Transaction) -> Transaction:
        transaction_model = TransactionMapper.to_model(transaction)
        self.session.add(transaction_model)
        self.session.commit()
        self.session.refresh(transaction_model)
        return TransactionMapper.to_domain(transaction_model)

    def list_by_account_id(self, account_id: int) -> List[Transaction]:
        transaction_models = (self.session.query(TransactionModel)
                              .filter(TransactionModel.account_id == account_id)
                              .order_by(TransactionModel.created_at.desc())
                              .all())
        if transaction_models is None:
            return []
        return [TransactionMapper.to_domain(transaction_model) for
                transaction_model in transaction_models]

