"""Test cases for the send_data API."""
from django.test import TestCase
from django.core.cache import cache
from rest_framework.test import RequestsClient
import json

class TestSendData(TestCase):

    """Tests for send_data."""

    def test_send_data_correct(self):
        """Test the send_data API."""

        cache.clear()
        
        client = RequestsClient()
        json_data = json.dumps({
            "date": "2021/01/10",
            "payee": "Name of the payee",
            "amount": "100.00",
            "currency": "€",
            "expenses_account": "Expenses:Account",
            "assets_account": "Assets:Account"
        }).encode('utf-8')

        response = client.post('http://127.0.0.1:8000/api/sender/send', json_data)
        self.assertEqual(response.status_code, 200)

    def test_send_data_correct2(self):
        """Test the send_data API."""

        cache.clear()

        client = RequestsClient()
        json_data = json.dumps({
            "date": "2021/01/01",
            "payee": "Name of the payee",
            "amount": "59",
            "currency": "USD",
            "expenses_account": "Expensess",
            "assets_account": "Assetss"
        }).encode('utf-8')

        response = client.post('http://127.0.0.1:8000/api/sender/send', json_data)
        self.assertEqual(response.status_code, 200)

    def test_send_data_empty(self):
        response = self.client.post('/api/sender/send', {})
        self.assertEqual(response.status_code, 400)


    def test_send_data_missing_fields(self):
        response = self.client.post('http://127.0.0.1:8000/api/sender/send', {
            "date": "2021-01-01",
            "payee": "Name of the payee",
            "amount": "100.00",
            "currency": "EUR",
            "expenses_account": "Expenses:Account"
        })
        self.assertEqual(response.status_code, 400)

    def test_send_data_invalid_currency(self):
        response = self.client.post('http://127.0.0.1:8000/api/sender/send', {
            "date": "2021-01-01",
            "payee": "Name of the payee",
            "amount": "100.00",
            "currency": "EURO",
            "assets_account": "Assets:Account"
        })
        self.assertEqual(response.status_code, 400)

    def test_send_data_invalid_date(self):
        response = self.client.post('http://127.0.0.1:8000/api/sender/send', {
            "date": "2021-40-01",
            "payee": "Name of the payee",
            "amount": "100.00",
            "currency": "EUR",
            "assets_account": "Assets:Account",
            "expenses_account": "Expenses:Account"
        })
        self.assertEqual(response.status_code, 400)

    def test_send_data_invalid_amount(self):
        response = self.client.post('http://127.0.0.1:8000/api/sender/send', {
            "date": "2021-01-01",
            "payee": "Name of the payee",
            "amount": "100.00.00",
            "currency": "EUR",
            "assets_account": "Assets:Account",
            "expenses_account": "Expenses:Account"
        })
        self.assertEqual(response.status_code, 400)

    def test_send_data_invalid_date_format(self):

        response = self.client.post('http://127.0.0.1:8000/api/sender/send', {
            "date": "2021/01/01",
            "payee": "Name of the payee",
            "amount": "100.00",
            "currency": "EUR",
            "assets_account": "Assets:Account",
            "expenses_account": "Expenses:Account"
        })
        self.assertEqual(response.status_code, 400)

