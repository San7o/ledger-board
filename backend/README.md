# Backend

This is the code of the backend. You can run a test server with:
```bash
python3 manage.py runserver
```
This will create a simple web server. This should not be used in production.

With `python3 manage.py` we can access many commands for administration purposes, such as:
- `runserver`: Starts the development server.
- `startapp`: Creates a new Django app within your project.
- `makemigrations`: Generates database migration files based on model changes.
- `migrate`: Applies database migrations to the database.
- `createsuperuser`: Creates a superuser for administrative access to the Django admin interface.
- `collectstatic`: Collects static files from all installed apps into one location.
- `shell`: Opens up a Python shell with Django environment loaded.
- `test`: Runs tests for your Django application.
- `dumpdata`: Dumps data from the database into JSON or YAML format.
- `loaddata`: Loads data from a JSON or YAML file into the database.

## Gunicorn

For producttion we need to use a more performant WSGI. This project uses `gunicorn`. You can run the server with a configuration file with the following command:
```bash
gunicorn -c gunicorn.conf.py backend.asgi:application -k uvicorn.workers.UvicornWorker
```
- `gunicorn.conf.py` is the config file. We specify the number of workers, threads, security and other values.
- `backend.asgi` is the entry point for the application
- `-k uvicorn.workers.UviconrWorker` use uvicorn for async requests

## Linter

I configured a linter, Prospector, which aggregates a certain number of other python linters. Before committing, please run the following to analyze the code inside the backend directory:
```bash
prospector
```

## Tests

Run tests with:
```bash
python3 manage.py test
```

## Django

Django is a feature rich framework, to learn more, check out my notes when learning about django in 'notes/setting-up.md`

## Celery

The application uses celery to manage tasks. Basically, for any kind of computation, we call a task that will be executed bu a worker asynchronously. All the tasks and the Celery configuration is inside `celeryApp`.

To run a worker, use the following command:
```bash
celery -A celeryApp worker -l INFO
```
