"""File contains the views for the Django app."""

# from django.shortcuts import render
import logging
from django.http import HttpResponse
from django.http import JsonResponse
from asgiref.sync import sync_to_async
from .models import Question

logger = logging.getLogger('django')


# Create your views here.
async def greet(request):
    """Return a JSON response with a greeting."""
    return JsonResponse({"message": "Hello, world from backend!"})


# Query the database to retrive data
async def index(request):
    """Return a JSON response with the latest questions."""
    output = "Questions:\n"
    latest_question_list = Question.objects.order_by("-pub_date")[:5]

    def get_output(output):
        output += ", ".join([q.question_text for q in latest_question_list])
        return output
    output = await sync_to_async(get_output)(output)
    return HttpResponse(output)


async def test_logs(request):
    """Test the logging functionality."""
    logger.debug('This is a debug message')
    logger.info('This is an info message')
    logger.warning('This is a warning message')
    logger.error('This is an error message')
    logger.critical('This is a critical message')
    return HttpResponse("Logging done")
