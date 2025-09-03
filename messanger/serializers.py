from rest_framework import serializers

from .models import Chat, Messages

from accounts.models import CustomUser


class ChatParticipantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'username', 'first_name', 'last_name'
        ]


class ChatListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ['id', 'chat_title', 'slug']


class ChatRetrieveSerializer(serializers.ModelSerializer):
    participants = ChatParticipantsSerializer(many=True)
    class Meta:
        model = Chat
        fields = ['id', 'chat_title', 'slug', 'participants']


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = ['chat', 'user', 'message']