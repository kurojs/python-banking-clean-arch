from pydantic import BaseModel

from core.domain.transaction import Transaction, TransactionType
from core.repository.account import AccountRepository
from core.repository.transaction import TransactionRepository


class TransactionUseCase(BaseModel):
    transaction_repo: TransactionRepository
    account_repo: AccountRepository

    def make_transaction(
            self, account_id: int, amount: float,
            transaction_type: TransactionType
    ) -> Transaction:
        account = self.account_repo.get(account_id=account_id)
        if not account:
            raise Exception("Account not found")

        if transaction_type == TransactionType.WITHDRAW:
            if account.balance < amount:
                raise Exception("Insufficient balance")

        # base on transaction type, update account balance
        if transaction_type == TransactionType.DEPOSIT:
            account.deposit(amount=amount)
        else:
            account.withdraw(amount=amount)

        # update account balance and create transaction
        self.account_repo.save(account=account)
        transaction = Transaction(account_id=account_id, amount=amount,
                                  transaction_type=transaction_type)

        return self.transaction_repo.create(transaction)
