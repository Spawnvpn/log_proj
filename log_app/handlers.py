import logging
import requests
from django.utils.datetime_safe import datetime


class SpaceHandler(logging.Handler):
    def __init__(self, link, *args, **kwargs):
        self.link = link
        super().__init__(*args, **kwargs)

    def emit(self, record):
        try:
            msg = self.format(record)
            link = self.link
            time = datetime.now()
            name = record.name
            level = record.levelno
            requests.post(link, data={'msg': msg, 'level': level, 'time': time,
                                      'name': name})

        except Exception:
            self.handleError(record)