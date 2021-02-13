from django.contrib import admin

# Register your models here.
from conversations.models import Conversation
from message.models import Message
from thoughts.models import Thoughts

admin.site.register(Conversation)
admin.site.register(Message)
admin.site.register(Thoughts)
