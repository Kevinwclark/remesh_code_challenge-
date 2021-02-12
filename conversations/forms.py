from django import forms
# from .models import Conversation


class ConversationForm(forms.Form):
    title = forms.CharField(max_length=140)
    start_date = forms.DateField(
            required=True,
            help_text="Format: DD/MM/YYYY",
            input_formats=['%d/%m/%Y']
            )
