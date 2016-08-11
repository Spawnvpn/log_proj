from django.db import models


class LogModel(models.Model):
    log_time = models.DateTimeField()
    log_level = models.CharField(max_length=255)
    log_message = models.CharField(max_length=255)
    log_sender = models.CharField(max_length=255)
    log_name = models.CharField(max_length=255)
