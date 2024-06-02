"""Define the views for the backend receiver."""
from django.http import JsonResponse

# Create your views here.


async def greet(_):
    """Return a JSON response with a greeting."""
    return JsonResponse({"message": "Hello, world from backend sender!"})
