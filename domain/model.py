from dataclasses import dataclass

@dataclass
class Customer:
    customer_id: str
    balance: int = 0