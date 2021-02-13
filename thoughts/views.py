from django.shortcuts import render, reverse, HttpResponseRedirect
from .forms import ThoughtForm
from message.models import Message
from .models import Thoughts
# Create your views here.


def new_thought_view(request, message_id):
    if request.method == "POST":
        form = ThoughtForm(request.POST)
        if form.is_valid():
            message_object = Message.objects.get(id=message_id)
            data = form.cleaned_data
            Thoughts.objects.create(
                text=data['text'],
                message=message_object
            )
            return HttpResponseRedirect(reverse(
                    'message-detail',
                    kwargs={'message_id': message_id}
            ))
    form = ThoughtForm()
    html = 'new_thought.html'
    return render(request, html, {'form': form})


def thought_detail_view(request, thought_id):
    thoughts = Thoughts.objects.get(id=thought_id)
    html = 'thought_detail.html'
    return render(request, html, {'thoughts': thoughts})
