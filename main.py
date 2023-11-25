from fastapi import FastAPI

from core.app.bank import BankApp
from core.domain.customer import Customer
from core.infrastructure.provider import RepositoryProvider
from core.usecase.account import AccountUseCase
from core.usecase.account_statement import AccountStatementUseCase
from core.usecase.customer import CustomerUseCase
from core.usecase.transaction import TransactionUseCase

app = FastAPI()
provider = RepositoryProvider()
bank_app = BankApp(
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


@app.get("/")
def read_root():
    return {
        "code": 200,
        "message": "Success",
    }


@app.post("/customers")
def create_customer(customer: Customer):
    customer = bank_app.create_customer(name=customer.name,
                                        email=customer.email,
                                        phone_number=customer.phone_number)
    return {
        "code": 200,
        "message": "Success",
        "data": customer,
    }


@app.get("/customers/{customer_id}")
def get_customer(customer_id: int):
    customer = bank_app.get_customer(customer_id=customer_id)
    return {
        "code": 200,
        "message": "Success",
        "data": customer,
    }


@app.post("/accounts")
def create_account(customer_id: int):
    account = bank_app.create_account(customer_id=customer_id)
    return {
        "code": 200,
        "message": "Success",
        "data": account,
    }


@app.post("/accounts/{account_id}/deposit")
def deposit(account_id: int, amount: float):
    transaction = bank_app.deposit(account_id=account_id, amount=amount)
    return {
        "code": 200,
        "message": "Success",
        "data": transaction,
    }


@app.post("/accounts/{account_id}/withdraw")
def withdraw(account_id: int, amount: float):
    transaction = bank_app.withdraw(account_id=account_id, amount=amount)
    return {
        "code": 200,
        "message": "Success",
        "data": transaction,
    }


@app.get("/accounts/{account_id}/statement")
def get_statement(account_id: int):
    statement = bank_app.get_statement(account_id=account_id)
    return {
        "code": 200,
        "message": "Success",
        "data": statement,
    }
