from django.shortcuts import render, reverse, HttpResponseRedirect
from .forms import ConversationForm
from .models import Conversation
from message.models import Message

# Create your views here.


def index_view(request):
    html = 'index.html'
    return render(request, html)


def new_conversation_view(request):
    if request.method == "POST":
        form = ConversationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Conversation.objects.create(
                title=data['title'],
                start_date=data['start_date']
            )
            return HttpResponseRedirect(reverse('homepage'))
    form = ConversationForm()
    html = 'conversation.html'
    return render(request, html, {'form': form})


def current_conversations_view(request):
    conversations = Conversation.objects.all()
    html = 'current_conversations.html'
    return render(request, html, {'conversations': conversations})


def conversation_detail_view(request, conversation_id):
    convo = Conversation.objects.get(id=conversation_id)
    messages = Message.objects.filter(conversation=convo)
    html = 'conversation_detail.html'
    return render(request, html, {
        'convo': convo,
        'messages': messages
        })
