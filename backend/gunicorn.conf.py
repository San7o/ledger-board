import multiprocessing
from backend.settings import LOGGING

# general configuration
bind = '0.0.0.0:8000'
workers = multiprocessing.cpu_count() * 2 + 1
threads = 2
timeout = 30
keepalive = 2
loglevel = 'info'
accesslog = '-'

# security
limit_request_line = 4094
limit_request_fields = 100
limit_request_field_size = 8190

# performance
preload_app = True
worker_tmp_dir = '/dev/shm'
worker_connections = 1000

# Logging
logconfig_dict = LOGGING
logconfig_dict['handlers']['file']['filename'] = "./.logs/gunicorn-logs.log"
