from core.domain.customer import Customer
from core.repository.customer import CustomerRepository


class CustomerUseCase:
    customer_repo: CustomerRepository

    def __init__(self, customer_repo: CustomerRepository):
        self.customer_repo = customer_repo

    def create(self, name: str, email: str, phone_number: str):
        customer = Customer(name=name, email=email, phone_number=phone_number)
        return self.customer_repo.create(customer)

    def get_customer(self, customer_id):
        return self.customer_repo.get(customer_id)
