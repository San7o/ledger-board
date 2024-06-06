
from django.test import TestCase
from sender.utils.checks import check_date, check_amount, check_fields, check_currency


class TestChekcs(TestCase):
    """Tests for the checks functions.

    Functions:
        - test_check_date
        - test_check_amount
        - test_check_fields
        - test_check_currency

    """

    def test_check_date(self):
        """The date must be in the format YYYY/MM/DD."""
        # True cases
        self.assertTrue(check_date("2000/01/01"))
        self.assertTrue(check_date("1999/10/07"))

        # False cases
        self.assertFalse(check_date(""))
        self.assertFalse(check_date("2000-01-01"))
        self.assertFalse(check_date("2000/01/01/01"))
        self.assertFalse(check_date("01/01/2000"))
        self.assertFalse(check_date("01/01/00"))
        self.assertFalse(check_date("01-01-2000"))

        # Wrong year
        self.assertFalse(check_date("199/10/10"))
        self.assertFalse(check_date("19999/10/10"))

        # Wrong month
        self.assertFalse(check_date("1999/70/10"))

        # Wrong day
        self.assertFalse(check_date("1999/10/70"))

    def test_check_amount(self):
        """The amount must be either an integer or a float."""
        # True cases
        self.assertTrue(check_amount("100"))
        self.assertTrue(check_amount("100.00"))
        self.assertTrue(check_amount("100.01"))
        self.assertTrue(check_amount("0.01"))
        self.assertTrue(check_amount("0.00"))
        self.assertTrue(check_amount("0"))
        self.assertTrue(check_amount("100"))

        # False cases
        self.assertFalse(check_amount(""))
        self.assertFalse(check_amount("test"))
        self.assertFalse(check_amount("100.0.0"))
        self.assertFalse(check_amount("10test"))
        self.assertFalse(check_amount("test10"))

    def test_check_fields(self):
        """The json must contain the following fields:
            - date,
            - payee,
            - amount,
            - currency,
            - expenses_account,
            - assets_account.
        """
        # True cases
        self.assertTrue(check_fields({
            "date": "2000/01/01",
            "payee": "Name of the payee",
            "amount": "100.00",
            "currency": "EUR",
            "expenses_account": "Expenses:Account",
            "assets_account": "Assets:Account"
        }))

        self.assertTrue(check_fields({
            "date": "1996/03/05",
            "payee": "Zio Peppe",
            "amount": "10000.50",
            "currency": "USD",
            "expenses_account": "Spesuccie",
            "assets_account": "Cassa"
        }))

        # False cases
        self.assertFalse(check_fields({
            "date": "2000/01/01",
            "payee": "Name of the payee",
            "amount": "100.00",
            "currency": "EUR",
            "expenses_account": "Expenses:Account"
        }))

        self.assertFalse(check_fields({
            "date": "2000/01/01",
            "payee": "Name of the payee",
            "amount": "100.00",
            "expenses_account": "Expenses:Account",
            "assets_account": "Assets:Account"
        }))

        self.assertFalse(check_fields({
            "date": "2000/01/01",
            "payee": "Name of the payee",
            "amount": "100.00",
            "currency": "EUR",
            "assets_account": "Assets:Account"
        }))

        self.assertFalse(check_fields({
            "date": "2000/01/01",
            "payee": "Name of the payee",
            "amount": "100.00",
            "currency": "EUR",
            "expenses_account": "Expenses:Account",
            "assets_account": "Assets:Account",
            "other": "other"
        }))

    def test_check_currency(self):
        """The currency must be one of the following:
            - USD = "$"         # United States Dollar
            - EUR = "€"         # Euro
            - GBP = "£"         # British Pound
            - JPY = "¥"         # Japanese Yen
            - CHF = "CHF"       # Swiss Franc
            - CAD = "$"         # Canadian Dollar
            - AUD = "$"         # Australian Dollar
        """
        # True cases
        self.assertTrue(check_currency("USD"))
        self.assertTrue(check_currency("EUR"))
        self.assertTrue(check_currency("GBP"))
        self.assertTrue(check_currency("JPY"))
        self.assertTrue(check_currency("CHF"))
        self.assertTrue(check_currency("CAD"))
        self.assertTrue(check_currency("AUD"))
        self.assertTrue(check_currency("Other"))

        self.assertTrue(check_currency("$"))
        self.assertTrue(check_currency("€"))
        self.assertTrue(check_currency("£"))
        self.assertTrue(check_currency("¥"))
        self.assertTrue(check_currency("OTHER"))

        # False cases
        self.assertFalse(check_currency(""))
        self.assertFalse(check_currency("test"))
        self.assertFalse(check_currency("usd"))
        self.assertFalse(check_currency("Usd"))
