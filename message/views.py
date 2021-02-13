from django.shortcuts import render, reverse, HttpResponseRedirect
from .forms import MessageForm
from .models import Message
from thoughts.models import Thoughts
from conversations.models import Conversation


def new_message_view(request, conversation_id):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            convo = Conversation.objects.get(id=conversation_id)
            data = form.cleaned_data
            Message.objects.create(
                text=data['text'],
                conversation=convo
            )
            return HttpResponseRedirect(reverse(
                'convo-detail',
                kwargs={'conversation_id': conversation_id}
                ))
    form = MessageForm()
    html = 'new_message.html'
    return render(request, html, {'form': form})


def message_detail_view(request, message_id):
    message = Message.objects.get(id=message_id)
    thoughts = Thoughts.objects.filter(message=message)
    html = 'message_detail.html'
    return render(request, html, {
        'message': message,
        'thoughts': thoughts
    })
