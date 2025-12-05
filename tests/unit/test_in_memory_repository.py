
from typing import Optional
from adapters.in_memory_customer_repository import InMemoryCustomerRepository
from domain.model import Customer


def test_repository_initial_empty() -> None:
    repo: InMemoryCustomerRepository = InMemoryCustomerRepository()

    customer: Optional[Customer] = repo.get_customer("abc")

    assert customer is None


def test_repository_save_and_get() -> None:
    repo: InMemoryCustomerRepository = InMemoryCustomerRepository()

    customer_to_save: Customer = Customer("abc", balance=99)
    repo.save_customer(customer_to_save)

    retrieved: Optional[Customer] = repo.get_customer("abc")

    assert retrieved is not None
    assert retrieved.customer_id == "abc"
    assert retrieved.balance == 99


def test_repository_overwrite_existing() -> None:
    repo: InMemoryCustomerRepository = InMemoryCustomerRepository()

    repo.save_customer(Customer("abc", balance=10))
    repo.save_customer(Customer("abc", balance=50))

    retrieved: Optional[Customer] = repo.get_customer("abc")

    assert retrieved is not None
    assert retrieved.balance == 50
