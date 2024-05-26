# Setting up

## Nix

I initialized the developement environment with flakes:
```bash
nix flake init --template github:MordragT/nix-templates#python-venv
```

## Django
I instelled django version 5.0.6 through `requirements.txt` and running:
```bash
pip install -r requirements.txt
```

I then created a base project with
```bash
django-admin startproject backend
```

The following directories are created:
- `manage.py`: A command-line utility that lets you interact with this Django project in various ways. You can read all the details about manage.py in django-admin and manage.py.
- The inner `backend/` directory is the actual Python package for your project. Its name is the Python package name you’ll need to use to import anything inside it (e.g. backend.urls).
- `backend/__init__.py`: An empty file that tells Python that this directory should be considered a Python package. If you’re a Python beginner, read more about packages in the official Python docs.
- `backend/settings.py`: Settings/configuration for this Django project. Django settings will tell you all about how settings work.
- `backend/urls.py`: The URL declarations for this Django project; a “table of contents” of your Django-powered site. You can read more about URLs in URL dispatcher.
- `backend/asgi.py`: An entry-point for ASGI-compatible web servers to serve your project. See How to deploy with ASGI for more details.
- `backend/wsgi.py`: An entry-point for WSGI-compatible web servers to serve your project. See How to deploy with WSGI for more details.

I then created an app with
```bash
python3 manage.py startapp polls
```

I added a view in `polls/view.py` with the following content
```python
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

We need to map the view to and url, we can create `poll/urls.py` with the following content:
```python
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]
```

And we add the irl to the backend server in `backend/urls`:
```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]
```

You can run the server with:
```bash
python3 manage.py runserver
```

### Migrations

Django has some installed modules in `backen/settings.py`. Some of them need database tables, to initialize those we can run migrate with:
```bash
python3 manage.py migrate
```

To create a model (to interact with the database) we can write code in `polls/models.py` like this:
```python3
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```

Now we need to apply those changes to the model, by doing a new migration. First, we need to tell Django that polls exists, we ca add this line to INSTALLED_APPS
```python
INSTALLED_APPS = [
    "polls.apps.PollsConfig",
    ...
```

We can make a new migration with
```bash
python3 manage.py makemigrations polls
```

The output looks something like this
```bash
Migrations for 'polls':
  backend/polls/migrations/0001_initial.py
    - Create model Question
    - Create model Choice
```

Migrations are how Django stores changes to your models

You can read the migration diffs with:
```bash
python3 backend/manage.py sqlmigrate polls 0001
```

To create those model tables, run migrate again:
```bash
python3 manage.py migrate
```

Summing up, to make a change to a model you need to:
- Change your models (in `models.py`).
- Run `python manage.py makemigrations` to create migrations for those changes
- Run `python manage.py migrate` to apply those changes to the database.

### Django Admin

Create ad admin user with
```bash
python3 manage.p createsuperuser
```

Then go to `http://localhost:8000/admin` to access the admin board

We can setup models in the admin board by editing `polls/admin.py` and adding entries like this:
```python
from .models import Question

admin.site.register(Question)
```

### Urls

We can define url arguments with this special syntax:
```python
urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
```

Look at this example to uderstand some functionalities
```python
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(rev
```


### Automated Testing

https://docs.djangoproject.com/en/5.0/intro/tutorial05/
