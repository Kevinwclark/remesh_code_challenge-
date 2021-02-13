from django.test import TestCase
from conversations.models import Conversation
from .models import Message


class ConversationTestCase(TestCase):
    def setUp(self):
        convo = Conversation.objects.create(title="Shrimp Tacos", start_date="2021-02-12")
        Message.objects.create(text="Do you like shrimp?", conversation=convo)
        Message.objects.create(text="Do you like tacos?", conversation=convo)
        Message.objects.create(text="Do you like lettuce on tacos?", conversation=convo)

    def test_Message_object_creation(self):
        """Tests if Message objects are created"""
        messages = Message.objects.all()
        count = messages.count()
        self.assertEqual(count, 3)
