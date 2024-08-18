# chat/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import MessageForm
from .models import Message

@login_required
def chat_room(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender_id = request.user.id
            message.save()
            return redirect('chat-messages')
    else:
        form = MessageForm()
    messages = Message.objects.all()
    return render(request, 'chat_room.html', {'form': form, 'messages': messages})
