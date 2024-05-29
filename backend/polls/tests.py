"""Tests for the models, views, and forms of the app."""
from django.test import TestCase

# Create your tests here.


class TestCallsView(TestCase):

    """Tests for the CallsView."""

    def test_logging(self):
        """Test that the logging is working."""
        response = self.client.get('/api/logging')
        self.assertEqual(response.status_code, 200)
