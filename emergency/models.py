from asyncio.windows_events import NULL
from queue import Empty
from django.db import models

# Create your models here.

from embed_video.fields import EmbedVideoField

class Container(models.Model):
    title = models.CharField(max_length=100)
    brief = models.CharField(max_length=400)
    measures = models.CharField(max_length=1000)
    video = EmbedVideoField()  # same like models.URLField()



    
