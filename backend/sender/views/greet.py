"""The module contains a single function that returns a greeting message."""
from django.http import JsonResponse

async def greet(_):
    """Return a JSON response with a greeting."""
    return JsonResponse({"message": "Hello, world from backend sender!"})
