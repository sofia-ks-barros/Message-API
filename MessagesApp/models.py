from django.db import models

class User(models.Model):
    username = models.CharField(max_length=64, blank=False, primary_key=True)
    password = models.CharField(max_length=24, null=False, default='')
    created_date = models.DateTimeField(blank=False, null=False)
    display_name = models.CharField(max_length=128, blank=False, default='')

class Chat(models.Model):
    name = models.CharField(max_length=128, blank=False, default='New group')
    created_date =  models.DateTimeField(blank=False, null=False)
    messages_amount = models.IntegerField(blank=False, default='0')
    
class Message(models.Model):
    user = models.ForeignKey(User, related_name='user', on_delete=models.DO_NOTHING)
    message = models.CharField(max_length=2000, blank=False, default='')
    created_date = models.DateTimeField(blank=False, null=False)
    from_chat = models.ForeignKey(Chat, related_name='chat', on_delete=models.DO_NOTHING, default='')