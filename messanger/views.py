from django.shortcuts import render

from rest_framework import viewsets, permissions
from rest_framework.response import Response

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



