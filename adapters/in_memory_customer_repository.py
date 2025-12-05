from domain.ports import CustomerRepository
from domain.model import Customer


class InMemoryCustomerRepository(CustomerRepository):

    def __init__(self):
        self._store = {}

    def get_customer(self, customer_id: str) -> Customer | None:
        return self._store.get(customer_id)

    def save_customer(self, customer: Customer):
        self._store[customer.customer_id] = customer