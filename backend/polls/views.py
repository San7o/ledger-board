from django.shortcuts import render
from django.http import HttpResponse
import json
import logging

logger = logging.getLogger('django')

# Create your views here.
def greet(request):
    return HttpResponse(json.dumps({"message": "Hello, world from backend!"}), content_type="application/json")

from .models import Question

# Query the database to retrive data
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def logging(request):
    logger.debug('This is a debug message')
    logger.info('This is an info message')
    logger.warning('This is a warning message')
    logger.error('This is an error message')
    logger.critical('This is a critical message')
    return HttpResponse("Logging done")

