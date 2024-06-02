"""File containing all the enums for the sender app.

The file contains:
- Currencies
"""
from enum import Enum

class Currencies(Enum):

    """Enum for the allowed currencies."""

    USD = "$"         # United States Dollar
    EUR = "€"         # Euro
    GBP = "£"         # British Pound
    JPY = "¥"         # Japanese Yen
    CHF = "CHF"       # Swiss Franc
    CAD = "CAD"       # Canadian Dollar
    AUD = "AUD"       # Australian Dollar
