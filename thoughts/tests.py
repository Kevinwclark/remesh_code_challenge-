from django.test import TestCase
from message.models import Message
from .models import Thoughts


class ConversationTestCase(TestCase):
    def setUp(self):
        message = Message.objects.create(text="Do you like shrimp")
        Thoughts.objects.create(text="No, I hate them", message=message)
        Thoughts.objects.create(text="Yeah, they are OK", message=message)
        Thoughts.objects.create(text="I can't get enough!", message=message)

    def test_Message_object_creation(self):
        """Tests if Thoughts objects are created"""
        thoughts = Thoughts.objects.all()
        count = thoughts.count()
        self.assertEqual(count, 3)
