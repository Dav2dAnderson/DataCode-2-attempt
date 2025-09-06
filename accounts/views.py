from django.shortcuts import render

from rest_framework import views, status, permissions
from rest_framework.response import Response

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken


from .models import BlacklistedAccessToken, Notification
from .serializers import MyTokenObtainPairSerializer, \
    CustomUserRegistrationSerializer, UserNotificationsSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class UserRegistrationView(views.APIView):
    def post(self, request):
        serializer = CustomUserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': "User has been created."
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


""" User Notifications """
class UserNotifications(views.APIView):
    def get(self, request, pk=None):
        if pk is None:
            notifications = Notification.objects.all()
            serializer = UserNotificationsSerializer(notifications, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            try:
                notification = Notification.objects.get(id=pk)
            except Notification.DoesNotExist:
                return Response({'detail': "Not found"}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = UserNotificationsSerializer(notification)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    
