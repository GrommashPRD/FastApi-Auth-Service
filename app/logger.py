import logging
import os
from datetime import datetime
from pythonjsonlogger import json
from app.config import settings

logger = logging.getLogger()

log_file_path = 'logs/app.log'

os.makedirs(os.path.dirname(log_file_path), exist_ok=True)

file_handler = logging.FileHandler(log_file_path)

stream_handler = logging.StreamHandler()

class CustomJSONFormatter(json.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super(CustomJSONFormatter, self).add_fields(log_record, record, message_dict)
        if not log_record.get('timestamp'):
            now = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.')
            log_record['timestamp'] = now

        if log_record.get('level'):
            log_record['level'] = log_record['level'].upper()
        else:
            log_record['level'] = record.levelname

formatter = CustomJSONFormatter(
    "%(timestamp)s %(level)s %(message)s %(module)s %(funcName)s"
)

file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)
logger.setLevel(settings.LOG_LEVEL)