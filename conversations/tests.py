from django.test import TestCase
from .models import Conversation
from django.shortcuts import reverse


class ConversationTestCase(TestCase):
    def setUp(self):
        Conversation.objects.create(title="Shrimp Tacos", start_date="2021-02-12")
        Conversation.objects.create(title="Pizza", start_date="2021-08-08")

    def test_Conversation_object_creation(self):
        """Tests if Conversation objects are created"""
        shrimp = Conversation.objects.get(title="Shrimp Tacos")
        tacos = Conversation.objects.get(title="Pizza")
        self.assertTrue(shrimp)
        self.assertTrue(tacos)

    def test_current_conversations_view(self):
        """Tests current_conversations_view"""
        url = reverse("current-conversation")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

    def test_conversation_detail_view(self):
        """Tests conversation_detail_view"""
        conversation = Conversation.objects.get(title="Shrimp Tacos")
        conversation_id = conversation.id
        url = reverse(
            "convo-detail",
            kwargs={'conversation_id': conversation_id}
        )
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
