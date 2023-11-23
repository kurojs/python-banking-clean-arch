from typing import Optional

from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from core.domain.customer import Customer
from core.infrastructure.postgres.account import AccountModel
from core.repository.customer import CustomerRepository


class Base(DeclarativeBase):
    pass


class CustomerModel(Base):
    __tablename__ = 'customer'
    customer_id: Mapped[int] = mapped_column('customer_id', Integer,
                                             primary_key=True)
    name: Mapped[str] = mapped_column('name', String(255))
    email: Mapped[str] = mapped_column('email', String(255))
    phone_number: Mapped[str] = mapped_column('phone_number', String(255))


class CustomerMapper:
    @staticmethod
    def to_domain(customer: CustomerModel) -> Customer:
        return Customer(
            customer_id=customer.customer_id,
            name=customer.name,
            email=customer.email,
            phone_number=customer.phone_number,
        )

    @staticmethod
    def to_model(customer: Customer) -> CustomerModel:
        return CustomerModel(
            customer_id=customer.customer_id,
            name=customer.name,
            email=customer.email,
            phone_number=customer.phone_number,
        )


class CustomerRepositoryImpl(CustomerRepository):
    def __init__(self, session):
        self.session = session

    def create(self, customer: Customer) -> Customer:
        customer_model = CustomerMapper.to_model(customer)
        self.session.add(customer_model)
        self.session.commit()
        self.session.refresh(customer_model)
        return CustomerMapper.to_domain(customer_model)

    def get(self, customer_id: int) -> Optional[Customer]:
        customer_model = self.session.query(CustomerModel).filter(
            CustomerModel.customer_id == customer_id).first()
        if customer_model is None:
            return None
        return CustomerMapper.to_domain(customer_model)

    def get_by_account_id(self, account_id: int) -> Optional[Customer]:
        customer_model = self.session.query(CustomerModel).filter(
            AccountModel.account_id == account_id).first()
        if customer_model is None:
            return None
        return CustomerMapper.to_domain(customer_model)
