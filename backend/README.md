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
gunicorn -c gunicorn.conf.py backend.wsgi:application
```
- `gunicorn.conf.py` is the config file. We specify the number of workers, threads, security and other values.
- `backend.wsgi` is the entry point for the application

## Django

Django is a feature rich framework, to learn more, check out my notes when learning about django in 'notes/setting-up.md`
