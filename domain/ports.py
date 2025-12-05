from abc import ABC, abstractmethod
from domain.model import Customer

class CustomerRepository(ABC):
    @abstractmethod
    def get_customer(self, customer_id: str) -> Customer | None:
        pass

    @abstractmethod
    def save_customer(self, customer: Customer):
        pass