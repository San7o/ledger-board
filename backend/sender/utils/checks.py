"""Utils for checking the correctness of the input data."""

from sender.enums.Currencies import Currencies
import re


def check_fields(json) -> bool:
    """Check if the json contains the required fields."""
    if len(json) != 6:
        return False

    required_fields = [
        "date",
        "payee",
        "amount",
        "currency",
        "expenses_account",
        "assets_account"
    ]

    for field in required_fields:
        if field not in json:
            return False

    return True

def check_currency(currency: str) -> bool:
    """
        Check if the currency is valid.
        Both the symbol and the code are valid.
    """
    for c in Currencies:
        if currency in (c.name, c.value):
            return True

    return False


def check_date(date: str) -> bool:
    """Check if the date is in the correct format."""
    pattern = r'^\d{4}/\d{2}/\d{2}$'
    if not re.match(pattern, date):
        return False

    # Check the month number is between 1 and 12
    month = int(date[5:7])
    if month < 1 or month > 12:
        return False

    # Check the day number is between 1 and 31
    day = int(date[8:10])
    if day < 1 or day > 31:
        return False

    return True


def check_amount(value: str) -> bool:
    """Check if the amount is a valid number."""
    try:

        float(value)
        return True

    except ValueError:
        return False
