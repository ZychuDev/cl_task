import click
from application.loyalty_app_service import LoyaltyAppService

@click.group()
@click.pass_context
def cli(ctx: click.Context):
    """Customer Loyalty System CLI"""
    pass

@cli.command()
@click.argument("customer_id")
@click.argument("points", type=int)
@click.pass_context
def earn(ctx: click.Context, customer_id: str, points: int):
    service: LoyaltyAppService = ctx.obj["service"]

    new_balance = service.earn(customer_id, points)
    click.echo(f"Customer {customer_id} earned {points} points. New balance: {new_balance}")

@cli.command()
@click.argument("customer_id")
@click.argument("points", type=int)
@click.pass_context
def redeem(ctx: click.Context, customer_id: str, points: int):
    service: LoyaltyAppService = ctx.obj["service"]

    try:
        new_balance, low_balance = service.redeem(customer_id, points)
        click.echo(f"Customer {customer_id} redeemed {points}. New balance: {new_balance}")

        if low_balance:
            click.echo(f"Warning: Customer {customer_id} has a low balance: {new_balance} points.")

    except ValueError as e:
        click.echo(f"Error: {str(e)}")

@cli.command()
@click.pass_context
def repl(ctx: click.Context):
    """Run multiple commands in one session."""
    service = ctx.obj["service"]

    click.echo("Entering REPL mode. Type 'exit' to quit.")

    while True:
        command = input("> ").strip()

        if command in ("exit", "quit"):
            break

        parts = command.split()

        if len(parts) < 1:
            continue

        cmd = parts[0]

        if cmd == "earn" and len(parts) == 3:
            customer_id = parts[1]
            points = int(parts[2])
            new_balance = service.earn(customer_id, points)
            click.echo(f"Customer {customer_id} earned {points}. Balance: {new_balance}")

        elif cmd == "redeem" and len(parts) == 3:
            customer_id = parts[1]
            points = int(parts[2])
            try:
                new_balance, low = service.redeem(customer_id, points)
                click.echo(f"Customer {customer_id} redeemed {points}. Balance: {new_balance}")
                if low:
                    click.echo(f"WARNING: Low balance ({new_balance})")
            except ValueError as e:
                click.echo(f"Error: {e}")

        else:
            click.echo("Unknown command.")


