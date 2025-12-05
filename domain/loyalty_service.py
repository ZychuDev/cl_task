from domain.model import Customer

class LoyaltyService:
    WARNING_TRESHOLD = 10

    def earn_points(self, customer: Customer, points: int) -> int:
        customer.balance += points
        return customer.balance
    
    def redeem_points(self, customer: Customer, points: int) -> tuple[int, bool]:
        if points > customer.balance:
            raise ValueError("Current balance is insufficient")
        
        customer.balance -= points

        isWarning = customer.balance < self.WARNING_TRESHOLD
        return customer.balance, isWarning