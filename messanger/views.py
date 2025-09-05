from django.shortcuts import render

from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action

from .serializers import ChatListSerializer, ChatRetrieveSerializer, MessageSerializer
from .models import Chat, Messages
# Create your views here.


class ChatView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Chat.objects.all()
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.action == 'list':
            return ChatListSerializer
        return ChatRetrieveSerializer
    
    def get_queryset(self):
        user = self.request.user
        return Chat.objects.filter(participants=user)

    @action(detail=True, methods=['GET'], url_path='messages', url_name='messages')
    def messages(self, request, slug=None):
        chat = self.get_object()
        messages = Messages.objects.filter(chat=chat).order_by("-date")
        if messages.exists():
            serializer = MessageSerializer(messages, many=True)
            return Response(serializer.data)
        return Response("Messages not found", status=status.HTTP_404_NOT_FOUND)
