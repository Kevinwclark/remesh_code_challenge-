from django.shortcuts import render, reverse, HttpResponseRedirect
from .forms import MessageForm
from .models import Message
# Create your views here.


def new_message_view(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Message.objects.create(
                title=data['title'],
                create_at=data['created_at']
            )
            return HttpResponseRedirect(reverse('convo-detail'))
    form = MessageForm()
    html = 'new_message.html'
    return render(request, html, {'form': form})
