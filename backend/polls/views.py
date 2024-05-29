from django.shortcuts import render
from django.http import HttpResponse
from asgiref.sync import sync_to_async
import json
import logging

logger = logging.getLogger('django')

# Create your views here.
async def greet(request):
    return HttpResponse(json.dumps({"message": "Hello, world from backend!"}), content_type="application/json")

from .models import Question

# Query the database to retrive data
async def index(request):
    output = "Questions:\n"
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    def getOutput(output):
        output += ", ".join([q.question_text for q in latest_question_list])
        return output
    output = await sync_to_async(getOutput)(output)
    return HttpResponse(output)

async def logging(request):
    logger.debug('This is a debug message')
    logger.info('This is an info message')
    logger.warning('This is a warning message')
    logger.error('This is an error message')
    logger.critical('This is a critical message')
    return HttpResponse("Logging done")

