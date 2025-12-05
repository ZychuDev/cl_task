from adapters.in_memory_customer_repository import InMemoryCustomerRepository
from adapters.cli import cli
from application.loyalty_app_service import LoyaltyAppService

def app():
    repo = InMemoryCustomerRepository()
    service = LoyaltyAppService(repo)

    cli(obj={"service": service})

if __name__ == "__main__":
    app()