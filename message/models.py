from django.db import models
from django.utils import timezone
from conversations.models import Conversation
# Create your models here.


class Message(models.Model):
    text = models.CharField(max_length=140)
    created_at = models.DateTimeField(default=timezone.now)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, null=True)
