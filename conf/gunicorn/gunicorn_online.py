import logging
import logging.handlers
from logging.handlers import WatchedFileHandler
import os
import multiprocessing

bind = "0.0.0.0:8000"
backlog = 512
worker_class = 'sync'
workers = 2
threads = 16
loglevel = 'debug'
# access_log_format = '%'

errorlog = "/tmp/logs/my_project/logs/gunicorn_error.log"
accesslog = "/tmp/logs/my_project/logs/gunicorn_access.log"

proc_name = 'my_project'