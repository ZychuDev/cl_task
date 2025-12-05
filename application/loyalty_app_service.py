from domain.model import Customer
from domain.ports import CustomerRepository
from domain.loyalty_service import LoyaltyService

class LoyaltyAppService:
    def __init__(self, customer_repository: CustomerRepository):
        self.repository = customer_repository
        self.service = LoyaltyService()

    def earn(self, customer_id: str, points: int) -> int:
        customer: Customer | None = self.repository.get_customer(customer_id)

        if customer is None:
            customer = Customer(customer_id)

        new_balance: int = self.service.earn_points(customer, points)
        self.repository.save_customer(customer)

        return new_balance
    
    def redeem(self, customer_id: str, points: int) -> tuple[int, bool]:
        customer: Customer | None = self.repository.get_customer(customer_id)

        if customer is None:
            raise ValueError("Customer does not exist.")
        
        new_balance, isWarning = self.service.redeem_points(customer, points)
        self.repository.save_customer(customer)

        return new_balance, isWarning