import pytest

from domain.model import Customer
from domain.loyalty_service import LoyaltyService

def test_earn_points() -> None:
    service: LoyaltyService = LoyaltyService()
    customer: Customer = Customer("user1", balance=10)

    new_balance: int = service.earn_points(customer, 20)

    assert new_balance == 30
    assert customer.balance == 30


def test_redeem_points_success() -> None:
    service: LoyaltyService = LoyaltyService()
    customer: Customer = Customer("user1", balance=50)

    new_balance, low_warning = service.redeem_points(customer, 20)

    assert new_balance == 30
    assert low_warning is False
    assert customer.balance == 30


def test_redeem_points_low_balance_warning() -> None:
    service: LoyaltyService = LoyaltyService()
    customer: Customer = Customer("user1", balance=12)

    new_balance, low_warning = service.redeem_points(customer, 5)

    assert new_balance == 7
    assert low_warning is True


def test_redeem_points_insufficient_balance() -> None:
    service: LoyaltyService = LoyaltyService()
    customer: Customer = Customer("user1", balance=5)

    with pytest.raises(ValueError):
        service.redeem_points(customer, 10)
