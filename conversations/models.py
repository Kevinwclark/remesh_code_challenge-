from django.db import models


class Conversation(models.Model):
    title = models.CharField(max_length=140)
    start_date = models.DateTimeField()
