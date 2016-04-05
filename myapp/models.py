from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


# Create your models here.


class Board(models.Model):
    title = models.CharField(max_length=200)
    VIDEO = 'vid'
    IMAGE = 'img'
    MEDIA_CHOICES = ((VIDEO, 'video'), (IMAGE, 'image'),)
    media_type = models.CharField(max_length=3, choices=MEDIA_CHOICES, default=IMAGE)
    caption = models.TextField()
    recorded_date = models.DateField(default=timezone.now)
