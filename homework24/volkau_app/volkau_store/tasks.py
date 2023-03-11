from datetime import datetime
from .models import Log
from celery import shared_task

import logging

logger = logging.getLogger('store')



@shared_task()
def log_store(path, user, time):
    time = datetime.now()
    message_log = f'{time} | {path} | {user}'
    logger.info(message_log)
    log = Log()
    log.log_text = message_log
    log.save()
