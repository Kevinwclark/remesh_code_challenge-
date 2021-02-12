from django.shortcuts import render

# Create your views here.

# help_text="Please use the following format: <em>YYYY-MM-DD</em>."


def index_view(request):
    html = 'index.html'
    return render(request, html)
