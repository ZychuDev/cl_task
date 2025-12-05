import pytest

from application.loyalty_app_service import LoyaltyAppService
from adapters.in_memory_customer_repository import InMemoryCustomerRepository
from domain.model import Customer


@pytest.fixture
def repo() -> InMemoryCustomerRepository:
    return InMemoryCustomerRepository()


@pytest.fixture
def app_service(repo: InMemoryCustomerRepository) -> LoyaltyAppService:
    return LoyaltyAppService(repo)


def test_app_service_earn_creates_customer(
    app_service: LoyaltyAppService,
    repo: InMemoryCustomerRepository
) -> None:
    assert repo.get_customer("user1") is None

    new_balance: int = app_service.earn("user1", 50)

    assert new_balance == 50
    customer: Customer | None = repo.get_customer("user1")
    assert customer is not None
    assert customer.balance == 50


def test_app_service_redeem_success(
    app_service: LoyaltyAppService,
) -> None:
    app_service.earn("user1", 100)

    new_balance, low_warning = app_service.redeem("user1", 40)

    assert new_balance == 60
    assert low_warning is False


def test_app_service_redeem_low_balance(
    app_service: LoyaltyAppService,
) -> None:
    app_service.earn("user1", 12)

    new_balance, low_warning = app_service.redeem("user1", 5)

    assert new_balance == 7
    assert low_warning is True


def test_app_service_redeem_unknown_customer(
    app_service: LoyaltyAppService
) -> None:
    with pytest.raises(ValueError):
        app_service.redeem("unknown", 10)
