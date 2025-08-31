from rest_framework import serializers

from .models import Chat


class ChatListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ['id', 'chat_title', 'slug']