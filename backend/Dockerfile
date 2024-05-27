# Backend docker file

FROM python:3.11-bookworm

WORKDIR /home/docker/app

COPY requirements.txt /tmp/requirements.txt
RUN python3 -m pip install -r /tmp/requirements.txt


CMD ["gunicorn", "-c", "gunicorn.conf.py", "backend.wsgi:application"]

EXPOSE 8000
