import pytest

from adapters.in_memory_customer_repository import InMemoryCustomerRepository
from application.loyalty_app_service import LoyaltyAppService

@pytest.fixture
def repo():
    return InMemoryCustomerRepository()

@pytest.fixture
def app_service(repo):
    return LoyaltyAppService(repo)
