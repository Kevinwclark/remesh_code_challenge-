from django import forms
# from .models import Conversation


class MessageForm(forms.Form):
    text = forms.CharField(max_length=140)
