from django.db import models
from django.utils import timezone
from message.models import Message
# Create your models here.


class Thoughts(models.Model):
    text = models.CharField(max_length=140)
    created_at = models.DateTimeField(default=timezone.now)
    message = models.ForeignKey(Message, on_delete=models.CASCADE, null=True)
