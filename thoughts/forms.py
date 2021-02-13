from django import forms


class ThoughtForm(forms.Form):
    text = forms.CharField(max_length=140)
