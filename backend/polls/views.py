from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.
def greet(request):
    return HttpResponse(json.dumps({"message": "Hello, world from backend!"}), content_type="application/json")

from .models import Question

# Query the database to retrive data
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.question_text for q in latest_question_list])
    return HttpResponse(output)
