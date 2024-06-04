"""Celery configuration file.
Celery will connect to redis DB as a broker and backend.
It will perform tasks defined in the SenderClass.
"""
from celery import Celery

app = Celery('celeryApp',
             broker='redis://:admin@localhost',
             backend='redis://:admin@localhost',
             include=['celeryApp.SenderClass'])

# Disable warning
app.conf.broker_connection_retry_on_startup = True
