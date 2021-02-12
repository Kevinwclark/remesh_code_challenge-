from django import forms


class DateInput(forms.DateInput):
    input_date = 'date'


class ConversationForm(forms.Form):
    title = forms.CharField(max_length=140)
    start_date = forms.DateField(widget=DateInput)\
