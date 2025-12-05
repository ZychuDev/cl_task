# Loyalty Points App

### Creating virtual env and installing dependencies
python -m venv venv

pip install -r requirements.txt

### Earn points

python main.py earn user123 100

### Redeem points

python main.py redeem user123 50

### For running multiple commands on non-persistent repo use repl mode

python main.py repl

## Run tests

pytest

pytest tests/unit

pytest tests/integration
