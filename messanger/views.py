from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import ChatListSerializer
from .models import Chat
# Create your views here.


class ChatView(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatListSerializer
