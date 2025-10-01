from django.urls import path, include

from rest_framework_simplejwt.views import TokenRefreshView

from .views import MyTokenObtainPairView, UserRegistrationView, UserNotifications


urlpatterns = [
    path('notifications/', UserNotifications.as_view(), name='notifications-list'),
    path('notifications/<int:pk>/', UserNotifications.as_view(), name='notification-detail'),
]

