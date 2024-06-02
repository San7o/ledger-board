"""Tests the greet view."""
from django.test import TestCase

# Create your tests here.


class TestGreet(TestCase):

    """Tests for the greet view."""

    def test_greet(self):
        """Test the greet view."""
        response = self.client.get('/api/sender/greet')
        self.assertEqual(response.status_code, 200)
