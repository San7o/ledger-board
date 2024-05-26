from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def greet(request):
    return HttpResponse("Hello, world. You're at the polls index.")

from .models import Question

# Query the database to retrive data
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.question_text for q in latest_question_list])
    return HttpResponse(output)
