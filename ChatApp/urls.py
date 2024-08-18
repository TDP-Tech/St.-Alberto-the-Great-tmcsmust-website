# chat/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('messages/', views.chat_room, name='chat-messages'),
]
