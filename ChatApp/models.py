# chat/models.py
from AuthenticationApp.models import TmcsMember
from django.db import models

class Message(models.Model):
    sender = models.ForeignKey(TmcsMember, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class ChatRoom(models.Model):
    participants = models.ManyToManyField(TmcsMember, related_name='chat_rooms')
    messages = models.ManyToManyField(Message, blank=True)
