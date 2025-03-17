from django.db import models

# Create your models here.
class Message(models.Model):
    user = models.CharField(max_length=128, blank=False, default='')
    message = models.CharField(max_length=2000, blank=False, default='')
    